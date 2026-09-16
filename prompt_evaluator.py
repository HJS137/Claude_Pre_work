"""
prompt_evaluator.py

A working equivalent of the PromptEvaluator class used in the Claude Academy
prompt engineering lessons. Matches the lesson's API:

    evaluator = PromptEvaluator(max_concurrent_tasks=3)
    dataset = evaluator.generate_dataset(...)
    results = evaluator.run_evaluation(...)

Uses threads rather than asyncio so it works the same in a notebook or a script.
"""

import html
import json
from concurrent.futures import ThreadPoolExecutor

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()
MODEL = "claude-haiku-4-5-20251001"


# --- helpers -------------------------------------------------------------

def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})


def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})


def chat(messages, system=None, stop_sequences=None, max_tokens=4000):
    params = {"model": MODEL, "max_tokens": max_tokens, "messages": messages}
    if system:
        params["system"] = system
    if stop_sequences:
        params["stop_sequences"] = stop_sequences

    message = client.messages.create(**params)
    if message.stop_reason == "max_tokens":
        print("WARNING: response truncated - raise max_tokens")
    return message.content[0].text


def _json_chat(prompt):
    """Ask for JSON, using prefill + stop sequence, and parse it."""
    messages = []
    add_user_message(messages, prompt)
    add_assistant_message(messages, "```json")
    text = chat(messages, stop_sequences=["```"])
    return json.loads(text.strip())


# --- the evaluator -------------------------------------------------------

class PromptEvaluator:
    def __init__(self, max_concurrent_tasks=3):
        self.max_concurrent_tasks = max_concurrent_tasks

    def generate_dataset(
        self,
        task_description,
        prompt_inputs_spec,
        output_file=None,
        num_cases=3,
    ):
        spec = "\n".join(f'- "{k}": {v}' for k, v in prompt_inputs_spec.items())
        example = ", ".join(f'"{k}": "..."' for k in prompt_inputs_spec)

        prompt = f"""
Generate an evaluation dataset for this task:

{task_description}

Each test case is a JSON object with these fields:
{spec}

Output a JSON array of {num_cases} objects, varied and realistic.

Example shape:
[
  {{{example}}}
]

Output only the JSON array.
"""
        dataset = _json_chat(prompt)

        if output_file:
            with open(output_file, "w") as f:
                json.dump(dataset, f, indent=2)
            print(f"Saved {len(dataset)} cases to {output_file}")

        return dataset

    def grade(self, prompt_inputs, output, extra_criteria=None):
        criteria = f"\nAdditional criteria:\n{extra_criteria}\n" if extra_criteria else ""

        prompt = f"""
You are an expert evaluator. Grade this AI-generated output.

Inputs given to the prompt:
{json.dumps(prompt_inputs, indent=2)}

Output produced:
{output}
{criteria}
Respond with a JSON object containing:
- "strengths": array of 1-3 key strengths
- "weaknesses": array of 1-3 key areas for improvement
- "reasoning": concise explanation of your assessment
- "score": number from 1 to 10

Be strict. Reserve 9-10 for output that fully meets every criterion.
"""
        return _json_chat(prompt)

    def run_evaluation(
        self,
        run_prompt_function,
        dataset_file=None,
        dataset=None,
        extra_criteria=None,
        json_output_file="results.json",
        html_output_file="report.html",
    ):
        if dataset is None:
            with open(dataset_file) as f:
                dataset = json.load(f)

        def run_one(case):
            try:
                output = run_prompt_function(case)
                grade = self.grade(case, output, extra_criteria)
                return {
                    "inputs": case,
                    "output": output,
                    "score": grade["score"],
                    "strengths": grade.get("strengths", []),
                    "weaknesses": grade.get("weaknesses", []),
                    "reasoning": grade.get("reasoning", ""),
                }
            except Exception as e:
                return {
                    "inputs": case,
                    "output": "",
                    "score": 0,
                    "strengths": [],
                    "weaknesses": [f"Evaluation failed: {e}"],
                    "reasoning": str(e),
                }

        with ThreadPoolExecutor(max_workers=self.max_concurrent_tasks) as pool:
            results = list(pool.map(run_one, dataset))

        scores = [r["score"] for r in results]
        average = sum(scores) / len(scores) if scores else 0

        for r in results:
            first_key = next(iter(r["inputs"]), None)
            label = str(r["inputs"].get(first_key, ""))[:50] if first_key else ""
            print(f"{r['score']:>4}/10  {label}")
        print(f"\nAverage: {average:.2f} over {len(results)} cases")

        if json_output_file:
            with open(json_output_file, "w") as f:
                json.dump({"average": average, "results": results}, f, indent=2)

        if html_output_file:
            self._write_html(results, average, html_output_file)
            print(f"Report: {html_output_file}")

        return {"average": average, "results": results}

    @staticmethod
    def _write_html(results, average, path):
        def esc(x):
            return html.escape(str(x))

        cards = []
        for i, r in enumerate(results, 1):
            strengths = "".join(f"<li>{esc(s)}</li>" for s in r["strengths"])
            weaknesses = "".join(f"<li>{esc(w)}</li>" for w in r["weaknesses"])
            cards.append(f"""
            <section>
              <h2>Case {i} &mdash; {r['score']}/10</h2>
              <h3>Inputs</h3>
              <pre>{esc(json.dumps(r['inputs'], indent=2))}</pre>
              <h3>Output</h3>
              <pre>{esc(r['output'])}</pre>
              <h3>Strengths</h3><ul>{strengths}</ul>
              <h3>Weaknesses</h3><ul>{weaknesses}</ul>
              <h3>Reasoning</h3><p>{esc(r['reasoning'])}</p>
            </section>""")

        doc = f"""<!doctype html>
<html><head><meta charset="utf-8"><title>Evaluation report</title>
<style>
  body {{ font-family: system-ui, sans-serif; max-width: 55rem; margin: 2rem auto;
         padding: 0 1rem; line-height: 1.5; }}
  section {{ border: 1px solid #ddd; border-radius: 8px; padding: 1rem 1.25rem;
             margin-bottom: 1.5rem; }}
  pre {{ background: #f6f6f6; padding: .75rem; border-radius: 6px;
         overflow-x: auto; white-space: pre-wrap; }}
  h1 {{ margin-bottom: .25rem; }}
</style></head>
<body>
<h1>Evaluation report</h1>
<p><strong>Average score: {average:.2f}/10</strong> across {len(results)} cases</p>
{''.join(cards)}
</body></html>"""

        with open(path, "w", encoding="utf-8") as f:
            f.write(doc)

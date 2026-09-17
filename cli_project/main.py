"""
main.py

The CLI. Reads your input, sends it to Claude, prints the reply.

It already knows how to run tools - but the server exposes none yet, so
every reply you see right now comes straight from the model.
"""

import asyncio
import os
import sys

from anthropic import Anthropic
from dotenv import load_dotenv

from mcp_client import MCPClient

load_dotenv()

anthropic_client = Anthropic()
MODEL = os.environ.get("CLAUDE_MODEL", "claude-haiku-4-5-20251001")
MAX_TURNS = 10


def text_from(message) -> str:
    return "\n".join(b.text for b in message.content if b.type == "text")


async def run_turn(mcp: MCPClient, messages: list) -> str:
    """One user turn: call Claude, run any tools it asks for, repeat."""
    tools = await mcp.list_tools()

    for _ in range(MAX_TURNS):
        params = {"model": MODEL, "max_tokens": 2000, "messages": messages}
        if tools:
            params["tools"] = tools

        response = anthropic_client.messages.create(**params)
        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason != "tool_use":
            return text_from(response)

        results = []
        for block in response.content:
            if block.type != "tool_use":
                continue
            print(f"  [tool] {block.name}({block.input})")
            try:
                output = await mcp.call_tool(block.name, block.input)
                is_error = False
            except Exception as e:
                output, is_error = f"Error: {e}", True

            results.append({
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": output,
                "is_error": is_error,
            })

        messages.append({"role": "user", "content": results})

    return "(stopped: too many tool turns)"


async def main():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("No ANTHROPIC_API_KEY found. Put it in .env and try again.")
        return

    async with MCPClient(command=sys.executable, args=["mcp_server.py"]) as mcp:
        tools = await mcp.list_tools()
        print(f"Connected. Server tools: {[t['name'] for t in tools] or 'none yet'}")
        print("Type 'exit' to quit.\n")

        messages = []
        while True:
            try:
                user_input = input("You: ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                break

            if user_input.lower() in {"exit", "quit"}:
                break
            if not user_input:
                continue

            messages.append({"role": "user", "content": user_input})
            reply = await run_turn(mcp, messages)
            print(f"\nClaude: {reply}\n")


if __name__ == "__main__":
    asyncio.run(main())

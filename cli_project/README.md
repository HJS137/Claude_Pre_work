# CLI MCP chatbot

A command-line chatbot with an MCP client and an MCP server.

- **`mcp_server.py`** — the server. Owns the documents and will expose tools to read and edit them.
- **`mcp_client.py`** — the client. Starts the server, talks to it over stdio, lists its tools.
- **`main.py`** — the CLI. Takes your input, calls Claude, runs any tools Claude asks for.

The server currently exposes **no tools**. You add them in the next lesson.

## Setup

1. Copy `.env.example` to `.env` and paste your key in:

   ```
   ANTHROPIC_API_KEY=sk-ant-api03-...
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Or with UV:

   ```bash
   uv venv
   uv pip install -r requirements.txt
   ```

3. Run it:

   ```bash
   python main.py
   ```

   Or `uv run main.py`.

## Verify the baseline

Two questions, in this order.

**First, ask something you can check on sight:**

```
You: what's 1+1?
```

Don't settle for a reply appearing — confirm it actually says 2. A correct
answer proves your key, your dependencies and the chat loop all work.

**Then ask about the documents:**

```
You: what do the documents say?
```

Whatever comes back did **not** come from the document tools, because they
don't exist yet. That's the model answering on its own. Once you build the
tools, you'll see `[tool] read_doc_contents(...)` printed before the reply —
that's how you tell the two apart.

## The habit

Every time you add a layer to an API project — a tool, a data source, an MCP
server — ask the running system one question whose answer you already know
before building the next layer. A baseline you've verified is the only
baseline you can debug against.

## Troubleshooting

**`No ANTHROPIC_API_KEY found`** — `.env` is missing, misnamed (check for
`.env.txt` on Windows), or you're running from a different directory.

**`ModuleNotFoundError: No module named 'mcp'`** — dependencies aren't
installed, or you're on a different Python than the one you installed into.

**Server won't start** — run `python mcp_server.py` on its own. It should
sit there waiting. Ctrl+C to exit.

**Client check** — run `python mcp_client.py`. It should connect and report
no tools yet.

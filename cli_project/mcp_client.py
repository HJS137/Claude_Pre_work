"""
mcp_client.py

The MCP CLIENT. Its job: start the server as a subprocess, talk to it over
stdio, and expose whatever tools the server offers.

Right now the server offers no tools, so list_tools() comes back empty.
That is expected until you build them.
"""

import sys
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


class MCPClient:
    def __init__(self, command: str, args: list[str]):
        self._command = command
        self._args = args
        self._session: ClientSession | None = None
        self._stack = AsyncExitStack()

    async def connect(self):
        params = StdioServerParameters(command=self._command, args=self._args)
        read, write = await self._stack.enter_async_context(stdio_client(params))
        self._session = await self._stack.enter_async_context(
            ClientSession(read, write)
        )
        await self._session.initialize()

    async def list_tools(self):
        """Tool definitions the server exposes, in Anthropic schema format."""
        result = await self._session.list_tools()
        return [
            {
                "name": t.name,
                "description": t.description or "",
                "input_schema": t.inputSchema,
            }
            for t in result.tools
        ]

    async def call_tool(self, name: str, args: dict) -> str:
        """Run one tool on the server and return its output as text."""
        result = await self._session.call_tool(name, args)
        return "\n".join(
            block.text for block in result.content if block.type == "text"
        )

    async def cleanup(self):
        await self._stack.aclose()
        self._session = None

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, *args):
        await self.cleanup()


async def main():
    """Smoke test: connect and print what the server offers."""
    async with MCPClient(command=sys.executable, args=["mcp_server.py"]) as client:
        tools = await client.list_tools()
        if tools:
            for t in tools:
                print(f"  {t['name']}: {t['description']}")
        else:
            print("  (no tools yet - you build them in the next lesson)")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())

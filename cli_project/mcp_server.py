"""
mcp_server.py

The MCP SERVER. Its job: manage documents and expose operations on them
as tools that any MCP client can call.

Right now it exposes NO tools. That is deliberate - you add them in the
next lessons. See the TODOs at the bottom.

Run it on its own to check it starts:
    python mcp_server.py
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("documents")

# All documents live in memory. No database needed.
docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specs define the technical requirements for the equipment.",
}


# ---------------------------------------------------------------------------
# TODO (next lesson): add a tool that reads a document's contents.
#
#   @mcp.tool(
#       name="read_doc_contents",
#       description="Read the contents of a document and return it as a string."
#   )
#   def read_document(doc_id: str) -> str:
#       ...
#
# TODO (next lesson): add a tool that edits a document.
#
#   @mcp.tool(
#       name="edit_document",
#       description="Edit a document by replacing a string with a new string."
#   )
#   def edit_document(doc_id: str, old_str: str, new_str: str) -> str:
#       ...
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    mcp.run(transport="stdio")

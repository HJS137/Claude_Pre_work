# Used when we need to claude to generate structured data like JSON, python code or bulleted list.
from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()

model = "claude-sonnet-4-5"


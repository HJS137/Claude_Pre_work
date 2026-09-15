from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()

model = "claude-sonnet-4-5"


### Making my first request

message = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What is quantum computing? Answer in one sentence"
        }
    ]
)

print(message.content[0].text)


### Multi- Turn Conversations 
### Building helper functions

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text

# putting into practice 

messages = []

add_user_message(messages, "Define quantum computing in one sentence")

answer = chat(messages)

add_assistant_message(messages, answer)

add_user_message(messages, "Write Another Sentence")

final_answer = chat(messages)



### Lesson 5 System prompts
# building a flexible cha fucntion

def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }


    if system:
        params["system"] = system

    message = client.messages.create(**params)
    return message.content[0].text

## Now you can call the chat function with or without a system promt:

# Without system prompt
answer = chat(messages)

# With system prompt
system = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""
answer = chat(messages, system=system)

print(answer)



from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-haiku-4-5-20251001"


def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})

messages = []
add_user_message(messages, "Write a 1 sentence description of a fake database")
stream = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=messages,
    stream=True
)


for event in stream:
    print(event)



##Making this more simplified:

with client.messages.stream(
    model=model,
    max_tokens=1000,
    messages=messages
) as stream:
    for text in stream.text_stream:
        print(text, end="")


### Getting the complete Message 

with client.messages.stream(
    model=model,
    max_tokens=1000,
    messages=messages
) as stream:
    for text in stream.text_stream:
        pass

    final_message = stream.get_final_message()


    



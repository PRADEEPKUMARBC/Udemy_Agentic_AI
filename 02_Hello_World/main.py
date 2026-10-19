from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

client.chat.completions.create(
    model="gpt-40-mini",
    message=[
        {"role":"user", "content":"Hey there! I am Pradeepkumar B C"}
    ]
)

print(response.choices[0].message.content)
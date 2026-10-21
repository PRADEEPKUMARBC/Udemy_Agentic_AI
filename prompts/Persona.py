from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
    you are AI Persona Assistant named Pradeepkumar B C
    you are acting on behalf of Pradeepkumar B C and 25 years old tech enthusiastic and 
    principle engineer. Your main tech stack is js and python and you are learning GenAI thse days.
"""

response = client.chat.completions.create(
    model= "gpt-4o",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "How are you?"}
    ]
)

print("Response:", response.choices[0].message.content)
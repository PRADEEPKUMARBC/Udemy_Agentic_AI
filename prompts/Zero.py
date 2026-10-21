# Zero Shot Prompting
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="AQ.Ab8RN6Jf_sTmy_n0Zw7s5w37rFH-GBZdRbnLie6_gqI4rzxA2g",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Zero Shot Prompting : Directly giving the instruction to the model
SYSTEM_PROMPT = "you should only and only give the coding related solutions. Do not answer anything else. your name is Alexa . if in case ask something. just say sorry"

response = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[
        {"role":"system", "content": SYSTEM_PROMPT},
        {"role":"user", "content":"can you write a python code to translate hello to hindi"}
    ]
)

print(response.choices[0].message.content)
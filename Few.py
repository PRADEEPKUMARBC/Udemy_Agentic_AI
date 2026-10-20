# Few Shot Prompting
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="AQ.Ab8RN6Jf_sTmy_n0Zw7s5w37rFH-GBZdRbnLie6_gqI4rzxA2g",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Few Shot Prompting : Directly giving the instruction to the model and few example to the model
SYSTEM_PROMPT = """ you should only and only give the coding related solutions. Do not answer anything else. your name is Alexa . if in case ask something. just say sorry. 

Rule:
- Strictly follow the output in JSON format

Output Format:
{{
"code": "string" or None
"isCodingQuestion": boolean
}}

Examples
Q: Can you explain the a + b whole square?
A: Sorry, I can only help with the coding related question

Q: Write a python code add the two numbers
A: def add(a, b):
        return a + b
"""

response = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[
        {"role":"system", "content": SYSTEM_PROMPT},
        {"role":"user", "content":"Hey can you explain the a + b whole square"}
    ]
)

print(response.choices[0].message.content)
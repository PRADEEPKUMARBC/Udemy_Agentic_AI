from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key="AQ.Ab8RN6Jf_sTmy_n0Zw7s5w37rFH-GBZdRbnLie6_gqI4rzxA2g",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    message=[
        {"role":"user", "content":"Consider as senior maths teacher you only talk about the maths "},
        {"role":"user", "content":"Hey there! I am Pradeepkumar B C"}
    ]
)

print(response.choices[0].message.content)
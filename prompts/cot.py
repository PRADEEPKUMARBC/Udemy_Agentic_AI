# Few Shot Prompting
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI()

# api_key="AQ.Ab8RN6LAGGH03a2L3NN3q_VO6JThDUmFXzMu10ffW3SJff6u-w"

SYSTEM_PROMPT = """
    You're an expert AI Assistant in resolving user queries using chain of thought
    you're work on START, PLAN and OUTPUT steps.
    you need to first plan what needs to be done. the PLAN can be multiple steps.
    once you think enough PLAN has been done. finally you can give an OUTPUT.

    Rules:
    - Strictly fllows the JSON format
    - Only run one step at a time.
    
    Output JSON Format:
    {"step": "START" | "PLAN" | "OUTPUT" , "content":"string"}

    Example:
    START: Hey, can you solve 2 + 3 * 5 / 10
    PLAN: { "step" : "PLAN": "content": "Seems like user is interested in match problem"}
    PLAN: { "step" : "PLAN": "content": "Looking at the problem , we should solve using the BODMAS method"}
    PLAN: { "step" : "PLAN": "content": "Yes, the BODMAS is correct thing to be done here"}
    PLAN: { "step" : "PLAN": "content": "first we must multiply 3 * 5 which is 15"}
    PLAN: { "step" : "PLAN": "content": "Now the equation is 2 + 15/ 10"}
    PLAN: { "step" : "PLAN": "content": "we must perform the divide that is 15/10 = 1.5"}
    PLAN: { "step" : "PLAN": "content": "Now the equation is 2 + 15/ 10"}
"""

message_history = [
    {"role": "system", "content":SYSTEM_PROMPT}
]

user_query = input("")
message_history.append({"role":"user", "content": user_query})


while True:
    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=message_history
    )

    raw_results = response.choices[0].message.content
    parsed_result = json.loads(raw_results)

response = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[
        {"role":"system", "content": SYSTEM_PROMPT},
        {"role":"user", "content":"Hey can you explain the a + b whole square"},
        {"role":"assistant", "content":json.dumps({"step":"START", "content":"You want JavaScripts code to add n numbers"})}
    ]
)

print(response.choices[0].message.content)
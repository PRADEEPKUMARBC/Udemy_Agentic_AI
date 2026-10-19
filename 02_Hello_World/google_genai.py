from google import genai


client = genai.Client(api_key="AQ.Ab8RN6Jf_sTmy_n0Zw7s5w37rFH-GBZdRbnLie6_gqI4rzxA2g")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explains how AI works in few words"
)

print(response.text)
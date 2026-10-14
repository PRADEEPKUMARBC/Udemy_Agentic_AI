import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My Name is Pradeepkumar B C"
tokens = enc.encode(text)

print("Tokens", tokens)

decoded = enc.decode([25216, 3274, 0, 3673, 7317, 382, 2284, 973, 1027, 74, 30463, 418, 363])
print("Decode", decoded)
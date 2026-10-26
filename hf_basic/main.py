from transformers import pipeline

pipe = pipeline("image-text-to-text", model="googl/gemma-3-4b-it")

messages = [
    {
        "role":"user",
        "content": [
            {"type": "image", "url":""},
            {"type": "text", "text": "What animal is on the candy?"}
        ]
    },
]

pipe(text=messages)
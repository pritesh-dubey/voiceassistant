import os
import openai

os.environ["apikey"] = "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"
openai.api_key = os.getenv("apikey")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "write a story in 50 words"
    },
    {
      "role": "user",
      "content": ""
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
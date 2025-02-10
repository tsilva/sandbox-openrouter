from dotenv import load_dotenv
load_dotenv()

import os
from openai import OpenAI

client = OpenAI(
  base_url=os.getenv("OPENROUTER_BASE_URL"),
  api_key=os.getenv("OPENROUTER_API_KEY")
)

completion = client.chat.completions.create(
  model="openrouter/auto",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is in this image?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
          }
        }
      ]
    }
  ]
)
print(completion.model)
print(completion.choices[0].message.content)
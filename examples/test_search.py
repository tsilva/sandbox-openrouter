from dotenv import load_dotenv
load_dotenv()

import os
import json
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# TODO: this doesnt seem to be working
# https://openrouter.ai/docs/features/web-search
response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
  },
  data=json.dumps({
    #"model": "openai/gpt-4o:online",
    "model": "openrouter/auto",
    "plugins": [
        {
            "id": "web",
            "max_results": 5, # Defaults to 5
            "search_prompt": "Some relevant web results:" # See default below
        }
    ],
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What happened today? Search the web."
          }
        ]
      }
    ]
  })
).json()

print(f"{response['model']} ({response['provider']})")
print(response)
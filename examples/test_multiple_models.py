from dotenv import load_dotenv
load_dotenv()

import os
import json
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
  },
  data=json.dumps({
    "models": ["gryphe/mythomax-l2-13b", "anthropic/claude-3.5-sonnet"],
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Who are you?"
          }
        ]
      }
    ],
    
  })
)
print(response.json())
from dotenv import load_dotenv
load_dotenv()

import os
import json
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

for x in range(5):
  response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
      "Authorization": f"Bearer {OPENROUTER_API_KEY}",
      "Content-Type": "application/json"
    },
    data=json.dumps({
      "model": "anthropic/claude-3.5-sonnet",
      'provider': {
        'sort': 'throughput',
        'data_collection': 'deny'
      },
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
      ]
    })
  ).json()

  print(f"{response['model']} ({response['provider']})")

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
    "model": "openrouter/auto",
    "response_format": {
        "type": "json_schema",
        "json_schema": {
          "name": "weather",
          "strict": True,
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "City or location name"
              },
              "temperature": {
                "type": "number",
                "description": "Temperature in Celsius"
              },
              "conditions": {
                "type": "string",
                "description": "Weather conditions description"
              }
            },
            "required": ["location", "temperature", "conditions"],
            "additionalProperties": False
          }
        }
    },
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Structure this: weather in porto is 30c and sunny"
          }
        ]
      }
    ]
  })
).json()

print(f"{response['model']} ({response['provider']})")
print(response["choices"][0]["message"]["content"])
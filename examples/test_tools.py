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
    "model": "openrouter/auto",
    "tools": [{
      "type": "function",
      "function": {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. San Francisco, CA"
            },
            "unit": {
              "type": "string",
              "enum": [
                "celsius",
                "fahrenheit"
              ]
            }
          },
          "required": [
            "location"
          ]
        }
      }
    }],
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What is the weather like in Boston?"
          }
        ]
      }
    ]
  })
).json()

print(f"{response['model']} ({response['provider']})")
print(response)
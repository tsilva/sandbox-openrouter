from dotenv import load_dotenv
load_dotenv()

import os
import json
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}
payload = {
    "model": "deepseek/deepseek-r1",
    "messages": [
        {"role": "user", "content": "How would you build the world's tallest skyscraper?"}
    ],
    "include_reasoning": True
}

response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response.json()['choices'][0]['message']['reasoning'])

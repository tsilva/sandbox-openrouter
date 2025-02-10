from dotenv import load_dotenv
load_dotenv()

import os
import json
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

question = "How would you build the tallest building ever?"

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
  "Authorization": f"Bearer {OPENROUTER_API_KEY}",
  "Content-Type": "application/json"
}

payload = {
  "model": "openrouter/auto",
  "messages": [{"role": "user", "content": question}],
  "stream": True
}

buffer = ""
with requests.post(url, headers=headers, json=payload, stream=True) as r:
  for chunk in r.iter_content(chunk_size=1024, decode_unicode=True):
    buffer += chunk
    while True:
      try:        
        # Find the next complete SSE line
        line_end = buffer.find('\n')
        if line_end == -1:
          break
        
        line = buffer[:line_end].strip()
        buffer = buffer[line_end + 1:]

        if line.startswith('data: '):
          data = line[6:]
          if data == '[DONE]':
            break

          try:
            data_obj = json.loads(data)
            content = data_obj["choices"][0]["delta"].get("content")
            if content:
              print(content, end="", flush=True)
          except json.JSONDecodeError:
            pass
      except Exception:
        break

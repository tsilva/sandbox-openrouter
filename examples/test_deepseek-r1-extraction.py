from dotenv import load_dotenv
load_dotenv()

import os
import json
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

question = "Which is bigger: 9.11 or 9.9?"

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

def do_req(model, content, include_reasoning=False):
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": content}
        ],
        "include_reasoning": include_reasoning,
        "stop": "</think>"
    }
    return requests.post(url, headers=headers, data=json.dumps(payload))

# R1 will reliably return "done" for the content portion of the response
content = f"{question} Please think this through, but don't output an answer"
reasoning_response = do_req("deepseek/deepseek-r1", content, True)
reasoning = reasoning_response.json()['choices'][0]['message']['reasoning']

# Let's test! Here's the naive response:
simple_response = do_req("openai/gpt-4o-mini", question)
print(simple_response.json()['choices'][0]['message']['content'])

# Here's the response with the reasoning token injected:
content = f"{question}. Here is some context to help you: {reasoning}"
smart_response = do_req("openai/gpt-4o-mini", content)
print(smart_response.json()['choices'][0]['message']['content'])

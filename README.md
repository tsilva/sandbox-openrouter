<div align="center">
  <img src="logo.png" alt="sandbox-openrouter" width="512"/>

  [![Python](https://img.shields.io/badge/Python-3.7+-3776ab?logo=python&logoColor=white)](https://python.org)
  [![OpenRouter](https://img.shields.io/badge/OpenRouter-API-6366f1)](https://openrouter.ai/)
  [![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

  **🌐 Sample project for learning OpenRouter LLM aggregation 🔀**

  [OpenRouter Docs](https://openrouter.ai/docs) · [API Reference](https://openrouter.ai/api/v1)
</div>

## Overview

This project demonstrates how to use [OpenRouter](https://openrouter.ai/), an LLM aggregator that provides a unified API to access different models (GPT-4, Claude, Llama, etc.) from various providers. Switch between models for optimal pricing, reliability, and throughput without changing your code.

## Features

- **Direct HTTP requests** - Full control over API interactions with streaming support
- **OpenAI SDK compatible** - Drop-in replacement using `base_url` override
- **LangChain integration** - Works seamlessly with LangChain's ecosystem
- **Auto model selection** - Use `openrouter/auto` for automatic best-model routing
- **Structured output** - JSON schema support for typed responses
- **Reasoning traces** - Access model thinking with `include_reasoning`

## Quick Start

```bash
# Clone and setup
git clone https://github.com/tsilva/sandbox-openrouter.git
cd sandbox-openrouter
uv venv && uv pip install -r requirements.txt

# Configure API key
cp .env.example .env
# Edit .env and add your OPENROUTER_API_KEY

# Run an example
python examples/test_requests.py
```

## Installation

### Prerequisites

- Python 3.7+
- [uv](https://github.com/astral-sh/uv) package installer
- OpenRouter API key ([get one here](https://openrouter.ai/keys))

### Setup

1. Create a virtual environment:
   ```bash
   uv venv
   ```

2. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```

3. Configure environment variables in `.env`:
   ```
   OPENROUTER_API_KEY=<your-api-key>
   OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
   ```

## Usage

### Direct HTTP Requests

```python
import requests
import os

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={"Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}"},
    json={
        "model": "openrouter/auto",
        "messages": [{"role": "user", "content": "Hello!"}]
    }
)
print(response.json()["choices"][0]["message"]["content"])
```

### OpenAI SDK

```python
from openai import OpenAI
import os

client = OpenAI(
    base_url=os.getenv("OPENROUTER_BASE_URL"),
    api_key=os.getenv("OPENROUTER_API_KEY")
)

completion = client.chat.completions.create(
    model="openrouter/auto",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(completion.choices[0].message.content)
```

### LangChain

```python
from langchain_openai import ChatOpenAI
import os

llm = ChatOpenAI(
    model="openrouter/auto",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL")
)

result = llm.invoke("Hello!")
print(result.content)
```

## Examples

| Example | Description |
|---------|-------------|
| `test_requests.py` | Basic API call with image input |
| `test_streaming.py` | Server-sent events (SSE) streaming |
| `test_openai.py` | OpenAI SDK compatibility |
| `test_langchain.py` | LangChain integration |
| `test_structured_output.py` | JSON schema responses |
| `test_deepseek-r1.py` | Reasoning model with traces |
| `test_multiple_models.py` | Query multiple models |
| `test_tools.py` | Function calling |
| `test_search.py` | Web search capability |
| `test_sort_provider.py` | Provider sorting |
| `test_disable_data_collection.py` | Privacy settings |

Run any example:
```bash
python examples/<example_name>.py
```

## Dependencies

| Package | Purpose |
|---------|---------|
| `requests` | Direct HTTP API calls |
| `openai` | OpenAI SDK (compatible with OpenRouter) |
| `langchain` + `langchain-openai` | LangChain integration |
| `python-dotenv` | Environment variable management |

## License

MIT

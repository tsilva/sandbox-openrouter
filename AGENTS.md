# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a sample project demonstrating how to use OpenRouter - an LLM aggregator that provides a unified API to access different models (GPT-4, Claude, etc.) from various providers. The project uses Python and includes multiple example scripts showing different OpenRouter features.

## Environment Setup

Required environment variables in `.env` (see `.env.example`):
- `OPENROUTER_API_KEY`: Your OpenRouter API key
- `OPENROUTER_BASE_URL`: https://openrouter.ai/api/v1

Virtual environment setup:
```bash
uv venv
uv pip install -r requirements.txt
```

## Running Examples

All example scripts are in the `examples/` directory and follow the pattern:
```bash
python examples/<example_name>.py
```

Each example demonstrates a specific OpenRouter feature and is self-contained with proper environment loading via `python-dotenv`.

## Key Dependencies

- `requests`: Direct HTTP API calls to OpenRouter
- `openai`: OpenAI SDK compatible with OpenRouter (via base_url override)
- `langchain` + `langchain-openai`: LangChain integration
- `python-dotenv`: Environment variable management

## Architecture Patterns

### API Integration Approaches

The codebase demonstrates three ways to interact with OpenRouter:

1. **Direct HTTP requests** (`test_requests.py`, `test_streaming.py`, etc.): Uses `requests` library for raw HTTP calls. This approach gives full control over the API interaction including streaming responses and custom parameters.

2. **OpenAI SDK** (`test_openai.py`): Uses the OpenAI Python SDK with `base_url` override pointing to OpenRouter. This provides a familiar interface for those accustomed to OpenAI's API.

3. **LangChain integration** (`test_langchain.py`): Uses `ChatOpenAI` from `langchain-openai` with OpenRouter endpoints. This integrates with LangChain's broader ecosystem.

### Model Selection

Most examples use `"openrouter/auto"` which automatically selects the best available model. Specific models can be targeted by changing the model parameter (e.g., `"deepseek/deepseek-r1"`).

### Response Patterns

- Standard responses: Parse `response["choices"][0]["message"]["content"]`
- Streaming: Handle SSE (Server-Sent Events) format with `data: ` prefix
- Structured output: Use `response_format` with JSON schema for typed responses
- Reasoning models: Set `include_reasoning: True` to access reasoning traces

## Important Implementation Notes

- README.md must be kept up to date with any significant project changes
- All examples load environment variables using `load_dotenv()` at the start
- The `.env` file is gitignored to prevent API key exposure
- Response metadata includes `model` and `provider` fields showing which model was actually used

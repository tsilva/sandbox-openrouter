from dotenv import load_dotenv
load_dotenv()

import os
from langchain_openai import ChatOpenAI

MODEL_NAME = "openrouter/auto"
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

llm = ChatOpenAI(
    model=MODEL_NAME,
    api_key=OPENROUTER_API_KEY,
    base_url=OPENROUTER_BASE_URL
)

result = llm.invoke("The meaning of life is ")
model_name = result.response_metadata["model_name"]
print(model_name)
print(result)
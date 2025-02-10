# sandbox-openrouter

This is a sample project that uses OpenRouter.

[OpenRouter](https://openrouter.ai/) is an aggregator that lets you use different LLMs (like gpt-4o, Claude-3.5-sonnet, etc.) through a single API. This allows you to easily switch between models and providers for best pricing, reliability and throughput.

## Prerequisites

*   Python 3.7+
*   `uv` package installer

## Setup

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  Create a virtual environment:

    ```bash
    uv venv
    ```

3.  Install dependencies:

    ```bash
    uv pip install -r requirements.txt
    ```

4.  Set up environment variables:

    *   Create a `.env` file in the project root.
    *   Add the following variables, replacing the placeholders with your actual values:

        ```
        OPENROUTER_API_KEY=<your_openrouter_api_key>
        OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
        ```

    *   Make sure to replace `<model_name>` in `main.py` with the desired model.

5.  Run the script:

    ```bash
    python main.py
    ```

    (No activation step is needed after creating the virtual environment with `uv venv`.)

## Notes

*   The `.env` file is ignored by Git (see `.gitignore`) to prevent accidental exposure of your API key.
*   Remember to replace the placeholder values in the `.env` file and `<model_name>` in `main.py`.
# sandbox-openrouter

This is a sample project that uses OpenRouter.

## Setup

1.  Clone the repository:

    ```bash
    git clone https://github.com/tsilva/sandbox-openrouter.git
    cd <repository_directory>
    ```

2.  Create a virtual environment:

    ```bash
    uv venv
    ```

3.  Install dependencies:

    ```bash
    uv pip install -r requirements.txt
    ```

4.  Set up environment variables:

    *   Create a `.env` file in the project root.
    *   Add the following variables, replacing the placeholders with your actual values:

        ```
        OPENROUTER_API_KEY=<your_openrouter_api_key>
        OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
        ```

    *   Make sure to replace `<model_name>` in `main.py` with the desired model.

5.  Run the script:

    ```bash
    python examples/<example_name>.py
    ```

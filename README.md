# LLMdoc - LLM Function Calling Framework

A flexible framework for implementing function calling capabilities across multiple LLM providers (OpenAI, Gemini, Anthropic). This project provides a structured way to define, manage, and use functions that can be called by various LLM APIs.

## Features

- Multi-provider support (OpenAI, Gemini, Anthropic)
- Structured function definitions using Pydantic models
- Environment variable management for API keys
- Asynchronous function calling implementation
- Type-safe function handling
- Tool-based interaction system
- Example implementations for common use cases

## Setup

1. Clone the repository:
```bash
git clone git@github.com:ResearchAgent/ToolAgentTemplate.git
cd llmdoc
```

2. Install dependencies:
```bash
poetry install
```

3. Create a `.env` file in the root directory with your API keys:
```
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

## Project Structure

```
src/
├── llmdoc/
│   ├── __init__.py
│   ├── config.py          # Configuration and environment setup
│   ├── clients/           # LLM provider clients
│   │   ├── __init__.py
│   │   └── factory.py     # Client factory for different providers
│   ├── functions/         # Function definitions
│   │   ├── __init__.py
│   │   └── example.py     # Example function implementations
│   ├── tools/            # Tool definitions and handlers
│   │   ├── __init__.py
│   │   └── available_tools.py
│   └── examples/         # Example implementations
│       └── function_calling_example.py
tests/                    # Test files
```

## Usage

### Basic Usage

```python
from llmdoc.client import OpenAIClient
from llmdoc.functions.example import get_weather_function

# Initialize the client
client = OpenAIClient()

# Define available functions
functions = [get_weather_function]

# Make a function call
response = client.chat_completion(
    messages=[{"role": "user", "content": "What's the weather in New York?"}],
    functions=functions
)
```

### Running the Example

You can run the example in two ways:

1. As a module (recommended):
```bash
python -m src.llmdoc.examples.function_calling_example
```

2. Using absolute imports:
```bash
python src/llmdoc/examples/function_calling_example.py
```

### Using Different Providers

The framework supports multiple LLM providers. To use a different provider:

```python
# In function_calling_example.py
asyncio.run(main("openai"))    # Use OpenAI
# asyncio.run(main("gemini"))  # Use Gemini
# asyncio.run(main("anthropic"))  # Use Anthropic
```

## Development

### Adding New Functions

1. Create a new function definition in `src/llmdoc/functions/`
2. Define the function schema using Pydantic models
3. Implement the function logic
4. Add the function to the available functions list

### Adding New Providers

1. Create a new client class in `src/llmdoc/clients/`
2. Implement the required interface
3. Add the provider to the client factory

## Testing

Run the test suite:
```bash
poetry run pytest
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT

## Acknowledgments

- OpenAI for the function calling API
- Google for Gemini
- Anthropic for Claude
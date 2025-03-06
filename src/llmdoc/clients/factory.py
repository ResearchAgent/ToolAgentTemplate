from typing import Literal
from .base import BaseLLMClient
from .openai_client import OpenAIClient
from .gemini_client import GeminiClient
from .anthropic_client import AnthropicClient

def create_client(provider: Literal["openai", "gemini", "anthropic"]) -> BaseLLMClient:
    """Create an LLM client for the specified provider."""
    clients = {
        "openai": OpenAIClient,
        "gemini": GeminiClient,
        "anthropic": AnthropicClient
    }
    return clients[provider]()
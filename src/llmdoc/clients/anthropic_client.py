from typing import Dict, Any, List, Optional
from anthropic import Anthropic
from .base import BaseLLMClient
from ..config import Config

class AnthropicClient(BaseLLMClient):
    def __init__(self):
        Config.validate()
        self.client = Anthropic(api_key=Config.ANTHROPIC_API_KEY)
    
    async def chat_completion(
        self,
        messages: List[Dict[str, str]],
        functions: Optional[List[Dict[str, Any]]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        response = await self.client.messages.create(
            model=kwargs.get("model", "claude-3-sonnet-20240229"),
            messages=messages,
            tools=functions if functions else None,
            **kwargs
        )
        return {"choices": [{"message": {"content": response.content[0].text}}]}
    
    def format_function_call(self, function_call: Dict[str, Any]) -> Dict[str, Any]:
        # Convert OpenAI format to Anthropic format
        return {
            "name": function_call["name"],
            "parameters": function_call["arguments"]
        }
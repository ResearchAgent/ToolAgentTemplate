from typing import Dict, Any, List, Optional
from openai import OpenAI
from .base import BaseLLMClient
from ..config import Config

class OpenAIClient(BaseLLMClient):
    def __init__(self):
        Config.validate()
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
    
    async def chat_completion(
        self,
        messages: List[Dict[str, str]],
        functions: Optional[List[Dict[str, Any]]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        params = {
            "model": kwargs.get("model", "gpt-3.5-turbo"),
            "messages": messages,
            **kwargs
        }
        if functions:
            params["functions"] = functions
        return self.client.chat.completions.create(**params)
    
    def format_function_call(self, function_call: Dict[str, Any]) -> Dict[str, Any]:
        return function_call  # OpenAI format is already correct
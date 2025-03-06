from typing import Dict, Any, List, Optional
import google.generativeai as genai
from .base import BaseLLMClient
from ..config import Config

class GeminiClient(BaseLLMClient):
    def __init__(self):
        Config.validate()
        genai.configure(api_key=Config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')
    
    async def chat_completion(
        self,
        messages: List[Dict[str, str]],
        functions: Optional[List[Dict[str, Any]]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        chat = self.model.start_chat()
        for message in messages:
            chat.send_message(message["content"])
        response = chat.last
        return {"choices": [{"message": {"content": response.text}}]}
    
    def format_function_call(self, function_call: Dict[str, Any]) -> Dict[str, Any]:
        # Convert OpenAI format to Gemini format
        return {
            "name": function_call["name"],
            "args": function_call["arguments"]
        }
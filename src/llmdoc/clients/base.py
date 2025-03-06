from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional

class BaseLLMClient(ABC):
    """Base class for LLM clients."""
    
    @abstractmethod
    async def chat_completion(
        self,
        messages: List[Dict[str, str]],
        functions: Optional[List[Dict[str, Any]]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Send a chat completion request to the LLM."""
        pass
    
    @abstractmethod
    def format_function_call(self, function_call: Dict[str, Any]) -> Dict[str, Any]:
        """Format function call for the specific provider."""
        pass
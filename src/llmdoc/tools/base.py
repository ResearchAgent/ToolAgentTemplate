from abc import ABC, abstractmethod
from typing import Dict, Any, Type
from pydantic import BaseModel

class BaseTool(ABC):
    """Base class for all tools."""
    
    name: str
    description: str
    parameters_schema: Type[BaseModel]
    
    @abstractmethod
    async def run(self, **kwargs) -> Dict[str, Any]:
        """Execute the tool with the given parameters."""
        pass
    
    @property
    def function_definition(self) -> Dict[str, Any]:
        """Get the OpenAI function definition for this tool."""
        schema = self.parameters_schema.model_json_schema()
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": schema["properties"],
                "required": schema.get("required", [])
            }
        }
from typing import Dict, Any
from pydantic import BaseModel, Field
from .base import BaseTool

class WeatherParams(BaseModel):
    """Parameters for the weather function."""
    location: str = Field(..., description="The city and state, e.g. San Francisco, CA")
    unit: str = Field(default="celsius", description="The unit of temperature to use")

class WeatherTool(BaseTool):
    """Tool for getting weather information."""
    
    name = "get_weather"
    description = "Get the current weather in a given location"
    parameters_schema = WeatherParams
    
    async def run(self, location: str, unit: str = "celsius") -> Dict[str, Any]:
        """Get weather information for a location."""
        # Mock implementation
        return {
            "location": location,
            "temperature": 22,
            "unit": unit,
            "description": "Partly cloudy"
        }
from typing import Dict, Any
from pydantic import BaseModel, Field

class WeatherParams(BaseModel):
    """Parameters for the get_weather function."""
    location: str = Field(..., description="The city and state, e.g. San Francisco, CA")
    unit: str = Field(default="celsius", description="The unit of temperature to use")

def get_weather(location: str, unit: str = "celsius") -> Dict[str, Any]:
    """
    Get the current weather in a given location.
    
    Args:
        location: The city and state, e.g. San Francisco, CA
        unit: The unit of temperature to use (celsius/fahrenheit)
        
    Returns:
        Dictionary containing weather information
    """
    # This is a mock implementation
    return {
        "location": location,
        "temperature": 22,
        "unit": unit,
        "description": "Partly cloudy"
    }

# Function definition for OpenAI
get_weather_function: Dict[str, Any] = {
    "name": "get_weather",
    "description": "Get the current weather in a given location",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA"
            },
            "unit": {
                "type": "string",
                "description": "The unit of temperature to use (celsius/fahrenheit)",
                "enum": ["celsius", "fahrenheit"],
                "default": "celsius"
            }
        },
        "required": ["location"]
    }
} 
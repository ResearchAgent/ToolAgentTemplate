from dotenv import load_dotenv
import os
from typing import Optional

load_dotenv()

class Config:
    """Configuration class for LLM clients."""
    
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    GEMINI_API_KEY: Optional[str] = os.getenv("GEMINI_API_KEY")
    ANTHROPIC_API_KEY: Optional[str] = os.getenv("ANTHROPIC_API_KEY")
    
    @classmethod
    def validate(cls, provider: str = "openai") -> None:
        """Validate the configuration for the specified provider."""
        if provider == "openai" and not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        elif provider == "gemini" and not cls.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY environment variable is not set")
        elif provider == "anthropic" and not cls.ANTHROPIC_API_KEY:
            raise ValueError("ANTHROPIC_API_KEY environment variable is not set")
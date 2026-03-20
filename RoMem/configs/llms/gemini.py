from base import LlmConfig
from pydantic import Field


class GeminiConfig(LlmConfig):
    """
    Config for Google Gemini LLMs.
    """
    model_name: str = "gemini-1.5-flash"  
    api_key: str = Field(..., repr=False)  # required, no default
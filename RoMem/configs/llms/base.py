from pydantic import BaseModel, Field

class LlmConfig(BaseModel):
    """
    Common config across all LLMs.
    """
    model_name: str | None = None
    api_key: str | None = Field(None, repr=False) 
    top_p: float = Field(0.1, ge=0.0, le=1.0, description="Nucleus sampling threshold")
    top_k: int = Field(1, ge=1, description="Top-k sampling")
    temperature: float = Field(0.5, ge=0.0, le=2.0, description="Sampling temperature")
    max_tokens: int = Field(500, gt=0, description="Maximum tokens to generate")
from abc import ABC

class LlmConfig(ABC):
    """
    This class Provides Common Config across all LLM's
    """
    def __init__(
        self,
        model_name: str | None = None,
        api_key: str | None = None,
        top_p: float = 0.1,
        top_k: int = 1,
        temperature: float = 0.5,
        max_tokens: int = 500,
    ):
        """
        Initialize a Base config class instance for llms
        """
        self.model_name = model_name
        self.api_key = api_key
        self.top_p = top_p
        self.top_k = top_k
        self.temperature = temperature
        self.max_tokens =  max_tokens
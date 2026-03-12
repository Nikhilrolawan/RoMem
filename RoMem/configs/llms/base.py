from abc import ABC

class LlmConfig(ABC):
    """
    This class Provides Common Config across all LLM's
    """
    def __init__(
            self,
            model_name: str,
            api_key: str,
            top_p: float,
            top_k: float,
            temperature: float,
            max_tokens: int
    ):
        pass
from base import LlmConfig

class GeminiConfig(LlmConfig):


    def __init__(
        self,
        model_name: str,
        api_key: str | None,
        top_p: float = 0.1,
        top_k: int = 1,
        temperature: float = 0.5,
        max_tokens: int = 500,
    ):
        super().__init__(
            model_name = model_name,
            api_key = api_key,
            top_p = top_p,
            top_k = top_k,
            temperature = temperature,
            max_tokens = max_tokens,
        )
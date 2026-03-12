import os
from llms.base import LLMBase
from configs.llms.base import LlmConfig
from configs.llms.gemini import GeminiConfig

try:
    from google import genai
    from google.genai.types import GenerateContentConfig
except ImportError:
    raise("google-genai not found please install it using 'pip install googel-genai'.")

class GeminiLLM(LLMBase):

    def __init__(self, config: LlmConfig | GeminiConfig | dict = None):
        if config is None:
            config = GeminiConfig()
        elif isinstance(config, dict):
            config = GeminiConfig(**config)
        elif isinstance(config, LlmConfig) and not isinstance(config, GeminiConfig):
            config = GeminiConfig(
                model_name = config.model_name,
                api_key = config.api_key,
                top_p = config.top_p,
                top_k = config.top_k,
                temperature = config.temperature,
                max_tokens = config.max_tokens
            )
        super().__init__(config)

        if not self.config.model_name:
            self.config.model_name = "gemini-2.5-flash"
        api_key = self.config.api_key or os.getenv("GOOGLE_API_KEY")
        self.client = genai.Client(api_key=api_key)

    def generate_response(self, message, tools = None):
        pass
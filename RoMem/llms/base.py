from configs.llms.base import LlmConfig
from abc import ABC, abstractmethod

class LLMBase(ABC):
    """
    Base llm class for all llm providers
    """
    def __init__(self, config: LlmConfig | dict):
        if config is None:
            self.config = LlmConfig()
        elif isinstance(config, dict):
            self.config = LlmConfig(**config)
        else:
            self.config = config
    

    @abstractmethod
    def generate_response(self, message: list[dict[str, str]], tools: list[dict] = None):
        pass
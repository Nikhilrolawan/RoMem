from abc import ABC, abstractmethod
from typing import Literal
from configs.embeddings.base import BaseEmbeddingConfig

class BaseEmbedding(ABC):

    def __init__(self, config: BaseEmbeddingConfig | None = None):
        if self.config is None:
            self.config = BaseEmbeddingConfig()
        else:
            self.config = config

    @abstractmethod
    def embed(self, text, memory_action: Literal["search", "update", "add"] | None = None):
        pass


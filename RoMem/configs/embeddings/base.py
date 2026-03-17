from abc import ABC

class BaseEmbeddingConfig(ABC):
    """
    config for embedding
    """

    def __init__(
        self,
        model: str | None = None,
        api_key: str | None = None,
        embed_dim: int | None = None
    ):
        """
        initialize a instance of config class for embedding
        """
        self.model = model
        self.api_key = api_key
        self.embed_dim = embed_dim
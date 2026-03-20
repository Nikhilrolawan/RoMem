from pydantic import BaseModel, Field

class BaseEmbeddingConfig(BaseModel):
    """
    config for embedding
    """
    model: str | None = None,
    api_key: str = Field(repr=False),
    embed_dim: int | None = Field(None, gt = 0, description = "Embedding Dimension")

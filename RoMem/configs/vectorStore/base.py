from pydantic import BaseModel, Field

class VectorStoreConfig(BaseModel):
    """
    Base config for all vector stores.
    """
    
    collection_name: str = "RoMem"
    embedding_dim: int = Field(512, gt=0, description="Must match your embedding model dimensions")
    
    top_k: int = Field(5, gt=0, description="Number of results to return")
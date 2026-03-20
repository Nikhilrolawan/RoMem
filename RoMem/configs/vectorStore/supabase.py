from pydantic import Field, model_validator
from configs.vectorStore.base import VectorStoreConfig
from enum import Enum
from typing import Any


class IndexMethod(Enum):
    AUTO = "auto"
    HNSM = "hnsw"
    IVFLAT = "ivflat"

class IndexMeasure(Enum):
    COSINE = "cosine"
    L2 = "l2"
    L1 = "l1"

class SupabaseConfig(VectorStoreConfig):
    connection_string: str | None = Field(...,repr = False)
    index_method: IndexMethod = IndexMethod.AUTO
    index_measure: IndexMeasure = IndexMeasure.COSINE

    @model_validator(mode = "before")
    @classmethod
    def check_connection_string(cls, values: dict[str, Any]):
        conn = values.get("connection_string")
        if not conn or not conn.startswith("postgresql://"):
            raise ValueError("A valid PostgreSQL string must be provided")
        return values
    
from configs.vectorStore.supabase import SupabaseConfig
from vectorStore.base import VectorStoreBase
import uuid

try:
    import vecs
except ImportError:
    raise ImportError("vecs module not found, install it using: pip install vecs")

class Supabase(VectorStoreBase):

    def __init__(self, config: SupabaseConfig):
        self.config = config
        try:
            self.client = vecs.create_client(config.connection_string)
        except Exception as e:
            raise ConnectionError(f"Failed to connect to Supabase: {e}")
    
    def create_collection(self, collection_name: str | None = None, embedding_dim: int | None = None):
        name = collection_name or self.config.collection_name
        dims = embedding_dim or self.config.embedding_dim
        if not dims: raise ValueError("dimension must be provided")
        try:
            self.collection = self.client.get_or_create_collection(
                    name=name,
                    dimension=dims
                )
        except Exception as e:
            raise 
    
    def insert(self, vectors: list[list[float]], ids: list[str] | None = None, metadata: list[dict] | None = None ):
        
        ids = ids if ids else [str(uuid.uuid4()) for _ in vectors]
        metadata = metadata if metadata else [{} for _ in vectors]
        records = [(id, vector, payload) for id, vector, payload in zip(ids, vectors, metadata)]
        self.collection.upsert(records = records)
        self.collection.create_index(method = self.config.index_method.value, measure = self.config.index_measure.value)

    def search(self, query_vector: list[float], limit):
        response = self.collection.query(
            data = query_vector,
            limit = limit,
            include_vector = True,
            include_metadata = True
        )
        return [result for result in response]
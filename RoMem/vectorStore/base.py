from abc import ABC, abstractmethod

class VectorStoreBase(ABC):
    
    @abstractmethod
    def create_collection(self, collection_name: str, embedding_dim: int):
        pass

    @abstractmethod
    def search(self, query_vector: list[float], data_vector: list[list[float]], limit: int):
        pass
    
    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def insert(self, vectors, ids, metadata: dict = {}):
        pass

    @abstractmethod
    def update(self, id, vector, metadata):
        pass

    @abstractmethod
    def get(self, id):
        pass

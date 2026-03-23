from abc import abstractmethod, ABC

class MemoryBase(ABC):
    """Base memory class"""

    @abstractmethod
    def add(self, user_id: str, content: str) -> list[dict[str,any]]:
        pass

    @abstractmethod
    def serach(self, query: str, user_id: str, top_k: int = 5) -> list[dict[str,any]]:
        pass

    @abstractmethod
    def update(self, memory_id: str, content: str) -> dict[str, any]:
        pass

    @abstractmethod
    def delete(self, memory_id: str) -> None:
        pass

    @abstractmethod
    def get_all(self, user_id: str) -> list[dict[str,any]]:
        pass
from abc import ABC, abstractmethod


class IParameterStore(ABC):
    @abstractmethod
    def put(
        self,
        Name: str,
        Value: str,
        Type: str = "String",
        Overwrite: bool = True,
    ) -> dict:
        ...
        
    @abstractmethod
    def get(self, Name: str, WithDecryption: bool = True) -> dict:
        ...

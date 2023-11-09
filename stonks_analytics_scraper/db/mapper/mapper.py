from abc import ABC, abstractmethod
from collections import namedtuple


class Mapper(ABC):
    data_shape: list[dict]

    @abstractmethod
    def map(self, data: dict) -> namedtuple:
        pass

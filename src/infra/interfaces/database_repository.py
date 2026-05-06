# pylint: disable=no-self-argument
from typing import Dict
from abc import ABC, abstractmethod


class DatabaseRepositoryInterface(ABC):
    @abstractmethod
    def insert_artist(cls, data: Dict) -> int:
        pass

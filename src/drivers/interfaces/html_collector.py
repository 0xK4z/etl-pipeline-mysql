from abc import ABC, abstractmethod
from typing import List, Dict


class HtmlCollectorInterface(ABC):

    @classmethod
    @abstractmethod
    def collect_essential_information(cls, html: str) -> List[Dict[str, str]]:
        pass

from typing import Dict
from src.infra.interfaces.database_repository import DatabaseRepositoryInterface


class DataBaseRepositoryMock(DatabaseRepositoryInterface):

    insert_artist_attributes = []

    @classmethod
    def insert_artist(cls, data: Dict) -> int:  # pylint: disable=arguments-differ
        cls.insert_artist_attributes.append(data)
        return len(cls.insert_artist_attributes)

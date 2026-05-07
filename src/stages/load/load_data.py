from src.errors.load_error import LoadError
from src.infra.interfaces.database_repository import DatabaseRepositoryInterface
from src.stages.contracts.transform_contract import TransformContract


class LoadData:
    def __init__(self, repository: DatabaseRepositoryInterface):
        self.__repository = repository

    def load_artist(self, transformed_data: TransformContract):
        try:
            for artist in transformed_data.load_content:
                self.__repository.insert_artist(artist)
        except Exception as exception:
            raise LoadError(str(exception)) from exception

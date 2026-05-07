from src.infra.mocks.database_repository_mock import DataBaseRepositoryMock
from src.stages.load.load_data import LoadData
from src.stages.transform.mocks.mock_transform_raw_data import mock_transform_raw_data


def test_load():
    transformed_data = mock_transform_raw_data()
    database_repository = DataBaseRepositoryMock()
    load_data = LoadData(repository=database_repository)
    load_data.load_artist(transformed_data)
    assert len(database_repository.insert_artist_attributes) == len(
        transformed_data.load_content
    )
    assert database_repository.insert_artist_attributes == transformed_data.load_content

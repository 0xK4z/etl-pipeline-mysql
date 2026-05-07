# pylint: disable=line-too-long
from src.infra.mocks.database_repository_mock import DataBaseRepositoryMock
from src.stages.transform.mocks.mock_transform_raw_data import mock_transform_raw_data

def test_insert_artist():
    database_repository = DataBaseRepositoryMock()
    transformed_data = mock_transform_raw_data()
    artist_id = database_repository.insert_artist(transformed_data.load_content[0])
    assert isinstance(artist_id, int)
    database_repository.insert_artist_attributes.clear()

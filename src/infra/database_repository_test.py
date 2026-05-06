from src.infra.database_repository import DatabaseRepository
from src.stages.transform.mocks.mock_transform_raw_data import mock_transform_raw_data

def test_insert_artist():
    database_repository = DatabaseRepository()
    transformed_data = mock_transform_raw_data()
    artist_id = database_repository.insert_artist(transformed_data)
    assert isinstance(artist_id, int)

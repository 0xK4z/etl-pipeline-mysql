# pylint: disable=line-too-long
import pytest

from src.infra.database_repository import DatabaseRepository
from src.stages.transform.mocks.mock_transform_raw_data import mock_transform_raw_data

@pytest.mark.skip(reason="This test requires a real database connection and should be run in an integration testing environment.")
def test_insert_artist():
    database_repository = DatabaseRepository()
    transformed_data = mock_transform_raw_data()
    artist_id = database_repository.insert_artist(transformed_data.load_content[0])
    assert isinstance(artist_id, int)

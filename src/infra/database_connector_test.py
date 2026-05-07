from .database_connector import DatabaseConnector


def test_database_connector():
    assert DatabaseConnector.connection is None
    connection = DatabaseConnector.connect()
    assert connection is not None
    DatabaseConnector.disconnect()

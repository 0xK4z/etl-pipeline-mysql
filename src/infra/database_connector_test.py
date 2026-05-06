from .database_connector import DatabaseConnector


def test_database_connector():
    assert DatabaseConnector.connection is None
    connection = DatabaseConnector.connect()
    print(connection)
    assert connection is not None
    DatabaseConnector.disconnect()

from typing import Dict
from src.infra.database_connector import DatabaseConnector
from src.infra.interfaces.database_repository import DatabaseRepositoryInterface


class DatabaseRepository(DatabaseRepositoryInterface):

    @classmethod
    def insert_artist(cls, data: Dict) -> int: # pylint: disable=arguments-differ
        connection = DatabaseConnector.connect()
        cursor = connection.cursor()
        insert_query = """
            INSERT INTO artists (first_name, last_name, surname, artist_id, link, extraction_date)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
        cursor.execute(insert_query, list(data.values()))
        connection.commit()
        artist_id = cursor.lastrowid
        cursor.close()
        DatabaseConnector.disconnect()
        return artist_id

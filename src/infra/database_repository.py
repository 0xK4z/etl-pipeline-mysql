from src.infra.database_connector import DatabaseConnector
from src.stages.contracts.transform_contract import TransformContract


class DatabaseRepository:

    @classmethod
    def insert_artist(cls, data: TransformContract) -> int:
        connection = DatabaseConnector.connect()
        cursor = connection.cursor()
        insert_query = """
            INSERT INTO artists (first_name, last_name, surname, artist_id, link, extraction_date)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
        cursor.execute(insert_query, list(data.load_content[0].values()))
        connection.commit()
        artist_id = cursor.lastrowid
        cursor.close()
        DatabaseConnector.disconnect()
        return artist_id

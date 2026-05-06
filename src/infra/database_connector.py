import mysql.connector as mysql


class DatabaseConnector:
    connection = None

    @classmethod
    def connect(cls) -> mysql.MySQLConnection:
        connection = mysql.connect(
            host="localhost", user="root", password="root", database="pipeline_db"
        )
        cls.connection = connection
        return cls.connection

    @classmethod
    def disconnect(cls):
        if cls.connection:
            cls.connection.close()
            cls.connection = None

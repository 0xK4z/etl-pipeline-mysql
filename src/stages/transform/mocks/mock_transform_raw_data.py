import datetime
from src.stages.contracts.transform_contract import TransformContract


def mock_transform_raw_data():
    return TransformContract(
            load_content=[
                {
                    "first_name": "John",
                    "last_name": "Smith",
                    "surname": None,
                    "artist_id": "123",
                    "link": "https://example.com/artist?artistid=123",
                    "extraction_date": datetime.date(2026, 5, 6),
                },
                {
                    "first_name": "Jr.",
                    "last_name": "Smith",
                    "surname": "John",
                    "artist_id": "321",
                    "link": "https://example.com/artist?artistid=321",
                    "extraction_date": datetime.date(2026, 5, 6),
                },
                {
                    "first_name": "Bob III",
                    "last_name": "Brown",
                    "surname": None,
                    "artist_id": "987",
                    "link": "https://example.com/artist?artistid=987",
                    "extraction_date": datetime.date(2026, 5, 6),
                },
                {
                    "first_name": "Jane",
                    "last_name": "Doe",
                    "surname": None,
                    "artist_id": "456",
                    "link": "https://example.com/artist?artistid=456",
                    "extraction_date": datetime.date(2026, 5, 6),
                },
                {
                    "first_name": "Bob",
                    "last_name": "Brown",
                    "surname": None,
                    "artist_id": "789",
                    "link": "https://example.com/artist?artistid=789",
                    "extraction_date": datetime.date(2026, 5, 6),
                },
                {
                    "first_name": "Sr.",
                    "last_name": "Doe",
                    "surname": "Jane",
                    "artist_id": "654",
                    "link": "https://example.com/artist?artistid=654",
                    "extraction_date": datetime.date(2026, 5, 6),
                },
                {
                    "first_name": "Smith",
                    "last_name": None,
                    "surname": None,
                    "artist_id": "111",
                    "link": "https://example.com/artist?artistid=111",
                    "extraction_date": datetime.date(2026, 5, 6),
                },
                {
                    "first_name": "Doe",
                    "last_name": None,
                    "surname": None,
                    "artist_id": "222",
                    "link": "https://example.com/artist?artistid=222",
                    "extraction_date": datetime.date(2026, 5, 6),
                },
                {
                    "first_name": "Brown",
                    "last_name": None,
                    "surname": None,
                    "artist_id": "333",
                    "link": "https://example.com/artist?artistid=333",
                    "extraction_date": datetime.date(2026, 5, 6),
                },
            ]
        )

from datetime import date
from src.stages.contracts.extract_contract import ExtractContract


def mock_extract_contract():
    ## this need to be accessible with .extraction_date and .raw_information_content
    return ExtractContract(
        extraction_date=date.today(),
        raw_information_content=[
            {"name": "Smith, John", "link": "https://example.com/artist?artistid=123"},
            {
                "name": "Smith, John, Jr.",
                "link": "https://example.com/artist?artistid=321",
            },
            {
                "name": "Brown, Bob III",
                "link": "https://example.com/artist?artistid=987",
            },
            {"name": "Doe, Jane", "link": "https://example.com/artist?artistid=456"},
            {"name": "Brown, Bob", "link": "https://example.com/artist?artistid=789"},
            {
                "name": "Doe, Jane, Sr.",
                "link": "https://example.com/artist?artistid=654",
            },
            {"name": "Smith", "link": "https://example.com/artist?artistid=111"},
            {"name": "Doe", "link": "https://example.com/artist?artistid=222"},
            {"name": "Brown", "link": "https://example.com/artist?artistid=333"},
        ],
    )

from src.drivers.mocks.http_collector_mock import mock_extract_contract
from src.stages.transform.transform_raw_data import TransformRawData


def test_transform():
    extract_contract = mock_extract_contract()

    transform_raw_data = TransformRawData()
    transformed_information = transform_raw_data.transform(extract_contract)

    assert isinstance(transformed_information, list)
    assert isinstance(transformed_information[0], dict)
    assert transformed_information[0]["first_name"] == "John"
    assert transformed_information[0]["last_name"] == "Smith"
    assert (
        transformed_information[0]["link"] == "https://example.com/artist?artistid=123"
    )

from src.drivers.mocks.http_collector_mock import mock_extract_contract
from src.errors.transform_error import TransformError
from src.stages.contracts.transform_contract import TransformContract
from src.stages.transform.transform_raw_data import TransformRawData


def test_transform():
    extract_contract = mock_extract_contract()

    transform_raw_data = TransformRawData()
    transformed_information = transform_raw_data.transform(extract_contract)

    assert isinstance(transformed_information, TransformContract)
    assert transformed_information.load_content[0]["first_name"] == "John"
    assert transformed_information.load_content[0]["last_name"] == "Smith"
    assert (
        transformed_information.load_content[0]["link"]
        == "https://example.com/artist?artistid=123"
    )


def test_transform_error():
    extract_contract = mock_extract_contract()
    extract_contract.raw_information_content[0]["link"] = "invalid_link"

    transform_raw_data = TransformRawData()

    try:
        transform_raw_data.transform(extract_contract)
    except Exception as exception:  # pylint: disable=broad-exception-caught
        assert isinstance(exception, TransformError)

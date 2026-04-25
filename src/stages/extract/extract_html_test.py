from unittest.mock import patch, MagicMock
import requests
from src.drivers.mocks.http_requester_mock import mock_request_from_page_sucess
from src.errors.extract_error import ExtractError
from src.stages.contracts.extract_contract import ExtractContract
from ...drivers.html_collector import HtmlCollector
from ...drivers.http_requester import HttpRequester
from ..extract.extract_html import ExtractHtml


@patch("requests.get")
def test_extract(mock_get):
    mock_success_results = mock_request_from_page_sucess()
    mock_value = MagicMock()
    mock_value.status_code = mock_success_results["status_code"]
    mock_value.text = mock_success_results["text"]
    mock_get.return_value = mock_value

    http_requester = HttpRequester()
    html_collector = HtmlCollector()
    extract_html = ExtractHtml(http_requester, html_collector)

    response = extract_html.extract()

    assert isinstance(response, ExtractContract)
    assert "name" in response[0][0]
    assert "link" in response[0][0]
    mock_get.assert_called_once_with(
        "https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm",
        timeout=10,
    )


@patch("requests.get")
def test_extract_error(mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError(
        "Failed to establish a new connection"
    )

    http_requester = HttpRequester()
    html_collector = HtmlCollector()
    extract_html = ExtractHtml(http_requester, html_collector)

    try:
        extract_html.extract()
    except Exception as exception:  # pylint: disable=broad-exception-caught
        assert isinstance(exception, ExtractError)

    assert mock_get.call_count == 1

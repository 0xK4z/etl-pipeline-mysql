from unittest.mock import patch, MagicMock
from .html_collector import HtmlCollector
from .http_requester import HttpRequester
from .mocks.http_requester_mock import mock_request_from_page_sucess

@patch("requests.get")
def test_collect_essential_information(mock_get):
    mock_success_results = mock_request_from_page_sucess()

    mock_value = MagicMock()
    mock_value.status_code = mock_success_results["status_code"]
    mock_value.text = mock_success_results["text"]
    mock_get.return_value = mock_value

    http_requester = HttpRequester()
    html_collector = HtmlCollector()

    essential_information = html_collector.collect_essential_information(
        http_requester.request_from_page()["html"]
    )

    assert isinstance(essential_information, list)
    assert isinstance(essential_information[0], dict)
    assert "name" in essential_information[0]
    assert "link" in essential_information[0]
    mock_get.assert_called_once_with(
        "https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm",
        timeout=10
    )

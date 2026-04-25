from unittest.mock import patch, MagicMock
from .http_requester import HttpRequester
from .mocks.http_requester_mock import mock_request_from_page_sucess

@patch("requests.get")
def test_request_from_page(mock_get):
    mock_success_results = mock_request_from_page_sucess()
    mock_response = MagicMock()
    mock_response.status_code = mock_success_results["status_code"]
    mock_response.text = mock_success_results["text"]

    mock_get.return_value = mock_response

    http_requester = HttpRequester()
    request_response = http_requester.request_from_page()

    assert "status_code" in request_response
    assert "html" in request_response
    assert request_response["status_code"] == 200
    assert request_response["html"] == mock_response.text

    mock_get.assert_called_once_with(
        "https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm",
        timeout=10
    )

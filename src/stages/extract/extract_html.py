from datetime import date

from src.drivers.interfaces.http_request import HttpRequesterInterface
from src.drivers.interfaces.html_collector import HtmlCollectorInterface
from src.stages.contracts.extract_contract import ExtractContract
from src.errors.extract_error import ExtractError

class ExtractHtml:

    def __init__(
        self,
        http_requester: HttpRequesterInterface,
        html_collector: HtmlCollectorInterface,
    ) -> None:
        self.__http_requester = http_requester
        self.__html_collector = html_collector

    def extract(self) -> ExtractContract:
        try:
            http_request_response = self.__http_requester.request_from_page()
            essential_information = self.__html_collector.collect_essential_information(
                http_request_response["html"]
            )
        except Exception as exception:
            raise ExtractError(str(exception)) from exception

        return ExtractContract(
            raw_information_content=essential_information,
            extraction_date=date.today(),
        )

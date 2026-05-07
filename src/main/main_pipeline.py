from src.stages.extract.extract_html import ExtractHtml
from src.stages.transform.transform_raw_data import TransformRawData
from src.stages.load.load_data import LoadData
from src.infra.database_connector import DatabaseConnector
from src.infra.database_repository import DatabaseRepository
from src.drivers.html_collector import HtmlCollector
from src.drivers.http_requester import HttpRequester


class MainPipeline:
    def __init__(self):
        self.extractor = ExtractHtml(HttpRequester(), HtmlCollector())
        self.transformer = TransformRawData()
        self.loader = LoadData(repository=DatabaseRepository())

    def run(self):
        try:
            raw_data = self.extractor.extract()
            transformed_data = self.transformer.transform(raw_data)
            self.loader.load_artist(transformed_data)
        except Exception as exception:  # pylint: disable=broad-exception-caught
            print(f"An error occurred during the ETL process: {str(exception)}")
        finally:
            DatabaseConnector.disconnect()

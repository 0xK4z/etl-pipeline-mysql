from typing import List, Dict

from src.errors.transform_error import TransformError
from src.stages.contracts.extract_contract import ExtractContract
from src.stages.contracts.transform_contract import TransformContract


class TransformRawData:

    def transform(self, extract_contract: ExtractContract) -> TransformContract:
        try:
            return TransformContract(
                load_content=self.__filter_and_transform_data(extract_contract)
            )
        except Exception as exception:
            raise TransformError(str(exception)) from exception

    def __filter_and_transform_data(
        self, extract_contract: ExtractContract
    ) -> List[Dict]:
        extracion_date = extract_contract.extraction_date
        data_content = extract_contract.raw_information_content
        transformed_information = []
        for data in data_content:
            transformed_data = None
            link = data["link"]

            if "artistid=" not in link:
                continue

            names = None

            if ", " in data["name"]:
                names = data["name"].split(", ")
            elif " " in data["name"]:
                names = data["name"].split(" ")
            else:
                names = [data["name"]]
            transformed_data = self.__transform_data(names, link)
            transformed_data["extraction_date"] = extracion_date
            transformed_information.append(transformed_data)
        return transformed_information

    def __transform_data(self, names: List, link: str) -> Dict:
        link_splited = link.split("artistid=")

        if len(names) == 2:
            return {
                "first_name": names[1],
                "last_name": names[0],
                "surname": None,
                "link": link,
                "artist_id": link_splited[1],
            }

        if len(names) == 3:
            return {
                "first_name": names[2],
                "last_name": names[0],
                "surname": names[1],
                "link": link,
                "artist_id": link_splited[1],
            }

        return {
            "first_name": names[0],
            "last_name": None,
            "surname": None,
            "link": link,
            "artist_id": link_splited[1],
        }

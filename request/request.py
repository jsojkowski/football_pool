import requests
import os
from abc import ABC
from typing import Dict, Final
import json

REQUEST_OK: Final = 200

class Requestor(ABC):

    def request(self, url: str, headers: Dict, querystring: Dict):

        response = requests.get(url, headers=headers, params=querystring).json()
        with open("request.json", "w+") as file:
            json.dump(response["body"], file, indent = 2)
        if int(response["statusCode"]) != REQUEST_OK:
            return None
        return response["body"]


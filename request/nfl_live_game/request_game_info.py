import os
from typing import Final, List
from request.request import Requestor
import datetime
from request.nfl_live_game.request_nfl_live_game import HOST, HEADERS

class RequestorNflGameInfo(Requestor):

    def request_game_info(self, game_date: int, home: str, away: str):
        # requestor_live_game.request_game_info("20240915", "DET", "TB")
        url = f"https://{HOST}/getNFLGameInfo"
        querystring = {"gameID":f"{game_date}_{away}@{home}"}
        return super().request(url, HEADERS, querystring)
        
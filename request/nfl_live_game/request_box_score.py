import os
from typing import Final, List
from request.request import Requestor
import datetime
from request.nfl_live_game.request_abstraction import HOST, HEADERS, GameId, FinalScore, get_request_game_id


class RequestorNflScore(Requestor):


    def request_box_score(self, game_id: str):
        # requestor_live_game.request_box_score("20240915", "DET", "TB")
        url = f"https://{HOST}/getNFLBoxScore"
        querystring = {"gameID":game_id,"playByPlay":"true",}

        return super().request(url, HEADERS, querystring)
    
    def request(self, game_date: int, home: str, away: str):
        request_game_id = get_request_game_id(game_date, home, away)
        request = self.request_box_score(request_game_id)
        if request is None:
            return [] 
        date = datetime.datetime(int(request["gameDate"][:4]), int(request["gameDate"][4:6]), int(request["gameDate"][6:]))
        game_id = GameId(home_team=request["teamStats"]["home"]["team"], away_team=request["teamStats"]["away"]["team"], date=date)
        final = request["scoringPlays"][-1]
        return FinalScore(game_id=game_id, home_score=int(final["homeScore"]), away_score=int(final["awayScore"]))

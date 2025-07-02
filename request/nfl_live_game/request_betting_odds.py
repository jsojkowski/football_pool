import os
from typing import Final, List
from request.request import Requestor
import datetime
from request.nfl_live_game.request_abstraction import GameId, Odds, HOST, HEADERS, get_request_game_id


class RequestorNflBettingOdds(Requestor):

    def request_betting_odds(self, game_id: str):
        # requestor_live_game.request_betting_odds(20240908)

        url = f"https://{HOST}/getNFLBettingOdds"
        querystring = {"gameID":game_id,"itemFormat":"list","impliedTotals":"true"}
        return super().request(url, HEADERS, querystring)
    
    def request(self, game_date: int, home: str, away: str) -> List[Odds]:
        request_game_id = get_request_game_id(game_date, home, away)
        game = self.request_betting_odds(request_game_id)
        if game is None:
            return None
        game_id = GameId(home_team=game["homeTeam"], away_team=game["awayTeam"], date=game_date)
        odds = game["sportsBooks"][0]["odds"]
        return Odds(game_id=game_id, 
                                away_spread=float(odds["awayTeamSpread"]),
                                home_spread=float(odds["homeTeamSpread"]),
                                implied_away_total=float(odds["impliedTotals"]["awayTotal"]),
                                implied_home_total=float(odds["impliedTotals"]["homeTotal"]),
        )
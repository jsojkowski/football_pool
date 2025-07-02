import os
from datetime import datetime
from request.nfl_live_game.request_games_for_week import RequestorNflGamesForWeek
from request.nfl_live_game.request_betting_odds import RequestorNflBettingOdds
from request.nfl_live_game.request_box_score import RequestorNflScore

def get_nfl_games(week: str):
    requestor_live_game = RequestorNflGamesForWeek()
    return requestor_live_game.request(week)

def get_odds(game_date: datetime, home: str, away: str):
    requestor_live_game = RequestorNflBettingOdds()
    return requestor_live_game.request(game_date, home, away)

def get_score(game_date: datetime, home: str, away: str):
    requestor_live_game = RequestorNflScore()
    return requestor_live_game.request(game_date, home, away)

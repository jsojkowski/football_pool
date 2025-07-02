from dataclasses import dataclass
from datetime import datetime
from typing import Final

def get_request_game_id(game_date: datetime, home: str, away: str):
    date_formatted = f"{game_date.year}{str(game_date.month).zfill(2)}{str(game_date.day).zfill(2)}"
    return f"{date_formatted}_{away}@{home}"


@dataclass
class GameId:
    home_team: str
    away_team: str
    date: datetime

@dataclass
class GameRequest:
    game_id: GameId
    status: str
    start_time: str
    week: str

@dataclass
class Odds:
    game_id: GameId
    away_spread: float
    home_spread: float
    implied_away_total: float
    implied_home_total: float

@dataclass
class FinalScore:
    game_id: GameId
    home_score: int
    away_score: int


HOST: Final = "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"

HEADERS: Final = {
    "x-rapidapi-key": "a77443fc07msh43a75439d5c82a0p1f9412jsnddb33f6b0e1e",
    "x-rapidapi-host": HOST
}

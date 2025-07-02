import datetime
from typing import Final

from dataclasses import dataclass


@dataclass
class Team:
    name: str = ""
    is_underdog: bool = False
    score: int = -1


@dataclass
class GameInfo:
    date: datetime = None
    week: str = ""
    status: str = ""
    game_winner: str = ""
    spread_winner: str = ""


@dataclass
class GameOdds:
    spread: float = 0.0
    implied_away_total: float = 0.0
    implied_home_total: float = 0.0


@dataclass
class Game:
    """Class for keeping track of a game."""

    home_team: Team = Team()
    away_team: Team = Team()
    info: GameInfo = GameInfo()
    odds: GameOdds = GameOdds()

    def set_score(self, home_score: int, away_score: int):
        self.home_team.score = home_score
        self.away_team.score = away_score
        self.info.game_winner = (
            self.home_team.name if home_score > away_score else self.away_team.name
        )
        final_spread = abs(home_score - away_score)
        if home_score > away_score:
            if self.home_team.is_underdog or final_spread >= self.odds.spread:
                # home team won and is the underdog OR home team won and is favorite and they beat the spread
                self.info.spread_winner = self.home_team.name
            else:
                self.info.spread_winner = self.away_team.name
        elif away_score > home_score:
            if self.away_team.is_underdog or final_spread >= self.odds.spread:
                # home team won and is the underdog OR home team won and is favorite and they beat the spread
                self.info.spread_winner = self.away_team.name
            else:
                self.info.spread_winner = self.home_team.name


NFL_SEASON_WEEKS: Final = {
    "1": datetime.datetime(2024, 9, 5),
    "2": datetime.datetime(2024, 9, 11),
    "3": datetime.datetime(2024, 9, 18),
    "4": datetime.datetime(2024, 9, 25),
    "5": datetime.datetime(2024, 10, 2),
    "6": datetime.datetime(2024, 10, 9),
    "7": datetime.datetime(2024, 10, 16),
    "8": datetime.datetime(2024, 10, 23),
    "9": datetime.datetime(2024, 10, 30),
    "10": datetime.datetime(2024, 11, 6),
    "11": datetime.datetime(2024, 11, 13),
    "12": datetime.datetime(2024, 11, 20),
    "13": datetime.datetime(2024, 11, 27),
    "14": datetime.datetime(2024, 12, 4),
    "15": datetime.datetime(2024, 12, 11),
    "16": datetime.datetime(2024, 12, 18),
    "17": datetime.datetime(2024, 12, 25),
    "18": datetime.datetime(2025, 1, 1),
    "Wild Card": datetime.datetime(2025, 1, 8),
    "Div Rd": datetime.datetime(2025, 1, 17),
    "Conf Champ": datetime.datetime(2025, 1, 24),
    "Pro Bowl": datetime.datetime(2025, 1, 31),
    "Super Bowl": datetime.datetime(2025, 2, 7),
}

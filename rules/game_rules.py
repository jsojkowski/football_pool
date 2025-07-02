from common.logging import Logger
from datetime import datetime
from typing import Dict, List, Final
from request.nfl_live_game.request_nfl_live_game import (
    get_nfl_games,
    get_odds,
    get_score,
)
from entities.game import Game
import copy
import glob
import json
import dataclasses


# .weekday() returns the day of the week‚ as an integer, where Monday is 0 and Sunday is 6.
# This makes Thursday 3
THURSDAY = 3


def is_game_on_thursday(game_date: datetime):
    return game_date.weekday() == 3


class Games:
    """Class to hold the model of all the games."""

    def __init__(self, week: str) -> None:
        """Initialize all of the desired games."""
        self.games = {}
        self.initialize_games(week)
        self.dump()

    def initialize_games(self, week: int = None):
        # TODO: load a cache of games for the year from stored JSON files
        # get all of the games
        games = get_nfl_games(week)
        # populate the class game structure
        for game in games:
            if is_game_on_thursday(game.game_id.date):
                continue
            new_game = Game()
            new_game.home_team.name = game.game_id.home_team
            new_game.away_team.name = game.game_id.away_team
            time = game.start_time.split(":")
            new_game.info.date = game.game_id.date.replace(
                hour=int(time[0]), minute=int(time[1][:-1])
            )
            new_game.info.week = game.week
            new_game.info.status = game.status

            odds = get_odds(
                new_game.info.date, new_game.home_team.name, new_game.away_team.name
            )
            new_game.odds.spread = abs(odds.away_spread)
            # The team that is the favorite to win gets the minus-number (-3); the underdog gets the plus-number (+3)
            if odds.away_spread > 0:
                new_game.away_team.is_underdog = True
            elif odds.home_spread > 0:
                new_game.home_team.is_underdog = True
            new_game.odds.implied_away_total = odds.implied_away_total
            new_game.odds.implied_home_total = odds.implied_home_total

            score = get_score(
                new_game.info.date, new_game.home_team.name, new_game.away_team.name
            )
            new_game.set_score(score.home_score, score.away_score)

            game_to_add = copy.deepcopy(new_game)
            if game_to_add.info.week not in self.games.keys():
                self.games[game_to_add.info.week] = []
            self.games[game_to_add.info.week].append(game_to_add)

    def dump(self):
        games_list = []
        for week, games in self.games.items():
            for game in games:
                games_list.append(dataclasses.asdict(game))
            
            games_json = {f"week_{week}": games_list}
            with open(
                f"/Users/juliesojkowski/repo/football/data/week_{week}.json", "w"
            ) as cache_file:
                cache_file.write(json.dumps(games_json, indent=4, default=str))

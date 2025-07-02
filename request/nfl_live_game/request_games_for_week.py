import os
from typing import Final, List, Any, Dict
from request.request import Requestor
from request.nfl_live_game.request_abstraction import GameRequest, GameId, HOST, HEADERS
import datetime
from common.logging import Logger


class RequestorNflGamesForWeek(Requestor):

    def request_games_for_week(self, week: str) -> Dict[str, Any]:
        """Send the HTTPS Request for Games of the Week

        Args:
            week (str): The Name of the week

        Returns:
            Dict[str, Any]: The body of the request, assuming the actual request does not throw
        """
        url = f"https://{HOST}/getNFLGamesForWeek"
        querystring = {"week": str(week), "seasonType": "reg", "season": "2024"}
        body = super().request(url, HEADERS, querystring)
        return body

    def request(self, week: str) -> List[GameRequest]:
        """Request all the games for a week.

        Args:
            week (str): The week for the games

        Returns:
            List[GameRequest]: A lit of games for the week, or an empty list
        """
        # requestor_live_game.get_games_for_week(2)
        request = self.request_games_for_week(week)
        if request is None:
            Logger().error(f"No games for that week. Is what you entered ann invalid week:{week}")
            return []
        all_games: List[GameRequest] = []
        for game in request:
            week = game["gameWeek"]
            if "Week " in game["gameWeek"]:
                week = game["gameWeek"].split()[1]

            date = datetime.datetime(
                int(game["gameDate"][:4]),
                int(game["gameDate"][4:6]),
                int(game["gameDate"][6:]),
            )
            game_id = GameId(home_team=game["home"], away_team=game["away"], date=date)
            all_games.append(
                GameRequest(
                    game_id=game_id,
                    status=game["gameStatus"],
                    start_time=game["gameTime"],
                    week=week,
                )
            )
        return all_games

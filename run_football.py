import argparse
from typing import List
import os
import sys
from rules.game_rules import Games
from common.logging import Logger, LogLevel


def main(argv: List[str]) -> int:
    """Main Method.

    Args:
        argv (List[str]): List of arguments for the Main

    Returns:
        int: The return code of the Main
    """
    parser = argparse.ArgumentParser(
                    prog='Football Stats',
                    description='Get football stats for a week.')
    parser.add_argument('-l', '--log_level',type=LogLevel, choices=list(LogLevel), default=LogLevel.INFO)
    # parser.add_argument('-v', '--verbose',
    #                 action='store_true')  # on/off flag
    args = parser.parse_args()
    Logger(LogLevel(args.log_level))
    Games("4")

    return os.EX_OK


# Using the special variable
# __name__
if __name__ == "__main__" and len(sys.argv) > 0:
    main(sys.argv)

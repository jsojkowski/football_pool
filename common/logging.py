from enum import Enum


# class syntax
class LogLevel(str, Enum):
    INFO_DEFAULT = None
    INFO = "info"
    DEBUG = "debug"
    ERROR = "error"


def is_log_level(obj: str) -> bool:
    """Check if a string is a log level

    Args:
        obj (str): The string to check

    Returns:
        bool: True if the string is a valid log level
    """
    try:
        LogLevel(obj)
    except ValueError:
        return False
    return True


class Colors(Enum):
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class Logger(object):
    """The logging class."""

    def __init__(self, level: str = "") -> None:
        """Initialize the logger with the logging level.

        Args:
            level (str): The logger level as a string, defaults to None.
        """
        if is_log_level(level):
            self.log_level = level
        else:
            self.log_level = LogLevel.INFO_DEFAULT
   
    def info(self, message: str) -> None:
        """Print an info logging message.

        Args:
            message (str): The info message to print.
        """
        if self.log_level == LogLevel.DEBUG or self.log_level == LogLevel.INFO or self.log_level == LogLevel.INFO_DEFAULT:
            print("\033[98m {}\033[00m".format(message))
            # print("{Colors.OKBLUE}[INFO]:{}{Colors.ENDC}".format(message))

    def warning(self, message: str) -> None:
        """Print an warning logging message

        Args:
            message (str): The warning message to print
        """
        if self.log_level == LogLevel.DEBUG:
            print(f"{Colors.WARNING}[WARNING]:{message}{Colors.ENDC}")

    def error(self, message: str) -> None:
        """Print an error logging message.

        Args:
            message (str): The error message to print.
        """
        print("\033[98m {}\033[00m".format(message))
        print(f"{Colors.FAIL}[FAIL]:{message}{Colors.ENDC}")

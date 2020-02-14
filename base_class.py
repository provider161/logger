
from .logger import get_logger, get_caller_name


class BaseClass:

    def __init__(self, name):

        self._name = name

        self._logger = get_logger(name=self._name)

    def _write_log(self, level, text, caller_name=None):
        """Wrapper for simple logging and publishing.

        Parameters
        ----------
        level : str
            Logging level (INFO, WARNING, ERROR, CRITICAL or DEBUG).
        text : str
            Additional info.
        caller_name : str
            The name of a caller of this function.
        """

        if caller_name is None:
            caller_name = get_caller_name()

        if level == 'INFO':
            self._logger.info(
                self.__class__.__name__ + "." + caller_name +
                " : " + text
            )

        elif level == 'WARNING':
            self._logger.warning(
                self.__class__.__name__ + "." + caller_name +
                " : " + text
            )

        elif level == 'ERROR':
            self._logger.error(
                self.__class__.__name__ + "." + caller_name +
                " : " + text
            )

        elif level == 'CRITICAL':
            self._logger.critical(
                self.__class__.__name__ + "." + caller_name +
                " : " + text
            )

        elif level == "DEBUG":
            self._logger.debug(
                self.__class__.__name__ + "." + caller_name +
                " : " + text
            )

    def log_info(self, text, caller_name=None):

        self._write_log(level="INFO", text=text, caller_name=caller_name)

    def log_warning(self, text, caller_name=None,):

        self._write_log(level="WARNING", text=text, caller_name=caller_name)

    def log_error(self, text, caller_name=None,):

        self._write_log(level="ERROR", text=text, caller_name=caller_name)

    def log_fatal(self, text, caller_name=None,):

        self._write_log(level="FATAL", text=text, caller_name=caller_name)

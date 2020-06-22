import inspect
import datetime

from functools import wraps

# ---- Decorators ----
def get_source(func):
    """
        Decorator to get function caller info
    """

    @wraps(func)
    def src_info(*args, **kwargs):
        _caller = inspect.stack()[1][1]
        _line = inspect.stack()[1][2]
        return func(caller=_caller, line=_line, *args, **kwargs)

    return src_info


# ---- Logging ----
class LOG():
    """
        Utility logging class to make lambda debuging easier.
    """

    def __init__(self):
        """
            default constructor
        """

    def _fmt_log(self, log_type, caller, line, message):
        """
        Format log string in this format: TYPE - LOCATION - Message
        ex. Debug message
            DEBUG - cron.hourly_event - Successfuly broadcasted new hourly event
        """
        st = datetime.datetime.utcnow()
        return "[{0} {1}] [{2}] [{3}] {4}".format(log_type.upper(), st, caller, line, message)

    @get_source
    def debug(self, message, caller="", line=""):
        """
            Print DEBUG message
        """
        print(self._fmt_log("debug", caller, line, message))

    @get_source
    def info(self, message, caller="", line=""):
        """
            Print INFO message
        """
        print(self._fmt_log("info", caller, line, message))

    @get_source
    def warn(self, message, caller="", line=""):
        """
            Print WARNING message
        """
        print(self._fmt_log("warning", caller, line, message))

    @get_source
    def error(self, message, caller="", line=""):
        """
            Print ERROR message
        """
        print(self._fmt_log("error", caller, line, message))

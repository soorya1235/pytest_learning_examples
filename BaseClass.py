import inspect
import logging

class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        handler = logging.FileHandler('logifile.log')
        setformat = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        handler.setFormatter(setformat)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger


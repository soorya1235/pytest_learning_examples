import logging

def  test_logging():
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler('logifile.log')
    setformat = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    handler.setFormatter(setformat)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")

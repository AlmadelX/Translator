import logging
import os


class Logger:
    LOGGING_FORMAT = '%(asctime)s %(levelname)-8s %(message)s'
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

    def __init__(self):
        logging.basicConfig(
            filename=os.getenv('LOGFILE'),
            encoding='utf-8',
            level=logging.INFO,
            format=self.LOGGING_FORMAT,
            datefmt=self.DATE_FORMAT)

    def info(self, message):
        logging.info(message)

    def warn(self, message):
        logging.warning(message)

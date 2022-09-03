import logging


class Logger:
    LOGGING_FORMAT = '%(asctime)s %(levelname)-8s %(message)s'
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

    def __init__(self, filename):
        self.filename = filename

        logging.basicConfig(
            format=self.LOGGING_FORMAT,
            datefmt=self.DATE_FORMAT)
        logging.info('Started translating', self.filename)

    def __del__(self):
        pass

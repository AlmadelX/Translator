import logging


class Logger:
    __LOGGING_FORMAT = '%(asctime)s %(levelname)-8s %(message)s'
    __DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    __ENCODING = 'utf-8'

    def __init__(self, log_filename: str):
        logging.basicConfig(
            filename=log_filename,
            encoding=self.__ENCODING,
            level=logging.INFO,
            format=self.__LOGGING_FORMAT,
            datefmt=self.__DATE_FORMAT
        )
        logging.getLogger('deepl').disabled = True

    @staticmethod
    def warn(message: str):
        logging.warning(message)

    @staticmethod
    def info(message: str):
        logging.info(message)

from configparser import ConfigParser
from glob import glob
from os.path import join
from typing import Tuple, Optional

from dotenv import load_dotenv

from src.html_processor import HTMLProcessor
from src.logger import Logger


def get_user_input() -> Tuple[str, str, str, Optional[str]]:
    config_parser = ConfigParser()
    config_parser.read('config.ini')
    return (
        config_parser['CONFIG']['DIRECTORY'],
        config_parser['CONFIG']['LOG_FILE'],
        config_parser['CONFIG']['LANGUAGE'],
        config_parser['CONFIG']['GLOSSARY']
    )


def main():
    load_dotenv()
    directory_name, log_filename, language, glossary = get_user_input()

    logger = Logger(log_filename)

    for filename in glob(join(directory_name, '*.html')):
        processor = HTMLProcessor(filename, language, glossary, logger)
        processor.process()

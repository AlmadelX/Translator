import argparse
from typing import Tuple, Optional

from dotenv import load_dotenv

from src.html_processor import HTMLProcessor


def get_user_input() -> Tuple[str, str, str, Optional[str]]:
    arguments_parser = argparse.ArgumentParser()
    arguments_parser.add_argument('-f', type=str, required=True)
    arguments_parser.add_argument('--logfile', type=str, required=True)
    arguments_parser.add_argument('--language', type=str, required=True)
    arguments_parser.add_argument('--glossary', type=str, required=False)
    arguments = arguments_parser.parse_args()
    return (
        arguments.f,
        arguments.logfile,
        arguments.language,
        arguments.glossary
    )


def main():
    load_dotenv()

    filename, log_filename, language, glossary = get_user_input()

    processor = HTMLProcessor(filename, log_filename, language, glossary)
    processor.process()

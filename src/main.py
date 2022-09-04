import argparse
from typing import Tuple, Optional

from dotenv import load_dotenv

from src.html_processor import HTMLProcessor


def get_user_input() -> Tuple[str, str, Optional[str]]:
    arguments_parser = argparse.ArgumentParser()
    arguments_parser.add_argument('-f', type=str, required=True)
    arguments_parser.add_argument('--language', type=str, required=True)
    arguments_parser.add_argument('--glossary', type=str, required=False)
    arguments = arguments_parser.parse_args()
    return arguments.f, arguments.language, arguments.glossary


def main():
    load_dotenv()

    filename, language, glossary = get_user_input()

    processor = HTMLProcessor(filename, language, glossary)
    processor.process()

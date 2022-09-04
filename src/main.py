import argparse

from dotenv import load_dotenv

from src.html_processor import HTMLProcessor


def get_filename() -> str:
    arguments_parser = argparse.ArgumentParser()
    arguments_parser.add_argument('-f', type=str, required=True)
    arguments = arguments_parser.parse_args()
    return arguments.f


def main():
    load_dotenv()

    filename = get_filename()

    processor = HTMLProcessor(filename)
    processor.process()

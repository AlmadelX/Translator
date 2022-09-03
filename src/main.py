import argparse
import shutil

from dotenv import load_dotenv

from src.html_parser import HTMLParser
from src.logger import Logger


def get_input():
    arguments_parser = argparse.ArgumentParser()
    arguments_parser.add_argument('-i', type=str, required=True)
    arguments_parser.add_argument('-o', type=str, required=True)
    arguments = arguments_parser.parse_args()
    input_filename = arguments.i
    output_filename = arguments.o
    return input_filename, output_filename


def main():
    load_dotenv()
    input_filename, output_filename = get_input()
    logger = Logger()
    logger.info(f'Started translating {input_filename}')
    shutil.copyfile(input_filename, output_filename)
    parser = HTMLParser(output_filename)
    logger.info(f'Finished translating {input_filename} into {output_filename}')

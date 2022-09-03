import argparse


def get_input():
    arguments_parser = argparse.ArgumentParser()
    arguments_parser.add_argument('-i', type=str, required=True)
    arguments_parser.add_argument('-o', type=str, required=True)
    arguments = arguments_parser.parse_args()
    input_filename = arguments.i
    output_filename = arguments.o
    return input_filename, output_filename


def main():
    input_filename, output_filename = get_input()
    print(input_filename)
    print(output_filename)

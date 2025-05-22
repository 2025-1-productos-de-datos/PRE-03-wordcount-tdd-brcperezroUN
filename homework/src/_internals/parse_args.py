import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Count words in files")
    parser.add_argument("input", help="path of input folder")
    parser.add_argument("output", help="path of output folder")

    args = parser.parse_args()

    input_folder = args.input
    output_folder = args.output

    return input_folder, output_folder

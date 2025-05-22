# import subprocess
import os
import shutil
import sys

from ..count_words import count_words
from ..parse_args import parse_args
from ..preprocess_lines import preprocess_lines
from ..read_all_lines import read_all_lines
from ..split_into_words import split_into_words
from ..write_word_counts import write_word_counts


def test_parse_args():
    test_args = ["homework", "data/input/", "data/output/"]
    sys.argv = test_args

    input_folder, output_folder = parse_args()
    assert input_folder == test_args[1]
    assert output_folder == test_args[2]


def test_real_all_lines():
    input_foler = "data/input/"
    lines = read_all_lines(input_foler)
    assert len(lines) > 0
    assert any(
        "Analytics refers to the systematic computational analysis of data " in line
        for line in lines
    )


def test_preprocess_lines():
    lines = [" Hello World! ", "Python is GREAT."]
    preprocessed_lines = preprocess_lines(lines)
    assert preprocessed_lines == ["hello world!", "python is great."]


def test_split_into_words():
    lines = ["hello world!", "python is great."]
    words = split_into_words(lines)
    assert words == ["hello", "world", "python", "is", "great"]


def test_count_words():
    words = ["hello", "world", "hello", "python"]
    word_counts = count_words(words)
    assert word_counts == {"hello": 2, "world": 1, "python": 1}


def test_write_word_counts():
    output_folder = "data/test_output"
    word_counts = {"hello": 2, "world": 1, "python": 1}

    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    write_word_counts(output_folder, word_counts)

    output_file = os.path.join(output_folder, "wordcount.tsv")
    assert os.path.exists(output_file), "Output file was not created"

    with open(output_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    assert lines == ["hello\t2\n", "world\t1\n", "python\t1\n"]

    shutil.rmtree(output_folder)

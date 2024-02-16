"""
ccwc - word, line, character, and byte count.

Author: @tonybnya
"""
from typing import Callable, List
import argparse


def ccwc_bytes(filename: str) -> int:
    """
    Count number of bytes

    :param filename: path to the text file
    :return: number of bytes
    """
    with open(filename, 'rb') as file:
        bytes = 0

        for byte in file.read():
            bytes += 1

    return bytes


def ccwc_chars(filename: str) -> int:
    """
    Count number of chars

    :param filename: path to the text file
    :return: number of characters
    """
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    return len(text)


def ccwc_lines(filename: str) -> int:
    """
    Count number of lines

    :param filename: path to the text file
    :return: number of lines
    """
    with open(filename) as file:
        lines = file.readlines()

    return len(lines)


def ccwc_words(filename: str) -> int:
    """
    Count number of words

    :param filename: path to the text file
    :return: number of words
    """
    with open(filename) as file:
        words = file.read()

    return len(words.split())


def count_print(func: Callable, filenames: List[str]) -> None:
    """
    :param func: function as corresponding counter
    :param filenames: list of paths
    :return: nothing
    """
    data = [(func(filename), filename) for filename in filenames]

    if len(data) > 1:
        total = sum(count for count, _ in data)
        data.append((total, 'total'))

    max_length = max(len(str(count)) for count, _ in data)

    for count, filename in data:
        print(f"{count:>{max_length + 2}} {filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-c', type=str, nargs='*', help='Count bytes')
    parser.add_argument('-l', type=str, nargs='*', help='Count lines')
    parser.add_argument('-m', type=str, nargs='*', help='Count characters')
    parser.add_argument('-w', type=str, nargs='*', help='Count words')

    args = parser.parse_args()

    if args.c:
        count_print(ccwc_bytes, args.c)
    elif args.l:
        count_print(ccwc_lines, args.l)
    elif args.m:
        count_print(ccwc_chars, args.m)
    elif args.w:
        count_print(ccwc_words, args.w)

"""
ccwc - word, line, character, and byte count.

Author: @tonybnya
"""
from typing import Tuple
import sys


def ccwc_bytes(filename: str) -> int:
    """
    Count number of bytes

    :param textfile: the path to the text file
    :return: the number of bytes in the file
    """
    with open(filename, 'rb') as file:
        bytes = 0

        for byte in file.read():
            bytes += 1

    return bytes


def ccwc_chars(filename: str) -> int:
    """
    Count number of chars

    :param textfile: the path to the text file
    :return: the number of characters in the file
    """
    with open(filename) as file:
        words = file.read()

    return len(words)


def ccwc_lines(filename: str) -> int:
    """
    Count number of lines

    :param textfile: the path to the text file
    :return: the number of lines in the file
    """
    with open(filename) as file:
        lines = file.readlines()

    return len(lines)


def ccwc_words(filename: str) -> int:
    """
    Count number of words

    :param textfile: the path to the text file
    :return: the number of words in the file
    """
    with open(filename) as file:
        words = file.read()

    return len(words.split())


def ccwc(filename: str) -> Tuple[int, int, int, int]:
    """
    Main function

    :param:
    :return: a tuple of the number of lines, bytes, characters, and words
    """
    bytes = ccwc_bytes(filename)
    characters = ccwc_chars(filename)
    lines = ccwc_lines(filename)
    words = ccwc_words(filename)

    return bytes, characters, lines, words


if __name__ == "__main__":
    args = sys.argv

    if len(args) == 1:
        with open('usage.txt') as usage:
            print(usage.read())

        sys.exit(0)

    filename = args[1]
    bytes = ccwc_bytes(filename)
    chars = ccwc_chars(filename)
    lines = ccwc_lines(filename)
    words = ccwc_words(filename)

    data = [bytes, chars, lines, words]
    max_length = max(len(str(item)) for item in data)

    for item in data:
        print(f"{item:>{max_length + 2}} {filename}")

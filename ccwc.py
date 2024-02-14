"""
ccwc - word, line, character, and byte count.

Author: @tonybnya
"""
from typing import IO
import sys


def ccwc_bytes(filename: IO) -> int:
    """
    Count number of bytes

    :param textfile: string containing the path to a text file
    :return: int representing the number of bytes
    """
    with open(filename, 'rb') as file:
        bytes = 0

        for byte in file.read():
            bytes += 1

    return bytes


# def ccwc_lines(filename: IO) -> int:
#     """
#     Count number of lines
#
#     :param textfile: string containing the path to a text file
#     :return: int representing the number of lines
#     """
#     with open(filename) as file:
#         lines = file.readlines()
#
#     return len(lines)
#
#
# def ccwc_words(filename: IO) -> int:
#     """
#     Count number of words
#
#     :param textfile: string containing the path to a text file
#     :return: int representing the number of words
#     """
#     with open(filename) as file:
#         words = file.read()
#
#     return len(words.split())
#
#
# def ccwc_chars(filename: IO) -> int:
#     """
#     Count number of chars
#
#     :param textfile: string containing the path to a text file
#     :return: int representing the number of chars
#     """
#     pass


if __name__ == "__main__":
    args = sys.argv
    print(ccwc_bytes(args[1]))
    # print(ccwc_lines(args[1]))
    # print(ccwc_words(args[1]))
    # print(ccwc_chars(args[1]))

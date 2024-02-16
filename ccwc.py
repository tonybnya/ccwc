"""
ccwc - word, line, character, and byte count.

Author: @tonybnya
"""
from typing import Callable, Sequence, Union
import argparse
import sys


def ccwc_bytes(source: Union[str, None]) -> int:
    """
    Count number of bytes

    :param source: path to the text file or None for standard input
    :return: number of bytes
    """
    bytes = 0
    if source:
        with open(source, 'rb') as file:
            for byte in file.read():
                bytes += 1
    else:
        bytes = len(sys.stdin.buffer.read())

    return bytes


def ccwc_chars(source: Union[str, None]) -> int:
    """
    Count number of chars

    :param source: path to the text file or None for standard input
    :return: number of characters
    """
    if source:
        with open(source, 'r', encoding='utf-8') as file:
            chars = file.read()
    else:
        chars = sys.stdin.read()

    return len(chars)


def ccwc_lines(source: Union[str, None]) -> int:
    """
    Count number of lines

    :param source: path to the text file or None for standard input
    :return: number of lines
    """
    if source:
        with open(source) as file:
            lines = file.readlines()
    else:
        lines = sys.stdin.readlines()

    return len(lines)


def ccwc_words(source: Union[str, None]) -> int:
    """
    Count number of words

    :param source: path to the text file or None for standard input
    :return: number of words
    """
    if source:
        with open(source) as file:
            words = file.read()
    else:
        words = sys.stdin.read()

    return len(words.split())


def count_print(func: Callable, sources: Sequence[Union[str, None]]) -> None:
    """
    :param func: function as corresponding counter
    :param sources: list of file paths or None for standard input
    :return: nothing
    """
    data = [(func(source), source) for source in sources]

    if len(data) > 1:
        total = sum(count for count, _ in data)
        data.append((total, 'total'))

    max_length = max(len(str(count)) for count, _ in data)

    for count, source in data:
        print(f"{count:>{max_length + 2}} {source}")


if __name__ == "__main__":
    if len(sys.argv) == 2 and not sys.argv[1].startswith('-'):
        source = sys.argv[1]

        lines = ccwc_lines(source)
        words = ccwc_words(source)
        bytes = ccwc_bytes(source)

        max_length = max(len(str(count)) for count in [bytes, lines, words])

        print(f"{lines:>{max_length + 2}}{words:>{max_length + 2}}{bytes:>{max_length + 2}} {source}")
        sys.exit(0)

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
    else:
        if sys.argv[-1] == '-c':
            count_print(ccwc_bytes, [''])
        elif sys.argv[-1] == '-l':
            count_print(ccwc_lines, [''])
        elif sys.argv[-1] == '-m':
            count_print(ccwc_chars, [''])
        elif sys.argv[-1] == '-w':
            count_print(ccwc_words, [''])

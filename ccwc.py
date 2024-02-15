"""
ccwc - word, line, character, and byte count.

Author: @tonybnya
"""
import argparse


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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-c', type=str, nargs='*', help='Count the number of bytes')
    parser.add_argument('-l', type=str, nargs='*', help='Count the number of lines')
    parser.add_argument('-m', type=str, nargs='*', help='Count the number of characters')
    parser.add_argument('-w', type=str, nargs='*', help='Count the number of words')

    args = parser.parse_args()

    if len(args.c) != 1:
        data = []
        for filename in args.c:
            data.append((ccwc_bytes(filename), filename))

        total = 0
        for item in data:
            total += item[0]

        data.append((total, 'total'))
        max_length = max(len(str(item[0])) for item in data)

        for item in data:
            print(f"{item[0]:>{max_length + 2}} {item[1]}")
    else:
        filename = args.c[0]
        print(f"{ccwc_bytes(filename):>{len(filename)}} {filename}")

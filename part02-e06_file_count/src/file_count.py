#!/usr/bin/env python3

import sys


def file_count(filename):
    with open(filename, "r") as in_file:
        nr_of_lines = nr_of_words = nr_of_characters = 0

        for line in in_file:
            # Increment lines
            nr_of_lines += 1
            nr_of_characters += len(line)
            # Increment words
            words_in_line = line.split()
            nr_of_words += len(words_in_line)

    return (nr_of_lines, nr_of_words, nr_of_characters)


def main():
    file_list = sys.argv[1:]

    for file in file_list:
        lines, words, chars = file_count(file)
        print(f"{lines}\t{words}\t{chars}\t{file}")


if __name__ == "__main__":
    main()

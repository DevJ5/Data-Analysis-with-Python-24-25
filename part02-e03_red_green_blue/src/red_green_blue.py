#!/usr/bin/env python3

import re


def red_green_blue(filename="src/rgb.txt"):
    result = []

    with open(filename, "r") as in_file:
        next(in_file)
        for line in in_file:
            match = re.search(
                r"^(\s*\d{1,3})\s+(\d{1,3})\s+(\d{1,3})\s+([\w ]+)$", line
            )
            result.append("\t".join(match.groups()))

    return result


def main():
    print(red_green_blue())


if __name__ == "__main__":
    main()

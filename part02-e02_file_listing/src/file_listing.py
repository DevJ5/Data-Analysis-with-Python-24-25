#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    result = []
    with open(filename, "r") as f:
        for line in f:
            match = re.search(
                r"[a-z-]+\s+\d\s+\w+\s+[\w-]+\s+(\d+)\s+(\w+)\s+(\d+)\s+(\d+):(\d+)\s+([\w.]+)",
                line,
            )

            size, month, day, hour, minute, filename = match.groups()
            result.append(
                (int(size), month, int(day), int(hour), int(minute), filename)
            )

    return result


def main():
    print(file_listing())


if __name__ == "__main__":
    main()

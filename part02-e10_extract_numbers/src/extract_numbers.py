#!/usr/bin/env python3


def extract_numbers(s):
    result = []
    parts = s.split()
    for part in parts:
        try:
            part = int(part)
            result.append(part)
        except ValueError:
            try:
                part = float(part)
                result.append(part)
            except ValueError:
                pass

    return result


def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))


if __name__ == "__main__":
    main()

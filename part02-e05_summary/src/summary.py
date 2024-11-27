#!/usr/bin/env python3

import sys, math


def summary(filename):
    with open(filename, "r") as in_file:
        numbers = []

        for line in in_file:
            try:
                f = float(line)
                numbers.append(f)
            except ValueError:
                pass

    count = len(numbers)
    total_sum = sum(numbers)
    avg = total_sum / count

    sum_squared_errors = 0
    for x in numbers:
        sum_squared_errors += (x - avg) ** 2

    std_dev = math.sqrt(sum_squared_errors / (count - 1))

    return (total_sum, avg, std_dev)


def main():
    files = sys.argv[1:]
    for file in files:
        total_sum, avg, std_dev = summary(file)
        print(
            f"File: {file} Sum: {total_sum:.6f} Average: {avg:.6f} Stddev: {std_dev:.6f}"
        )


if __name__ == "__main__":
    main()

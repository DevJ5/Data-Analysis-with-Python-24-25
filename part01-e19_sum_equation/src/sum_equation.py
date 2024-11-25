#!/usr/bin/env python3
from functools import reduce


def sum_equation(L):
    if len(L) == 0:
        return "0 = 0"
    total_sum = reduce(lambda x, y: x + y, L, 0)
    equation = " + ".join(map(str, L))
    return f"{equation} = {total_sum}"


def main():
    print(sum_equation([0]))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import numpy as np


def get_rows(a):
    row_list = [row for row in a]
    return row_list


def get_columns(a):
    a = np.transpose(a)
    column_list = [column for column in a]

    return column_list


def main():
    np.random.seed(0)
    a = np.random.randint(0, 10, (4, 4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))


if __name__ == "__main__":
    main()

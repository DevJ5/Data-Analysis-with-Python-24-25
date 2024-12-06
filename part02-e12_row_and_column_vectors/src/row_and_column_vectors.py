#!/usr/bin/env python3

import numpy as np


def get_row_vectors(a):
    row_vectors = [row.reshape(1, len(row)) for row in a]
    return row_vectors


def get_column_vectors(a):
    column_vectors = [column.reshape(len(column), 1) for column in np.transpose(a)]
    return column_vectors


def main():
    np.random.seed(0)
    a = np.random.randint(0, 10, (4, 4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))


if __name__ == "__main__":
    main()

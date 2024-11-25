#!/usr/bin/env python3


def transform(s1, s2):
    list_1 = s1.split()
    list_2 = s2.split()
    merged_list = list(zip(list_1, list_2))
    result = list(map(lambda x: int(x[0]) * int(x[1]), merged_list))
    return result


def main():
    print(transform("1 5 3", "2 6 -1"))


if __name__ == "__main__":
    main()

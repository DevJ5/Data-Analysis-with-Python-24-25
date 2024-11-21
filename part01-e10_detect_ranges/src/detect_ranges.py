#!/usr/bin/env python3


def detect_ranges(L):
    sortedL = sorted(L)
    result = []
    a_range = None

    for i, number in enumerate(sortedL):
        if i + 1 < len(sortedL) and number + 1 == sortedL[i + 1]:
            if a_range == None:
                a_range = (number, sortedL[i + 1] + 1)
            else:
                a_range = (a_range[0], sortedL[i + 1] + 1)
        else:
            if a_range == None:
                a_range = number
            result.append(a_range)
            a_range = None

    return result


def main():
    # L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    L = [2, 4, 5, 6, 7, 8, 10, 12, 13]
    result = detect_ranges(L)
    print(L)
    print(result)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3


# len(L1 if len(L1 >= L2) else L2
def merge(L1, L2):
    result = []

    i = j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] <= L2[j]:
            result.append(L1[i])
            i += 1
        else:
            result.append(L2[j])
            j += 1

    result = result + L1[i:] + L2[j:]

    return result


def main():
    print(merge([1, 2, 3], [3, 4, 5, 6]))


if __name__ == "__main__":
    main()

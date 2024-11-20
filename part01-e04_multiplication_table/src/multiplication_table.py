#!/usr/bin/env python3


def main():
    for i in range(1, 11):
        for j in range(1, 11):
            result = i * j
            if j == 10:
                print(f"{result:4d}")
            else:
                print(f"{result:4d}", end="")


if __name__ == "__main__":
    main()

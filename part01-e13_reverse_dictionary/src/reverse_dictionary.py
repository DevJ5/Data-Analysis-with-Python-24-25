#!/usr/bin/env python3


def reverse_dictionary(d):
    reversed_d = {}
    for k, v in d.items():
        for word in v:
            if reversed_d.get(word) == None:
                reversed_d[word] = [k]
            else:
                reversed_d[word].append(k)
    return reversed_d


def main():
    d = {
        "move": ["liikuttaa"],
        "hide": ["piilottaa", "salata"],
        "six": ["kuusi"],
        "fir": ["kuusi"],
    }

    print(reverse_dictionary(d))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3


def word_frequencies(filename):
    result = {}
    with open(filename, "r") as in_file:
        for line in in_file:
            words = line.split()
            if len(words):
                for word in words:
                    word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                    result[word] = result[word] + 1 if result.get(word) != None else 1

    return result


def main():
    print(word_frequencies("src/alice2.txt"))


if __name__ == "__main__":
    main()

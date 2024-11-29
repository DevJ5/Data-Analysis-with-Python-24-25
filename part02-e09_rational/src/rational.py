#!/usr/bin/env python3


class Rational(object):
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    def __str__(self):
        return f"{self.nominator}/{self.denominator}"

    def __add__(self, r):
        denominator = self.denominator * r.denominator
        nominator = r.denominator * self.nominator + self.denominator * r.nominator
        return Rational(nominator, denominator)

    def __sub__(self, r):
        denominator = self.denominator * r.denominator
        nominator = r.denominator * self.nominator - self.denominator * r.nominator
        return Rational(nominator, denominator)

    def __mul__(self, r):
        denominator = self.denominator * r.denominator
        nominator = self.nominator * r.nominator
        return Rational(nominator, denominator)

    def __truediv__(self, r):
        denominator = self.denominator * r.nominator
        nominator = self.nominator * r.denominator
        return Rational(nominator, denominator)

    def __eq__(self, r):
        denominator = self.denominator * r.denominator
        nom1 = self.nominator * r.denominator
        nom2 = r.nominator * self.denominator
        return nom1 == nom2

    def __gt__(self, r):
        denominator = self.denominator * r.denominator
        nom1 = self.nominator * r.denominator
        nom2 = r.nominator * self.denominator
        return nom1 > nom2

    def __lt__(self, r):
        denominator = self.denominator * r.denominator
        nom1 = self.nominator * r.denominator
        nom2 = r.nominator * self.denominator
        return nom1 < nom2


def main():
    r1 = Rational(1, 4)
    r2 = Rational(2, 3)
    print(r1)
    print(r2)
    print(r1 * r2)
    print(r1 / r2)
    print(r1 + r2)
    print(r1 - r2)
    print(Rational(1, 2) == Rational(2, 4))
    print(Rational(1, 2) > Rational(2, 4))
    print(Rational(1, 2) < Rational(2, 4))


if __name__ == "__main__":
    main()

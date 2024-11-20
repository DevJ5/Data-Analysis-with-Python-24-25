#!/usr/bin/env python3

import math


def calculate_area(shape_input):
    if shape_input == "circle":
        radius_input = int(input("Give radius of the cirlce: "))
        area = math.pi * radius_input**2
    elif shape_input == "rectangle":
        width_input = int(input("Give width of the rectangle: "))
        height_input = int(input("Give height of the rectangle: "))
        area = width_input * height_input
    elif shape_input == "triangle":
        base_input = int(input("Give base of the triangle: "))
        height_input = int(input("Give height of the triangle: "))
        area = (base_input * height_input) / 2

    return area


def main():
    while True:
        shape_input = input("Choose a shape (triangle, rectangle, circle): ")
        if shape_input == "":
            break
        elif shape_input not in ["triangle", "rectangle", "circle"]:
            print("Unknown shape!")
        else:
            area = calculate_area(shape_input)
            print(f"The area is {area:6f}")


if __name__ == "__main__":
    main()

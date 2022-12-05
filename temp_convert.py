#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Dec 4, 2022
# A program which converts celsius to fahrenheit


def calc_fahrenheit():
    # Input
    inp_cel_str = input("Enter a number to convert (°C): ")
    try:
        # converting to a float
        inp_cel = float(inp_cel_str)
        # converts the cels to fahren
        Fah_out = (9 / 5 * inp_cel) + 32
        print(f" {inp_cel}(°C) is equal to {Fah_out}°F ")

        # for invalid inputs
    except Exception:
        print(f"{inp_cel_str} is invalid, use numbers only!")


def main():
    # calls the function, has no use here.
    calc_fahrenheit()


if __name__ == "__main__":
    main()

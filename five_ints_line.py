#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Nov. 21, 2023
# This program displays all numbers from 1000 to 2000, inclusive, and displays 5 numbers per line.


def main():
    # introduce program to user
    print("This program displays all numbers from 1000 to 2000.")
    for counter in range(1000, 2001):
        if counter == 1000:
            print(f"{counter} ", end="")
        elif counter % 5 == 0:
            print(f"\n{counter} ", end="")
        else:
            print(f"{counter} ", end="")


if __name__ == "__main__":
    main()

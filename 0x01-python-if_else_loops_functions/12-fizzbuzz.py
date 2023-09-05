#!/usr/bin/python3
def fizzbuzz():
    print("1")
    for n in range(1, 101):
        if n % 3 == 0:
            print(" Fizz", end="")
        elif n % 5 == 0:
            print(" Buzz", end="")
        elif n % 3 == 0 and n % 5 == 0:
            print(" FizzBuzz", end="")
        else:
            print(" {}".format(n), end="")
    print("\n", end="")

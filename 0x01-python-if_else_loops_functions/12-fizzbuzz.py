#!/usr/bin/python3
def fizzbuzz():
    print("1", end="")
    for n in range(2, 101):
        if n % 3 == 0 and n % 5 == 0:
            print(" FizzBuzz", end="")
        elif n % 3 == 0:
            print(" Fizz", end="")
        elif n % 5 == 0:
            print(" Buzz", end="")
        else:
            print(" {}".format(n), end="")

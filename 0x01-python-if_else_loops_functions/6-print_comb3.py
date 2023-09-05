#!/usr/bin/python3
for n in range(0, 10):
    for m in range(n + 1, 10):
        if n == m:
            continue
        elif n == 8 and m == 9:
            print("{}{}".format(n, m))
        elif n <= 8 and m <= 9:
            print("{}{}".format(n, m), end=", ")

#!/usr/bin/python3
"""this defines a module that reads stdin line by line and computes metrics"""
from sys import stdin
import signal


my_dict = {'200': 0, '301': 0, '400': 0, '401': 0,
           '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0


def SIGINT_handler(signal, frame):
    """ handles signal interrupt """
    print_dict()
    exit(0)


signal.signal(signal.SIGINT, SIGINT_handler)


def print_dict():
    """ prints the statistics """
    global total_size, my_dict
    print("File size: {}".format(total_size))
    for key in my_dict:
        if my_dict[key] > 0:
            print("{}: {}".format(key, my_dict[key]))
            my_dict[key] = 0


def main():
    """ gets input from input stream """
    global total_size, my_dict
    line_count = 0
    try:
        while True:
            if not stdin.isatty():
                for line in stdin:
                    my_list = line.split()
                    if str(my_list[-2]) in my_dict:
                        key = str(my_list[-2])
                        my_dict[key] = my_dict[key] + 1
                    line_count = line_count + 1
                    total_size = total_size + int(my_list[-1])
                    if line_count == 10:
                        print_dict()
                        line_count = 0
    except KeyboardInterrupt:
        print("Input termination by CTRL-C")


if __name__ == "__main__":
    main()

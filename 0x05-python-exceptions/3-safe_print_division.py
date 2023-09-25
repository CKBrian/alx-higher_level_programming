#!/usr/bin/python3
def safe_print_division(a, b):
    quotient = None
    try:
        quotient = a / b
    except (ZeroDivisionError, TypeError):
        return None
    finally:
        print("Inside result: {}".format(quotient))
        return quotient

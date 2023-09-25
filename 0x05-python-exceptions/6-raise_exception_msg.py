#!/usr/bin/python3
def raise_exception_msg(message=""):
    class custom_msg(Exception):
        def __init__(self, msg):
            super().__init__(msg)
    raise custom_msg(message)

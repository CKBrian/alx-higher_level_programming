#!/usr/bin/python3

def text_indentation(text):
    """
        prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        if char == '?' or char == '.' or char == ',':
            print("{}\n\n".format(char),end="")
        else:
            print("{}".format(char), end="")
    print("\n\n",end="")

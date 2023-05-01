#!/usr/bin/python3
""" define a function """


def text_indentation(text):
    """ prints lines of text inserting newlines after ., ? and : """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    add_newline = False
    for char in text:
        if add_newline:
            result += "\n\n"
            add_newline = False
        if char == " " and not add_newline and (result == ""
                                                or result[-1] == "\n"):
            continue
        result += char
        if char in ".?:":
            add_newline = True
    if add_newline:
        result += "\n\n"
    print(result.rstrip())

#!/usr/bin/python3
'''
This function prints a text
with 2 new lines after of
'.', '?' and ':'
'''


def text_indentation(text):
    '''
    text must be a string
    '''
    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = False
    for i in range(len(text)):
        if (text[i] == ' ' and text[i - 1] == '.' or
                text[i - 1] == '?' or text[i - 1] == ':'):
            if flag is True:
                pass
            else:
                print(text[i], end="")
        else:
            print(text[i], end="")
            flag = True
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print("\n")

"""
Regex Version of the strip() Method
Write a function that takes a string and does the same thing as the strip() string method. 
If no other arguments are passed other than the string to strip, 
then whitespace characters will be removed from the beginning and end of the string. 
Otherwise, the characters specified in the second argument to the function will be removed from the string.
"""

import re

def stripper(string, char=' '):
    stringRegex = re.compile(char, re.I)
    convert = stringRegex.sub('', string)
    print(convert)

    
message = input('Enter a string \n')
c = input('Enter the character that you want to remove!\nIf nothing\
 is entered, space will be removed\n')

if c != '':
    stripper(message, c)
else:
    stripper(message)
#! python3
# Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import sys,pyperclip
text = pyperclip.paste()

#Separate lines and add stars.
lines = text.split('\n')    #splits all the lines
for i in range(len(lines)):      # loop through all indexes for "lines" list
    lines[i] = '* ' + lines[i]    # add star to each string in "lines" list
text = '\n'.join(lines)     # joining all the line and making a multi line string
sys.stdout.write(text)       # to display the output at the terminal
pyperclip.copy(text)      #changing the text of the clipboard

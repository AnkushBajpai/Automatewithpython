"""
Let’s use PyInputPlus to create a simple program that does the following:

Ask the user if they’d like to know how to keep an idiot busy for hours.
If the user answers no, quit.
If the user answers yes, go to Step 1.

Of course, we don’t know if the user will enter something besides “yes” or “no,” so we need to perform input validation.
It would also be convenient for the user to be able to enter “y” or “n” instead of the full words.
PyInputPlus’s inputYesNo() function will handle this for us and,
no matter what case the user enters,
return a lowercase 'yes' or 'no' string value.

"""


import pyinputplus as pyip

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break

print('Thank you. Have a nice day.')
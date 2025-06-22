# here we ar3e writing a Fn. which will check if the digit sum of the enetered number adds up to 10 or not
# if the sum doesn't adds up to 10, the fn. will throw an exception
# if the sum is 10, then the fn. will return the integer form of numbers enetered

import pyinputplus as pyip

def addUpToTen(numbers):
    numbersList = list(numbers)
    for i,digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception(f'The digits are not adding up to 10, their sum is {sum(numbersList)}')
    return int(numbers)        # returns an int for of numbers

response = pyip.inputCustom(addUpToTen)
print(f'{response} is of type {type(response)}')
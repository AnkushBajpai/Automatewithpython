import sys

def colatz():
    print(' Enter number: ')
    try:
        number = int(input())
    except ValueError:
        print('you must enter an integer.')
        number = int(input())
    while number!=1:
        if number%2 == 0:
            print(number//2)
            number=number//2
        elif number%2 == 1:
            print(3*number+1)
            number=3*number+1

colatz()

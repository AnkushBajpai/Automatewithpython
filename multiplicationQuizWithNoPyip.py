import random, time

correctAwnsers = 0
numberOfQuestions = 10

#loop for asking 10 questions
for questionNumber in range(1, numberOfQuestions+1):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    retryLimit = 3
    start = time.time()
    localNum1 = num1
    localNum2 = num2
    # As user can retry for at least 3 times
    while retryLimit > 0:
        awnser = input(f'\n Question number {questionNumber}: {localNum1} * {localNum2}\n')
        # condition to check if integer is entered
        while awnser.isdigit() == False:
            awnser = input(f'\n {awnser} is not valid, enter an integer\n')

        if int(awnser) == num1*num2:
            end = time.time()
            if end-start > 8:
                print(f'\nYou took too long to awnser, we consedered your awnser as INCORRECT!\n')
            else:
                print(f"\n {awnser} is the correct Awnser!")
                correctAwnsers += 1
            break
        elif int(awnser) != num1*num2:
            print(f'\n{awnser} is not the correct awnser, please retry, mentioning the question again below.\n')
            retryLimit -= 1
            if retryLimit == 0:
                print(f'\nYou have met enough reties, we are marking your awnser as INCORRECT!\n')
                break
    
print(f'\nYou have awnswered total {correctAwnsers} correct awnsers, congratulations')



"""
run results mentioned below
-----------------------------------------------

 Question number 0: 0 * 6
0

 0 is the correct Awnser!

 Question number 1: 0 * 9
0

 0 is the correct Awnser!

 Question number 2: 7 * 9
5

5 is not the correct awnser, please retry, mentioning the question again below.


 Question number 2: 7 * 9
3

3 is not the correct awnser, please retry, mentioning the question again below.


 Question number 2: 7 * 9
3

3 is not the correct awnser, please retry, mentioning the question again below.


You have met enough reties, we are marking your awnser as INCORRECT!


 Question number 3: 9 * 5
45

 45 is the correct Awnser!

 Question number 4: 0 * 0
0

You took too long to awnser, we consedered your awnser as INCORRECT!


 Question number 5: 6 * 8
48

 48 is the correct Awnser!

 Question number 6: 7 * 8
56

 56 is the correct Awnser!

 Question number 7: 1 * 7
7

 7 is the correct Awnser!

 Question number 8: 4 * 6
24

 24 is the correct Awnser!

 Question number 9: 1 * 8
8

 8 is the correct Awnser!
You have awnswered total 8 awnsers, congratulations
"""
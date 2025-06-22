#comma Code
def commaCode(inputList):
    try:
        a = ''
        for i in range(len(inputList)-1):
            a += str(inputList[i]) + ', '
        a += str('and ' + inputList[len(inputList)-1])
        print (a)
    except IndexError:
        print("List enetered should not be empty")

spam = ['apples', 'bananas', 'tofu', 'cats']
commaCode(spam)

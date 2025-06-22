#this program says hello and asks for my name
import sys
print('what is your name')  # to ask for their name
myName=input()
print('It is good to meet you '+myName)
print('The length of your name is: ')
print(len(myName))
print('what is your age? ')   #ask for their age
myAge=input()
print('you will be '+str(int(myAge)+1)+' in an year!')
sys.exit()

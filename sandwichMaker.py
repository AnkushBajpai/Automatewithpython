"""
Write a program that asks users for their sandwich preferences. The program should use PyInputPlus to ensure that they enter valid input, such as:

Using inputMenu() for a bread type: wheat, white, or sourdough.
Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
Using inputYesNo() to ask if they want cheese.
If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.

Come up with prices for each of these options, and have your program display a total cost after the user enters their selection.
"""

import pyinputplus as pyip

breadType =  {'wheat': 10 , 'white': 20 , 'sourdough': 30}
proteinType = {'chicken':10 , 'turkey':20 , 'ham':30 , 'tofu':40}
cheeseType = {'cheddar':10 , 'Swiss':20 , 'mozzarella':30}
addOns = {'mayo':10 , 'mustard':10 , 'lettuce':10 , 'tomato':10}

totalPrice = 0

breadChoice = pyip.inputMenu(list(breadType.keys()),prompt='What should be the bread type: \n', default= 'wheat', numbered= True)
print()
totalPrice += breadType[breadChoice]

proteanChoice = pyip.inputMenu(list(proteinType.keys()),prompt='What will you choose for the source of protean: \n', default= 'tofu', numbered= True)
print()
totalPrice += proteinType[proteanChoice]

cheeseYesOrNo = pyip.inputYesNo(prompt='Would you like to have some cheese in your Sandwich?')
print()
if cheeseYesOrNo.lower() == 'yes':
    chesseChoice = pyip.inputMenu(list(cheeseType.keys()),prompt='Please let us know which cheese type would you prefer \n', default= 'cheddar', numbered= True)
    print()
    totalPrice += cheeseType[chesseChoice]

addOnsYesOrNo = pyip.inputYesNo(prompt='Would you like to have any addOns in your Sandwich?')
print()
totalPriceAddOns = 0
while True:
    if addOnsYesOrNo.lower() == 'yes':
        addOnsChoice = pyip.inputMenu(list(addOns.keys()),prompt='What should be the addOn for your Sandwich: \n', default= 'mayo', numbered= True)
        print()
        totalPriceAddOns += addOns[addOnsChoice]
        
        # the below statment only executes if the user has chosen to get add-ons initially, else not.
        moreAddOns = pyip.inputYesNo('Do you like to have more add ons for your sandwich')
        print()
        if moreAddOns.lower() == 'no':
            break
    break
sandwichCount = pyip.inputInt('How many sandwiches would you like to have? ', min=1)
print()
totalPrice += totalPriceAddOns 
totalPrice *= sandwichCount

print(f'Your billing amounbt is {totalPrice}.')


"""
run results mentioned below
-----------------------------------------------
What should be the bread type: 
1. wheat
2. white
3. sourdough
1

What will you choose for the source of protean:
1. chicken
2. turkey
3. ham
4. tofu
1

Would you like to have some cheese in your Sandwich?1  
'1' is not a valid yes/no response.
Would you like to have some cheese in your Sandwich?yes

Please let us know which cheese type would you prefer
1. cheddar
2. Swiss
3. mozzarella
1

Would you like to have any addOns in your Sandwich?yes

What should be the addOn for your Sandwich:
1. mayo
2. mustard
3. lettuce
4. tomato
1

Do you like to have more add ons for your sandwichno

How many sandwiches would you like to have? 3

Your billing amounbt is 120.
"""
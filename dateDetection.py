"""Write a regular expression that can detect dates in the DD/MM/YYYY for-
mat. Assume that the days range from 01 to 31, the months range from 01 
to 12, and the years range from 1000 to 2999. Note that if the day or month 
is a single digit, it’ll have a leading zero.
The regular expression doesn’t have to detect correct days for each 
month or for leap years; it will accept nonexistent dates like 31/02/2020 or 
31/04/2021. Then store these strings into variables named month, day, and 
year, and write additional code that can detect if it is a valid date. April, 
June, September, and November have 30 days, February has 28 days, and 
the rest of the months have 31 days. February has 29 days in leap years. 
Leap years are every year evenly divisible by 4, except for years evenly divisi-
ble by 100, unless the year is also evenly divisible by 400. Note how this 
calculation makes it impossible to make a reasonably sized regular expression 
that can detect a valid date.
1/01/2020 29/02/2020 01/3/2020 29/02/2019 29/02/2000 31/09/2000 29/02/2600
"""
import re, pyperclip

dateRegex = re.compile(r'''(
    (3[0-1]|[1-2][0-9]|0?[1-9])       # day from 1-31 or 01-31
    [/,._:]                         # separator
    ([1][0-2]|0?[1-9])              # month from 1-12 or 01-12
    [/,._:]                         # separator
    ([1-2]\d{3})                     # year from 1000-2999
    )''', re.VERBOSE)               # https://www.debuggex.com/

text = str(pyperclip.paste())
monthsWitch30Days = ['04', '06', '09', '11']
date19 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
matches= []

for dayMonthYear in dateRegex.findall(text):
    valid = True
    
    # store strings into dict keys: day month year
    date = {'day':1, 'month':2, 'year':3}
    for k, v in date.items():
        date[k] = dayMonthYear[v]
    
    # append leading zero if the day or month is a single digit
    if date['day'] in date19:
        date['day'] = '0' + date['day']
    if date['month'] in date19:
        date['month'] = '0' + date['month']

    # detect correct days for each month or for leap years
    if date['day'] in ['29', '30', '31']:
        if date['day'] == '29' and date['month'] == '02':
            if (int(date['year']) % 4 == 0 and \
                int(date['year']) % 100 != 0) or \
                (int(date['year']) % 400 == 0 and \
                 int(date['year']) % 100 != 0):
                valid = True
            else:
                valid = False
        if date['day'] == '30' and date['month'] != '02':
            if date['month'] in monthsWitch30Days:
                valid = True
            else:
                valid = False
        if date['day'] == '31' and date['month'] != '02':
            if date['month'] not in monthsWitch30Days:
                valid = True
            else:
                valid = False       
    
    if valid:
        matches.append(date)

print(matches)
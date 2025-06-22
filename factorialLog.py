"""
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')
"""

import logging
#filename='myProgramLog.txt',    --- can be added for getting the logs added tro a file
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

# the below statement is to diable the logging
logging.disable(logging.DEBUG)

def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))

    logging.debug('End of factorial(%s%%)' % (n))
    return total

print(f'Factorial ==  {factorial(5)}')
logging.debug('End of program')


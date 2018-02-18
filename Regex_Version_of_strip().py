#! python3
# StripLikeFn.py

"""
Regex_Version_of_strip()
Write a function that takes a string and does the same thing as the strip() string method.
If no other arguments are passed other than the string to strip, then whitespace characters
will be removed from the beginning and end of the string. Otherwise, the characters
specified in the second argument to the function will be removed from the string.
"""

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -%(levelname)s -:%(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start the program')


def FirstChar(string, separator=' '):
    # Finds the First Significant character
    logging.debug('FirstChar with separator(%s)' % separator)
    for fc in range(len(string)):
        logging.debug("i is " + str(fc))
        if string[fc] != separator:
            return fc
    return 0


def LastChar(string, separator=' '):
    # Finds the Last Significant character
    logging.debug('LastChar with separator(%s)' % separator)
    for lc in range((len(string) - 1), -1, -1):
        logging.debug("i is " + str(lc))
        if string[lc] != separator:
            return lc
    return len(string)


def strip(string, separator=' '):
    logging.debug('The string is "' + string + '" and separator is "' + separator + '":')
    logging.debug('The length of the string is ' + str(len(string)))
    print('The Stripped string is:' + string[FirstChar(string, separator):(LastChar(string, separator)+1)])


take = input('Enter the string to strip:')
strip(take)
print('This was one parameter fn')
take = input('Enter the string to strip:')
sep = input('Enter the separator:')
strip(take, sep)
print('This was two parameter fn')
logging.debug('End of the program')

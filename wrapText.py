#! python3
"""
-->Takes text from clipboard
-->Wraps text to approx 50 characters per line
    accoording to
-->Paste the formatted text to clipboard
"""

import pyperclip
import os


def wrap(List):
    # Return an index of the list upto which the length of the characters is 50.
    finalList = []
    start = 0
    end = len(List)
    while len(List) >= end >= start:
        if len(' '.join(List[start:end])) < 110:
            finalList.append(' '.join(List[start:(end+1)]))
            start = end+1
            end = len(List)
        else:
            end -= 1
    return finalList


toWrap = pyperclip.paste()
newString = os.linesep.join(wrap(toWrap.split(' ')))
pyperclip.copy(newString)
'''
import pypercliprt os
import pprint
import logging
impo

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s-%(levelname)s-%(message)s')


logging.disable(logging.CRITICAL)


def wrap(List):
    # Return an index of the list upto which the length of the characters is 50.
    logging.debug('Function call')
    finalList = []
    start = 0
    end = len(List) - 1
    logging.debug('start is ' + str(start))
    logging.debug('end is ' + str(end))
    while len(List) >= end >= start:
        logging.debug('Inside loop')
        if len(' '.join(List[start:end])) < 110:
            logging.debug('Inside If clause')
            logging.debug('start is ' + str(start))
            logging.debug('end is ' + str(end))
            finalList.append(' '.join(List[start:end]))
            start = end + 1
            end = len(List) - 1
            logging.debug('start and end are modified')
            logging.debug('start is ' + str(start))
            logging.debug('end is ' + str(end))
        else:
            logging.debug('Inside else clause')
            logging.debug('end is ' + str(end))
            end -= 1
            logging.debug('end is modified to ' + str(end))
        logging.debug(pprint.pformat(finalList))
    return finalList


logging.debug('Start of the program')
toWrap = pyperclip.paste()
logging.debug(toWrap)
newString = os.linesep.join(wrap(toWrap.split(' ')))
pyperclip.copy(newString)
logging.debug(newString)
logging.debug('End of the progeam')
'''
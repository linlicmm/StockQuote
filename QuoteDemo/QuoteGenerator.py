__author__ = 'lilin'

import time
import Quote


def re_exe(intv=60):
    while True:
        Quote.generateQuotes('Quote.csv', 'Quote.csv', intv)
        Quote.printQuotes('Quote.csv')
        time.sleep(intv)

Quote.initializeQuotes('Quote.csv')
re_exe(0.1)
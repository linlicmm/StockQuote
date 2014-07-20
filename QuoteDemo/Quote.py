__author__ = 'lilin'

import csv
import random
import os

def printQuotes(inputFilePath):
    os.system('clear')
    print 'stock id'.center(10), 'stock name'.center(10), 'price'.center(10), 'variation'.center(10), 'volume'.center(10)
    with open(inputFilePath, 'rb') as quoteFile:
        rows = csv.reader(quoteFile)
        for row in rows:
            print row[0].center(10), row[1].center(10), row[2].center(10), (row[6] + "%").center(10), row[7].center(10)


def initializeQuotes(inputFilePath):
    with open(inputFilePath, 'wb') as quoteFile:
        row = csv.writer(quoteFile, delimiter=',')
        row.writerow([0, 'Stock A', 5, 5, 0.8, 0.8, 0, 0])
        row.writerow([1, 'Stock B', 5, 5, 0.8, 0.8, 0, 0])
        row.writerow([2, 'Stock C', 5, 5, 0.8, 0.8, 0, 0])
        row.writerow([3, 'Stock D', 5, 5, 0.8, 0.8, 0, 0])
        row.writerow([4, 'Stock E', 5, 5, 0.8, 0.8, 0, 0])
        row.writerow([5, 'Stock F', 5, 5, 0.4, 0.4, 0, 0])
        row.writerow([6, 'Stock G', 5, 5, 0.4, 0.4, 0, 0])
        row.writerow([7, 'Stock H', 5, 5, 0.4, 0.4, 0, 0])
        row.writerow([8, 'Stock I', 5, 5, 0.4, 0.4, 0, 0])
        row.writerow([9, 'Stock J', 5, 5, 0.4, 0.4, 0, 0])

def generateQuotes(inputFilePath, outputFilePath, intv):
    quotes_list = []

    # Read all data from the csv file.
    with open(inputFilePath, 'rb') as csvInputFile:
        quotes = csv.reader(csvInputFile)
        quotes_list.extend(quotes)


    # Write data to the csv file and replace the lines in the line_to_override dict.
    with open(outputFilePath, 'wb') as csvOutputFile:
        writer = csv.writer(csvOutputFile)
        for row in quotes_list:
            if float(row[5]) <= 0:
                price = float(row[2])
                delta = (1 + (random.random() - 0.5) * 0.05)
                row[2] = str(round(price * delta, 2))
                row[6] = str((float(row[2]) - float(row[3])) * 100/ float(row[3]))
                row[7] = str((int(row[7]) + int(random.random() * 100)))
                #sellDelta = (1 + (random.random() - 0.5) * 0.01)
                #row[3] = str(round(buyPrice * sellDelta, 2))
                row[5] = row[4]
            else:
                row[5] = str(float(row[5]) - intv)
            writer.writerow(row)
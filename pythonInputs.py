#! python3
# Read data from a CSV file as input for your Python programs.
import csv
fileObj=open('pythonInputs.csv')
csvReader=csv.reader(fileObj)
Inputs=list(csvReader)
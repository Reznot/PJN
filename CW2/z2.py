import re
import os

# cwd = os.getcwd()
# print(cwd)


def isCSVFileValid(obj):
    if obj is None:
        print("This file is not valid.")
        exit(1)
    else:
        print("This file is valid")
        exit(0)


filename = input("Enter name of the file to validate")
file = open(filename, 'r')

for line in file:
    isMatchingObj = re.match(r'.*;\d*;\d*', line)
    isCSVFileValid(isMatchingObj)
file.close()



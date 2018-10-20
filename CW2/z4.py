import re

in_filename = input("Enter the name of a file (with file extension) you want to scan for email adressess: ")
out_file = open("Emails.txt", 'a+')

with open(in_filename) as in_file:   #alternative to in_file = open(filename, 'r')
    for line in in_file:
        isMatchingObj = re.search(r"\w+@(\w+\.)*\w+", line)
        if isMatchingObj is not None:
            out_file.write(str(isMatchingObj.group()) + '\n')
print("File with emails has been created")
in_file.close()

out_file.close()






#notes
#str() converts obj to string
#findall retuns list of matches in string
import re


with open('file2.csv') as in_file:
    reader = csv.reader(in_file)
    for line in in_file:
        CSVstring = re.search(r'.-\d-\d*$', line)


line_Check = re.match(r'', string1)


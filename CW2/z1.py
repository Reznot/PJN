import re

name = input('Podaj imie ')

name_Check = re.match(r'[A-Z][a-z]+',name)
if name_Check:
    print(name_Check.group())
else:
    print('Blad')
    exit(1)


surname = input('Podaj nazwisko ')
check_Surname = re.match(r'[A-Z][a-z]+',surname)

if check_Surname is None:
    print('Blad')
    exit(1)


city = input('Podaj miasto ')
check_City = re.match(r'[A-Z][a-z]+',city)

if check_City is None:
    print('Blad')
    exit(1)

phone = input('Podaj numer tel')
check_phone = re.match(r'\(\d\d\) \d\d\d-\d\d-\d\d$', phone)
if check_phone is None:
    print('Blad')
    exit(1)


postcode = input('Podaj kod pocztowy')
check_Postcode = re.match(r'\d\d-\d\d\d$',postcode)
if check_Postcode is None:
    print('Blad')
    exit(1)
s
#moge napisywac matchingObj

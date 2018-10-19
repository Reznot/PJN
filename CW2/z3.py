import re

explicitfilename = input("Enter the name of a file to be censored: ")
censoredfilename = (explicitfilename.split("."))[0] + "CENSORED." + (explicitfilename.split("."))[1]

explicit = open(explicitfilename, 'r')
censored = open(censoredfilename, 'w+')

for line in explicit:
    censored.write(re.sub(r'\w*[Kk]urw\w*|\w*[Jj]eb\w*|\w*[Pp]ierdol\w*|\w*[Cc]huj\w*|^[Cc]ip\w*|[Pp]izd\w*', '---', line))


print("Text has been censored")
explicit.close()
censored.close()

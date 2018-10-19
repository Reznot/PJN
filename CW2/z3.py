import re

dirtyfilename = input("Type the filename to clean (f.e. file.txt)")
cleanfilename = (dirtyfilename.split("."))[0]+"CLEAN."+(dirtyfilename.split("."))[1]

dirty = open(dirtyfilename, 'r+')
clean = open(cleanfilename, 'w+')

for line in dirty:
    clean.write(re.sub(r'\w*[Kk]urw\w*|\b[Cc]huj\w*|^[Cc]ip\w*|[Pp]izd\w*|\w*[Jj]eb\w*|\w*[Pp]ierdol\w*', '---', line))

print("Censored file saved in "+ cleanfilename)
dirty.close()
clean.close()

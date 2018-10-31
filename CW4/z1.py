import re
import urllib.request


grinders = []
sources = ['https://www.ceneo.pl/Narzedzia_i_warsztat;szukaj-szlifierka+k%C4%85towa', 'https://www.ceneo.pl/Narzedzia_i_warsztat;szukaj-szlifierka+k%C4%85towa;0020-30-0-0-1.htm',
           'https://www.ceneo.pl/Narzedzia_i_warsztat;szukaj-szlifierka+k%C4%85towa;0020-30-0-0-2.htm', 'https://www.ceneo.pl/Narzedzia_i_warsztat;szukaj-szlifierka+k%C4%85towa;0020-30-0-0-3.htm',
           'https://www.ceneo.pl/Narzedzia_i_warsztat;szukaj-szlifierka+k%C4%85towa;0020-30-0-0-4.htm']

for i in range(len(sources)):
    response = urllib.request.urlopen(sources[i])
    page_source = response.read()
    grinders += re.findall(r'data-source-tag="">([A-Za-z0-9 ]+)</a>', str(page_source))

grinders_list = list(set(grinders))

for i in range(len(grinders_list)):
    print("{}: {}".format(i + 1, grinders_list[i]))
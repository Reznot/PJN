from bs4 import BeautifulSoup
import urllib.request
import re


polish_sources = ['http://rjawor.home.amu.edu.pl/index.php', 'http://rjawor.home.amu.edu.pl/science.php', 'http://rjawor.home.amu.edu.pl/relax.php',
                  'http://rjawor.home.amu.edu.pl/contact.php']
english_sources = ['http://rjawor.home.amu.edu.pl/index_en.php', 'http://rjawor.home.amu.edu.pl/science_en.php', 'http://rjawor.home.amu.edu.pl/relax_en.php',
                   'http://rjawor.home.amu.edu.pl/contact_en.php']

pl_ver = open('rjawor_pl.txt', 'w+')
en_ver = open('rjawor_en.txt', 'w+')


def download_src(source):
    page_source = ''
    for i in range(len(source)):
        print(source[i])
        response = urllib.request.urlopen(source[i])
        soup = BeautifulSoup(response, "html.parser")
        page_source = page_source + re.sub(r'\s{2,}', ' ', (soup.get_text()).replace('\n', ' '))
    return page_source


pl_text = download_src(polish_sources)
pl_ver.write(pl_text)

en_text = download_src(english_sources)
en_ver.write(en_text)

pl_ver.close()
en_ver.close()
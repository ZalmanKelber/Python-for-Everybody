from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

orig_url = input('Enter url: ')
SEQ_LEN = 7
url = orig_url
name = None

for i in range(SEQ_LEN):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    link = soup('a')[17]
    name = link.contents[0]
    url = link.get('href', None)
    print(name)

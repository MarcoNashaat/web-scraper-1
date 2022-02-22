#enabling https
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#importing libraries
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

#function to fetch page title
def get_title(url):
    try:
        html = urlopen(url)
    #handling http errors
    except HTTPError:
        return None
    try:
        bs = BeautifulSoup(html,'html.parser')
        title = bs.h1
    #handling attribute errors and possible url errors
    except AttributeError:
        return None
    return title

title = get_title('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('title not found')
else:
    print(title)


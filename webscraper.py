import urllib
import ssl
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = 'https://www.gic.com.sg/news-and-resources/pgim-and-gic-help-cios-build-balanced-portfolios-when-investing-in-illiquid-private-assets/'

#connect to website
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

#print header
page_soup = soup(page_html,'html.parser')
print(page_soup.h1.text)
print(page_soup.p)
#test
print('test')

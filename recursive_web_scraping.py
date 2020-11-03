#!/usr/bin/env python3
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import ssl
import re


#pos = 3
#repeat = 4

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#url =  'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
#url = ' http://py4e-data.dr-chuck.net/known_by_Inka.html'
repeat = input("Enter count: ")
pos = input("Enter Position: ")



def get_soup_from_url(url):
    print('Retrieving: ', url)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req, context=ctx).read()
    hot_soup = BeautifulSoup(html, "html.parser")
    return hot_soup

soup = get_soup_from_url(url)

count = 0
last_name = ""
while count < repeat:
    tags = soup('a')
    i = 0
    for tag in tags:
        i += 1
        last_name = tag.get('href', None)
        if (i == pos):  # get the third name
            soup = get_soup_from_url(tag.get('href', None))
            #print('Retrieving: ',str(i) +' '+ tag.get('href', None))
            break
    count += 1

#print(last_name)
#extract = re.findall('known_by_(.*).html', last_name)
#print("Name: ",extract[0])
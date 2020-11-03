#!/usr/bin/env python3
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#url =  'http://py4e-data.dr-chuck.net/comments_42.html'
#url = 'http://py4e-data.dr-chuck.net/comments_1038962.html'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup.find_all('span')
total = 0
count = 0
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('comments: ', tag.text)
    total +=  int(tag.text)
    count += 1
    #print('span', tag.get('')
print("Count", count)
print("Total", total)
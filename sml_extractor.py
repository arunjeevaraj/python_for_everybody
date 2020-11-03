#!/usr/bin/env python3
from urllib.request import urlopen, Request
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import ssl
import re


print("XML EXTRACTOR 0.1")

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location : ')
#url =  'http://py4e-data.dr-chuck.net/comments_42.xml'
#url =  'http://py4e-data.dr-chuck.net/comments_1038964.xml'

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
print('Retrieving ', url)
xml_string = urlopen(req, context=ctx).read()
print("Retrieved " + str(len(xml_string)) + " characters") 
#print("going to print the url data")
#print(html)

tree = ET.fromstring(xml_string)
list_of_comments = tree.findall('comments/comment')
total = 0
count = 0
for comment in list_of_comments:
    total += int(comment.find('count').text)
    count += 1
print("count ", count)
print("sum ", total)
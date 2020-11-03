#!/usr/bin/env python3
from urllib.request import urlopen, Request
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import ssl
import re
import json

print("JSON EXTRACTOR 0.1")

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = 'http://py4e-data.dr-chuck.net/comments_1038965.json'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
print('Retrieving ', url)
json_string = urlopen(req, context=ctx).read()

info = json.loads(json_string)

#print(info['comments'])
total = 0
for it in info['comments']:
    total += int(it['count'])

print(total)
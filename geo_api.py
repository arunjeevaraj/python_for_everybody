#!/usr/bin/env python3
from urllib.request import urlopen, Request
import xml.etree.ElementTree as ET
import urllib.parse
from bs4 import BeautifulSoup
import ssl
import re
import json
import sys

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = 'NYU'

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

params = dict()
params['address'] = address
params['key'] = api_key

url = serviceurl + urllib.parse.urlencode(params)


req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
print('Retrieving ', url)
json_string = urlopen(req, context=ctx).read().decode()
try:
    info = json.loads(json_string)
    print(info['results'][0]['place_id'])
except:
    print('Json format downloaded is not supported')
    info = None


if not info or 'status' not in info or info['status']!= 'OK':
    print("Failure to retreive, status is not ok")
    print(json_string)
    sys.exit(1)
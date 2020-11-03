#!/usr/bin/env python3
# this tells the os how the script is run, and who runs it.

import re



text = "http://py4e-data.dr-chuck.net/known_by_Anayah.html"
extract = re.findall('known_by_(.*).html', text)
print("Name: ",extract[0])
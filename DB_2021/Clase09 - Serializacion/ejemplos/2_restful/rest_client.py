#!/usr/bin/env python
import requests
import urllib.parse
from pprint import pprint

URL = 'http://localhost:4000/artists/'

r = requests.get(URL)

print(r.status_code)
pprint(r.json())
print(type(r.json()))

"""while(True):
    name = input('--> ').replace('/', '|')
    if name == '':
        break
    r = requests.get(urllib.parse.urljoin(URL, urllib.parse.quote(name, safe='')))
    print(r.status_code)
    if (r.status_code == 200):
        pprint(r.json())
        print(type(r.json()))
    else:
        print(r.text)"""
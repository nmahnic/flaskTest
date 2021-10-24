#!/usr/bin/env python
import requests
import urllib.parse
from pprint import pprint

URL = 'http://localhost:5000/user/'

r = requests.get(URL)

print(r.status_code)
pprint(r.json())
print(type(r.json()))

URL = 'http://localhost:5000/dum/'

r = requests.get(URL)

print(r.status_code)
pprint(r.json())
print(type(r.json()))

#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
files = os.listdir("./supplier-data/images/")

for x in files:
    if x.endswith('jpeg'):
        
        with open("./supplier-data/images/"+x, 'rb') as opened:
            r = requests.post(url, files={'file': opened})

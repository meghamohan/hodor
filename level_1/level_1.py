#!/usr/bin/python
import requests

URL = 'http://54.221.6.249/level1.php/cookies'
headers = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
payload = {'id': '128', 'holdthedoor': 'submit', 'key': '0'}

cookies = {'HoldTheDoor' : '0'}
r = requests.get(URL, cookies=cookies)
jar = requests.cookies.RequestsCookieJar()

r.cookies['HoldTheDoor']

for i in range (2):
    r = requests.post(URL, data=payload)

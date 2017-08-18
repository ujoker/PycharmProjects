# -*-coding:utf-8-*-

import requests

req = requests.session()
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}
cookies = {'jydms': '3ccd3d4d-5b59-466c-86fa-0dec85d7ebfa'}
url = "http://dms.gene.ac/portal"
resp = req.get(url, cookies=cookies, headers=headers)
print resp, 'aaa'
print resp.text, 'bbb'

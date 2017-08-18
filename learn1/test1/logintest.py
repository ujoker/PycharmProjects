import requests
import re

req = requests.session()
url = "https://gene.ac/login"
resp = req.get(url)
print resp, 'aaa'
content = resp.text
print content, 'bbb'
csrf_token = re.findall('<input id="csrf_token" name="csrf_token" type="hidden" value="([#\\w]+)">', content)[0]
print(csrf_token)
resp = req.post(url, data={"account": "hl_test", "passwd": "gene.ac", "csrf_token": csrf_token})
print resp.text, 'ccc'

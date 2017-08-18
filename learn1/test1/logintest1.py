# -*-coding:utf-8-*-

import urllib
import urllib2


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}
values = {'user_name': 'hl_test', 'password': 'gene.ac'}
data = urllib.urlencode(values)
url = "http://dms.gene.ac/login"
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
print response.read()

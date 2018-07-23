import urllib.request
#f = urllib.request.urlopen('https://ya.ru')
#print (f.read())

import requests
resp = requests.get('https://www.yandex.ru')
print (resp.status_code)
print (resp.encoding)
cookies = resp.cookies.items()
for x in cookies:
    print(x)
print (resp.elapsed)
print (resp.history)
print (resp.reason)
print (resp.request)
print (resp.url)
#print (resp.headers)
#print (resp.text)
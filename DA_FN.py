import requests

url = 'https://www.github.com'
r = requests.get(url)
print('Status code:', r.status_code)
print(r)
print(r.ok)
print(r.headers)
headers = {'User-Agent': 'Mobile'}
r3 = requests.get(url, headers = headers)
print(r3.text)




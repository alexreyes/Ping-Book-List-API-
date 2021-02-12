import requests

url2021 = 'https://book-list-api-v2.alex243.repl.co/?year=2021'

x = requests.post(url2021)
print(x.text)
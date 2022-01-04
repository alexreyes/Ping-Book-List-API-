import requests

url2021books = 'https://book-list-api-v2.alex243.repl.co/?year=2022'

x = requests.post(url2021books)
print(x.text)

# cryptoPrices = 'https://priceData.alex243.repl.co'

# y = requests.post(cryptoPrices)
# print(y.text)

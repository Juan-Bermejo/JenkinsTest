import requests

url = 'https://api.chuknorris.io/jokes/random'

r = requests.get(url, verify=False)
data = r.json()
print(data['value'])
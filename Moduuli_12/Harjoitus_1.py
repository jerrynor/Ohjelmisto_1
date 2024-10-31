import requests

url = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(url)
    response_body = response.json()
    print(response_body['value'])
except requests.exceptions.ConnectionError:
    print("Verkko-ongelma.")


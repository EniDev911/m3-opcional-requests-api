import requests # pip install requests

endpoint = "https://reqres.in/api/users"
respuesta = requests.get(endpoint)

users_data = respuesta.json()['data']
print(*users_data, sep="\n")
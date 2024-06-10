import requests

endpoint = "https://reqres.in/api/users"
respuesta = requests.get(endpoint)

users_data = respuesta.json()['data']

for user in users_data:
    if user['first_name'] == 'Tracey':
        deleted_user = requests.delete(f"{endpoint}/{user['id']}")
        print(deleted_user.status_code)
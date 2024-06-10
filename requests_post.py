import requests

endpoint = "https://reqres.in/api/users"

nuevo_usuario = {
	"name": "ignacio",
	"job": "profesor"
}

respuesta = requests.post(endpoint, nuevo_usuario)

created_user = respuesta.json()
print(created_user)
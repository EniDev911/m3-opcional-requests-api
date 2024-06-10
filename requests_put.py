import requests

endpoint = "https://reqres.in/api/users/2"

usuario_actualizado = {
	"name": "morpheus",
	"residence": "zion"
}

respuesta = requests.put(endpoint, usuario_actualizado)

updated_user = respuesta.json()
print(updated_user)
<a href="https://colab.research.google.com/gist/EniDev911/07d0c42cafc339da4ddafedf49bbbf86/estructuras-de-datos-y-funciones-uso-de-api.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## Descripción

Se tiene una API que contiene cierta información personal de clientes. Esta API está siendo testeada porque otro equipo de desarrolladores quiere integrarla en una aplicación que utiliza información personal de personas.

- Para este desafío, se debe usar la API de pruebas de reqres, disponible en [https://reqres.in/](https://reqres.in/){: target='_blank'}.
- Esta API no requiere autenticación, y su unico recurso es users.
- Todas las solicitudes se hacen a [https://reqres.in/api/users](https://reqres.in/api/users).
- Se considerará para la evaluación, que las respuestas de la API sean exitosa (códigos 2xx).

## Requerimientos

### 1. Obtener a todos los usuarios

Nos socilitan toda la información de los usuarios retornada por la API, debemos almacenarla en una variable llamada `users_data` e imprimirla en pantalla:


```python
import requests # pip install requests

endpoint = "https://reqres.in/api/users"
respuesta = requests.get(endpoint)

users_data = respuesta.json()['data']
print(*users_data, sep="\n")
```

    {'id': 1, 'email': 'george.bluth@reqres.in', 'first_name': 'George', 'last_name': 'Bluth', 'avatar': 'https://reqres.in/img/faces/1-image.jpg'}
    {'id': 2, 'email': 'janet.weaver@reqres.in', 'first_name': 'Janet', 'last_name': 'Weaver', 'avatar': 'https://reqres.in/img/faces/2-image.jpg'}
    {'id': 3, 'email': 'emma.wong@reqres.in', 'first_name': 'Emma', 'last_name': 'Wong', 'avatar': 'https://reqres.in/img/faces/3-image.jpg'}
    {'id': 4, 'email': 'eve.holt@reqres.in', 'first_name': 'Eve', 'last_name': 'Holt', 'avatar': 'https://reqres.in/img/faces/4-image.jpg'}
    {'id': 5, 'email': 'charles.morris@reqres.in', 'first_name': 'Charles', 'last_name': 'Morris', 'avatar': 'https://reqres.in/img/faces/5-image.jpg'}
    {'id': 6, 'email': 'tracey.ramos@reqres.in', 'first_name': 'Tracey', 'last_name': 'Ramos', 'avatar': 'https://reqres.in/img/faces/6-image.jpg'}
    

### 2. Crear un usuario

Crear un nuevo usuario que tenga el nombre (*name*) de `ignacio` y de trabajo (*job*) `profesor`. Guarda el diccionario de respuesta en una variable llamada `created_user` e imprímela en pantalla:


```python
import requests

endpoint = "https://reqres.in/api/users"

nuevo_usuario = {
	"name": "ignacio",
	"job": "profesor"
}

respuesta = requests.post(endpoint, nuevo_usuario)

created_user = respuesta.json()
print(created_user)
```

    {'name': 'ignacio', 'job': 'profesor', 'id': '183', 'createdAt': '2024-05-17T11:25:56.643Z'}
    

### 3. Actualizar un usuario

Actualizar un usuario llamado `morpheus` para que tenga un campo llamado 'residence' igual a `zion`. Guarde el diccionario de respuesta en una variable llamada `updated_user` e imprímela en pantalla:


```python
import requests

endpoint = "https://reqres.in/api/users/2"

usuario_actualizado = {
	"name": "morpheus",
	"residence": "zion"
}

respuesta = requests.put(endpoint, usuario_actualizado)

updated_user = respuesta.json()
print(updated_user)
```

    {'name': 'morpheus', 'residence': 'zion', 'updatedAt': '2024-05-17T11:31:20.131Z'}
    

### 4. Eliminar a un usuario

Eliminar a un usuario llamado `Tracey`. Imprima el código de respuesta en pantalla:


```python
import requests

endpoint = "https://reqres.in/api/users"
respuesta = requests.get(endpoint)

users_data = respuesta.json()['data']

for user in users_data:
    if user['first_name'] == 'Tracey':
        deleted_user = requests.delete(f"{endpoint}/{user['id']}")
        print(deleted_user.status_code)
```

    204
    

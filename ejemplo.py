import requests

# URL del endpoint de la API
url = 'https://api.ejemplo.com/data'

# Si la API requiere una clave API para autenticación
headers = {
    'Authorization': 'Bearer tu_clave_api_aquí'
}

# Parámetros opcionales
params = {
    'param1': 'valor1',
    'param2': 'valor2'
}

response = requests.get(url, headers=headers, params=params)

# Verifica que la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error en la solicitud:', response.status_code)

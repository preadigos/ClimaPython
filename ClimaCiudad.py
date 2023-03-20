# coding=utf-8

import click
import requests

url = 'http://api.weatherstack.com/current'

ciudad = 'Lanus'
clave_api = '1edcd0bfda6233db6c788a57c7d3c5ae' # Reemplazar con tu propia clave de API
params = {'access_key': clave_api, 'query': ciudad}

respuesta = requests.get(url, params=params)

if respuesta.status_code == 200:
    # Si la solicitud se realizó correctamente, imprimir los datos del clima actual
    datos = respuesta.json()
    temperatura = datos['current']['temperature']
    descripcion = datos['current']['weather_descriptions'][0]
    print("El clima actual en", ciudad, "es de", temperatura, "grados Celsius y", descripcion)
else:
    # Si la solicitud no se realizó correctamente, imprimir un mensaje de error
    print("No se pudo obtener el clima para la ciudad especificada.")
#crear entorno Virtual= python -m venv venv|py -3.11.9 -m venv venv311
#Activar entorno venv\Scripts\activate
import requests



url = "https://pokeapi.co/api/v2/pokemon"



res = requests.get(url)

print(res.text)



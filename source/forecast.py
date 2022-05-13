"""
This code uses the requests library
and results in the weather forecast.

-> Requirements:
    . pip install requests
    . https://openweathermap.org/ -> register e get the API Key
"""

import requests

API_KEY = "type your API Key"
city = "curitiba"
link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=pt_br"

request = requests.get(link)
request_answer = request.json()
local = request_answer['name']
description = request_answer['weather'][0]['description']
min_temperature = request_answer['main']['temp_min'] - 273.15
max_temperature = request_answer['main']['temp_max'] - 273.15
cur_temperature = request_answer['main']['temp'] - 273.15
print()
print(f"City: {local}")
print(f"Clima: {description.title()}")
print(f"Temperature mínima: {min_temperature:.2f}ºC")
print(f"Temperature máxima: {max_temperature:.2f}ºC")
print(f"Temperature atual: {cur_temperature:.2f}ºC")

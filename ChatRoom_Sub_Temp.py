import socket
s = socket.socket()
host = '127.0.0.1'
port = int(80)

import requests
import time

def get_external_temperature(city):
    api_key = "4b608b026eabe79968f2bfe9e0c8b34f"
    weather_location = "Toronto"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={weather_location}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    data = response.json()
    print(data)
    return data['main']['temp']

print('Connecting to ', host, port)
s.connect((host, port))

while True:
  temperature = get_external_temperature("Tokyo")
  msg = str(temperature)
  msg = msg.encode()
  s.send(msg)
  time.sleep(5)
  msg = s.recv(1024)
  print('SERVER >> ', msg)
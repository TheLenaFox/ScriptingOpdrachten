import socket
s = socket.socket()
host = '127.0.0.1'
port = int(80)

import requests
import time

global weather_location
weather_location = input("Which city for weather data? ")

def get_external_temperature():
    api_key = "4b608b026eabe79968f2bfe9e0c8b34f"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={weather_location}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    data = response.json()
    #print(data)
    return data['main']['temp']

print('Connecting to ', host, port)
s.connect((host, port))

while True:
  temperature = get_external_temperature()
  msg = str(f"Temperature is: {temperature} in {weather_location}")
  msg = msg.encode()
  s.send(msg)
  time.sleep(5)
  msg = s.recv(1024)
  print('SERVER >> ', msg)

#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
s = socket.socket()         # Create a socket object
host = '' # Get local machine name
port = 80                # Reserve a port for your service.

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

print('Server started!')
print('Waiting for clients...')

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()     # Establish connection with client.
print('Got connection from', addr)
while True:
  temperature = get_external_temperature()
  msg = c.recv(1024)
  print(addr, ' >> ', msg)
  time.sleep(5)
  msg = str(f"Temperature is: {temperature} in {weather_location}")
  msg = msg.encode()
  c.send(msg);
  #c.close()

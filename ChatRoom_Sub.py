import socket
s = socket.socket()
host = '127.0.0.1'
port = int(80)

print('Connecting to ', host, port)
s.connect((host, port))

while True:
  msg = input('CLIENT >> ')
  msg = msg.encode()
  s.send(msg)
  msg = s.recv(1024)
  print('SERVER >> ', msg)
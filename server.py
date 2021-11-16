import socket

# socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
# bind server
server_socket.bind(('localhost', 8000))

bufferSize = 1024
msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)

print("Server up")

# enable broadcast
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


listen = True
while(listen):
  print("Server is listening")
  bytesAddressPair = server_socket.recvfrom(bufferSize)
  message = bytesAddressPair[0]
  address = bytesAddressPair[1]

  clientMsg = "Message from Client:{}".format(message)
  clientIP = "Client IP Address:{}".format(address)

  print(clientMsg)
  print(clientIP)

  server_socket.sendto(bytesToSend, address)

import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# get local machine name
host = socket.gethostname()

# set the port number
port = 12345

# send data to the server
message = input('Enter message to send: ')
client_socket.sendto(message.encode(), (host, port))

# receive response from the server
data, server_address = client_socket.recvfrom(1024)
print('Received data from {}:{}'.format(server_address[0], server_address[1]))
print('Response from server:', data.decode())

# close the socket
client_socket.close()
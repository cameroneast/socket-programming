import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# get local machine name
host = socket.gethostname()

# set the port number
port = 12345

# bind the socket to a public host, and a well-known port
server_socket.bind((host, port))

# listen for incoming data
print('Waiting for incoming data...')
while True:
    # receive data from the client
    data, address = server_socket.recvfrom(1024)
    print('Received data from {}:{}'.format(address[0], address[1]))
    
    # convert the data to uppercase
    data_upper = data.decode().upper()
    
    # send the uppercase data back to the client
    server_socket.sendto(data_upper.encode(), address)
    print('Sent data to {}:{}'.format(address[0], address[1]))
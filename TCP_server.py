import socket

# Define the server address and port
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address and port
server_socket.bind((SERVER_ADDRESS, SERVER_PORT))

# Listen for incoming connections
server_socket.listen()

print(f'Server listening on {SERVER_ADDRESS}:{SERVER_PORT}...')

# Wait for a client connection
client_socket, client_address = server_socket.accept()

print(f'Client connected from {client_address[0]}:{client_address[1]}')

# Receive data from the client
data = client_socket.recv(1024).decode()
print(f'Received data from client: {data}')

# convert the data to uppercase
data_upper = data.upper()

# send the uppercase data back to the client
client_socket.send(data_upper.encode())

# Close the client socket
client_socket.close()

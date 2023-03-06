import socket

# Define the server address and port
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

# Send data to the server
message = 'Hello, server!'
client_socket.send(message.encode())

# Receive data from the server
response = client_socket.recv(1024).decode()
print(f'Response from server: {response}')

# Close the socket
client_socket.close()
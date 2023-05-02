import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5001

# Create server socket
server_socket = socket.socket()
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print(f"Listening on {SERVER_HOST}:{SERVER_PORT}...")

# Accept incoming connections
client_socket, client_address = server_socket.accept()
print(f"Connected by {client_address}")

# Open the file
with open('ROBO_21064.pdf', 'rb') as file:
    # Read and send the file contents
    chunk = file.read(1024)
    while chunk:
        client_socket.send(chunk)
        chunk = file.read(1024)

# Close the connection
client_socket.close()
server_socket.close()
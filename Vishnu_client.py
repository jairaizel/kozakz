import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5001

# Connect to the server
client_socket = socket.socket()
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Receive the file contents
with open('receiver_file.pdf', 'wb') as file:
    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        file.write(chunk)

# Close the connection
client_socket.close()
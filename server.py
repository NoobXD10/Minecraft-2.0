import socket
import threading

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5555))
server.listen()

# Dictionary to store worlds and their associated codes
worlds = {}

def handle_client(client_socket, world_code):
    # Handle client logic here
    pass

while True:
    client, addr = server.accept()
    world_code = "ABC123"  # Generate a unique code for the world
    worlds[world_code] = {"players": []}

    # Send the world code to the client
    client.send(world_code.encode())

    # Start a new thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client, world_code))
    client_handler.start()


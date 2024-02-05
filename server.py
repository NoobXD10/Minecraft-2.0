import socket
import threading

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5555))
server.listen()

# Dictionary to store worlds and their associated codes
worlds = {}

def handle_client(client_socket, world_code):
    try:
        # Notify all clients in the world about the new player
        for player_socket in worlds[world_code]["players"]:
            player_socket.send(f"Player joined the world.".encode('utf-8'))

        # Add the player's socket to the list of players in the world
        worlds[world_code]["players"].append(client_socket)

        while True:
            # Receive and broadcast messages to other players
            message = client_socket.recv(1024).decode('utf-8')

            if message:
                print(f"Received message from {world_code}: {message}")

                for player_socket in worlds[world_code]["players"]:
                    if player_socket != client_socket:
                        player_socket.send(f"Player: {message}".encode('utf-8'))

    except:
        print("An error occurred.")
        client_socket.close()

while True:
    client, addr = server.accept()
    world_code = client.recv(1024).decode('utf-8')

    if world_code in worlds:
        worlds[world_code]["players"].append(client)
    else:
        worlds[world_code] = {"players": [client]}

    # Start a new thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client, world_code))
    client_handler.start()


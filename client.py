import socket
import threading

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print("An error occurred.")
            client.close()
            break

def send_message():
    while True:
        message = input()
        client.send(message.encode('utf-8'))

# Player creates a new world
world_code = input("Enter the world code: ")

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('server_ip_here', 5555))

# Send the world code to the server
client.send(world_code.encode())

# Start threads for receiving and sending messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_message)
send_thread.start()

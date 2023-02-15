"""
A Python File to implement client side of the chat application
"""
import socket
import sys
import threading
import random

# Check if the command line have provided sufficient arguments
if len(sys.argv) != 3:
    format()

# Initializing host, port, and buffer size
client_ip = sys.argv[1]
client_port = int(sys.argv[2])
print('Client IP->'+str(client_ip)+'Client Port->'+str(client_port))
address = (client_ip, client_port)
buffer_size = 1024

# Creating socket object for client connection
try:
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print('Error creating socket connection')
    sys.exit()

# Empty nickname will assign a random nickname
name = input("Nickname: ")
if name == '':
    name = "User" + str(random.randint(1, 9999))
    print('Nickname assigned by system is:' + name)

socket_client.sendto(f"SIGN-IN:{name}".encode(), address)


# Define how to run the UdpChatClient
def format():
    print('Format: python3 filename ip_address port ')
    print('Example: python3 UdpChatServer.py 192.168.1.235 7777')
    sys.exit("Argument not correct, see above arguments")


# Send text messages to the target server
def send():
    while True:
        # send the msg
        msg = input("")
        if msg == "quit":
            sys.exit()
        socket_client.sendto(f"{name}:{msg}".encode(), address)


# receive sender's ip address, port number, and text messages
def receive():
    while True:
        try:
            text, address = socket_client.recvfrom(buffer_size)
            print(f'<From {address[0]}:{address[1]}>: {text.decode()}')
        except:
            pass


# creating two threads for send and receive functions so that they can run same time by using multi-threading
receive_thread = threading.Thread(target=receive)
send_thread = threading.Thread(target=send)


# starting both threads
receive_thread.start()
send_thread.start()




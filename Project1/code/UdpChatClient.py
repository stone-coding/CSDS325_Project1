"""
A Python File to implement client side of the chat application
"""
import socket
import sys
import threading
import queue
import random

# check if the command line have provided sufficient arguments
if len(sys.argv) != 3:
    format()

host = sys.argv[1]
port = int(sys.argv[2])
print('Client IP->'+str(host)+' Port->'+str(port))
addr = (host, port)
buffer_size = 1024

# creating socket object for client connection
try:
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print('Error creating socket connection')
    sys.exit()

#
name = input("Nickname: ")
if name == '':
    name = "User" + str(random.randint(1,9999))
    print('Nickname assigned by system is:' + name)


def format():
    print('Usage: python3 filename ip_address port ')
    print('Example: python3 UdpChatServer.py 192.168.1.235 7777')
    sys.exit("Argument not correct, see above arguments")


def receive():
    while True:
        try:
            text, addr = socket_client.recvfrom(buffer_size)
            print(f'<From {addr}>: {text.decode()}')
            # print(f"{text.decode()} ")
        except:
            pass


t = threading.Thread(target=receive).start()

socket_client.sendto(f"SIGNUP_TAG:{name}".encode(), addr)

while True:
    # send the msg
    # data = input("Please enter the messages send the server side:")
    data = input("")
    if data == 'exit' or not data:
        break
    socket_client.sendto(f"{name}:{data}".encode(), addr)




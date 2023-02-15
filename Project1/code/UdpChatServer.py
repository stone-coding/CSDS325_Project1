"""
A Python File to implement sever side of the chat application
"""
import socket
import sys
import threading
import queue


# check if the command line have provided sufficient arguments
if len(sys.argv) != 2:
    format()

# text stores chat messages and clients stores each client
texts = queue.Queue()
clients = []
buffer_size = 1024


# take the first argument for ip address(host) and second argument for the port number
ip = socket.gethostbyname(socket.gethostname())
port = int(sys.argv[1])
print('Server hosting on IP-> '+str(ip))
address = (ip, port)

# creating socket object for client connection
try:
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_server.bind(address)
    print('Sever Initialized...')
except socket.error:
    print('Error creating socket connection')
    sys.exit()


# defines how to run the UdpChatServer
def format():
    print('Format: python3 filename port')
    print('Example: python3 UdpChatServer.py 7777')
    sys.exit("Argument not correct, see above arguments")


# receive connections from client with a maximum buffer size 1024 bytes
# and stores the info of client to texts
def receive_text():
    try:
        while True:
            text, address = socket_server.recvfrom(buffer_size)
            texts.put((text, address))
    except:
        pass


# read clients and update the current list if clients
def broadcast_text():
    while True:
        while not texts.empty():
            text, address = texts.get()
            print(text.decode())
            if address not in clients:
                clients.append(address)
            for client in clients:
                try:
                    if text.decode().startwith("SIGN-IN:"):
                        name = text.decode()[text.decode().index(":") + 1:]
                        socket_server.sendto(f"{name} joined!".encode(), client)
                    else:
                        socket_server.sendto(text, client)
                except:
                    clients.remove(client)


# creating two threads for receive and broadcast functions so that they can run same time by using multi-threading
receive_thread = threading.Thread(target=receive_text)
broadcast_thread = threading.Thread(target=broadcast_text)

# starting both threads
receive_thread.start()
broadcast_thread.start()

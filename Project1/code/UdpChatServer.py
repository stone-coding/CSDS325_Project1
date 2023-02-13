"""
A Python File to implement sever side of the chat application
"""
import socket
import sys
import threading
import queue


def format():
    print('Usage: python3 filename port')
    print('Example: python3 UdpChatServer.py 7777')
    sys.exit("Argument not correct, see above arguments")


# check if the command line have provided sufficient arguments
if len(sys.argv) != 2:
    format()

# text stores chat messages and clients stores each client
texts = queue.Queue()
clients = []

# take the first argument for ip address(host) and second argument for the port number
host = socket.gethostbyname(socket.gethostname())
port = int(sys.argv[1])
print('Server hosting on IP-> '+str(host))
addr = (host, port)
buffer_size = 1024

# creating socket object for client connection
try:
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_server.bind(addr)
    print('Sever Initialized...')
except socket.error:
    print('Error creating socket connection')
    sys.exit()


# receive the information from client with a maximum buffer size 1024 bytes
# and stores the info of client to texts
def receive():
    while True:
        try:
            text, addr = socket_server.recvfrom(buffer_size)
            texts.put((text, addr))
            # print('<From %s>: %s' % (addr, text.decode()))
            # socket_server.sendto(('<From %s>- %s' % (addr, text.decode())).encode(), addr)
        except:
            pass


def broadcast():
    while True:
        while not texts.empty():
            text, addr = texts.get()
            print(text.decode())
            if addr not in clients:
                clients.append(addr)
            for client in clients:
                try:
                    if text.decode().startswith("SIGNUP_TAG:"):
                        name = text.decode()[text.decode().index(":") + 1:]
                        socket_server.sendto(f"{name} joined!".encode(), client)
                    else:
                        socket_server.sendto(text, client)
                except:
                    clients.remove(client)


if __name__ == '__main__':
    # creating two threads for receive and broadcast functions so that they can run same time by using multi-threading
    receive_thread = threading.Thread(target=receive)
    broadcast_thread = threading.Thread(target=broadcast)

    # starting both threads
    receive_thread.start()
    broadcast_thread.start()






















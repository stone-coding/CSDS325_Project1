"""
A Python File to implement sever side of the chat application
"""
import socket
import sys
import threading
import queue

# check if the command line have provided sufficient arguments
if len(sys.argv) != 2:
    print('''
          argv is error!!!
          input should be as: python3 filename.py port_number
          ''')
    exit()

# take the first argument for ip address(host) and second argument for the port number
host = socket.gethostbyname(socket.gethostname())
port = int(sys.argv[1])
print('Server hosting on IP-> '+str(host))
addr = (host, port)
buffer_size = 1024
# creating socket obj
socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# binding the ip address and the port number
socket_server.bind(addr)
# text stores chat messages and clients stores each client
texts = queue.Queue()
clients = []


def receive():
    print('Sever Initialized...')
    # receive the information from client with a maximum buffer size 1024 bytes
    # info returns a bytes obj, convert it to str by decoding it as UTF-8
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


t1 = threading.Thread(target=receive)
t2 = threading.Thread(target=broadcast)

t1.start()
t2.start()



















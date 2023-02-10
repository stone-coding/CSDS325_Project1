"""
A Python File to implement sever side of the chat application
"""
import socket
import sys
import threading
import queue

# check if the command line have provided sufficient arguments
if len(sys.argv) < 3:
    print('''
          argv is error!!!
          input should be as: python3 filename.py ip_address port_number
          ''')
    exit()

# take the first argument for ip address(host) and second argument for the port number
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST, PORT)
BUFFSIZE = 1024


texts = queue.Queue()
clients = []

# creating socket obj
socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# binding the ip address and the port number
socket_server.bind(ADDR)


def receive():
    print('Sever Initialized...')
    # receive the information from client with a maximum buffer size 1024 bytes
    # info returns a bytes obj, convert it to str by decoding it as UTF-8
    while True:
        try:
            text, addr = socket_server.recvfrom(BUFFSIZE)
            texts.put((text,addr))
            print('Recv from %s: %s ' % (addr, text.decode('UTF-8')))
            socket_server.sendto((' %s: %s ' % (addr, text.decode('UTF-8'))).encode(), addr)
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



















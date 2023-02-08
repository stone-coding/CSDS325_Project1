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


message = queue.Queue()
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
        info, addr = socket_server.recvfrom(BUFFSIZE)
        print('Recv from %s: %s ' %(addr, info.decode('UTF-8')))
        socket_server.sendto((' %s: %s ' %(addr, info.decode('UTF-8'))).encode(), addr)


        # send_data = input('Please send information back to the client side: ')
        # socket_server.sendto(send_data.encode('UTF-8'), addr)

if __name__ == '__main__':
    receive()















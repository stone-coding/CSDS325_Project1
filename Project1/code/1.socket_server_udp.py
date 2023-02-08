"""
A file displays the socket server (udp)
"""
from socket import *
import sys
from time import ctime

if len(sys.argv) < 3:
    print('''
          argv is error!!!
          input should be as python3 filename.py ip_address port_number
            ''')

HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST, PORT)
BUFFSIZE = 1024


# creating socket obj
socket_server = socket(AF_INET, SOCK_DGRAM)

# binding the ip address and the port number
socket_server.bind(ADDR)

print('Sever Initialized...')

# receive the information from client with a maximum buffer size 1024 bytes
# info returns a bytes obj, convert it to str by decoding it as UTF-8
while True:
    info, addr = socket_server.recvfrom(BUFFSIZE)
    print('Recv from %s: %s ' %(addr, info.decode('UTF-8')))
    socket_server.sendto(("[%s] 接收到消息" % ctime()).encode(), addr)
    # socket_server.sendto(("[%s] 接收到消息" %ctime()).encode(),addr)


    # send_data = input('Please send information back to the client side: ')
    # socket_server.sendto(send_data.encode('UTF-8'), addr)













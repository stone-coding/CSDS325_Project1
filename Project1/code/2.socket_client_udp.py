"""
A file displays the socket client (udp)
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
socket_client = socket(AF_INET, SOCK_DGRAM)


while True:
    # send the msg
    data = input("Please enter the messages send the server side:")
    if data == 'exit' or not data:
        break
    socket_client.sendto(data.encode("UTF-8"), ADDR)
    # give a 1024 buffer receive the msg
    reve_data, addr = socket_client.recvfrom(BUFFSIZE)
    print(f"Messsage from the server is:{reve_data.decode('UTF-8')}")

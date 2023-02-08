"""
A Python File to implement client side of the chat application
"""
import socket
import sys
import threading
import queue

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
socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:
    # send the msg
    data = input("Please enter the messages send the server side:")
    if data == 'exit' or not data:
        break
    socket_client.sendto(data.encode("UTF-8"), ADDR)
    # give a 1024 buffer receive the msg
    reve_data, addr = socket_client.recvfrom(BUFFSIZE)
    print(f"Messsage Received by the server is:{reve_data.decode('UTF-8')}")

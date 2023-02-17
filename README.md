# Project 1
It is a simple UDP Chat Application made with Python3 based on the Pycharm IDE. 
It used the UDP protocol as the tool to transmit the data between client and server 
<br />
Python Version == 3.9
<br />
Quick Start:
Server:
       python3 UdpChatServer.py <port> 
Client:
       python3 UdpChatServer.py <server ip> <server port>
<br />
<br />
Functions:
Server to client:
Incoming -> Server put the text message from sender with sender's ip and port to every client which greeted server.
<br />
Client to server:
Greeeting -> User will type a "nickname" as a indentity indentification. A message as "nickname" joined will register the client as active in the server
Message -> Client send the message packets to the server, and server receives the message and send it back to peer clients(include this sending client)
<br />
Sample Format:
<br />
<br />
Final Note:
When running the server and client for multiple times, it is good to know a way to kill the processes on the terminal as:
https://stackoverflow.com/questions/22334761/how-to-kill-all-processes-with-the-same-name-using-os-x-terminal







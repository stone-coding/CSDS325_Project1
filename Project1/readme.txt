It is a simple UDP Chat Application made with Python3 based on the Pycharm IDE.
It used the UDP protocol as the tool to transmit the data between client and server

Python Version == 3.9

Quick Start:
Server:

       python3 UdpChatServer.py <port> 
Client:

       python3 UdpChatClient.py <server ip> <server port>

Functions:
Server to client:
Incoming -> Server put the text message from sender with sender's ip and port to every client which greeted server.

Client to server:
Greeeting -> User will type a "nickname" as a indentity indentification. A message as '"nickname" joined' will register the client as active in the server
Message -> Client send the message packets to the server, and server receives the message and send it back to peer clients(include this sending client)

Sample Format:
Server:
(base) shihaomiao@shihaomaodeAir8 code % python3 UdpChatServer.py 8888
Server hosting on IP-> 192.168.1.235 Server hosting on port-> 8888
Sever Initialized...
SIGN-IN:Stone
SIGN-IN:Peter
Stone:Hi Peter
Peter:Hi Stone


Client 1:
(base) shihaomiao@shihaomaodeAir8 code % python3 UdpChatClient.py 192.168.1.235 8888
Client IP->192.168.1.235Client Port->8888
Nickname: Stone
<From 192.168.1.235:8888>: Stone joined!
<From 192.168.1.235:8888>: Peter joined!
Hi Peter   
<From 192.168.1.235:8888>: Stone:Hi Peter
<From 192.168.1.235:8888>: Peter:Hi Stone
quit


Client2:
(base) shihaomiao@shihaomaodeAir8 code % python3 UdpChatClient.py 192.168.1.235 8888
Client IP->192.168.1.235Client Port->8888
Nickname: Peter 
<From 192.168.1.235:8888>: Peter joined!
<From 192.168.1.235:8888>: Stone:Hi Peter
Hi Stone
<From 192.168.1.235:8888>: Peter:Hi Stone




Final Note:
When running the server and client for multiple times, it is good to know a way to kill the processes on the terminal as:
https://stackoverflow.com/questions/22334761/how-to-kill-all-processes-with-the-same-name-using-os-x-terminal

GitHub Link:https://github.com/stone-coding/CSDS325_Spring2023.git
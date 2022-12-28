import socket

# serverAddressPort = ("127.0.0.1", 5000)
bufferSize = 1024

server_ip = '192.168.137.243'
server_port = 15000

client_id = input('Input the client id\n')

bKeepDefaults = input("Do you want to keep the defaults? y/n\n")

if(bKeepDefaults == "no"):
    # client_id = input("Input the client id:\n")
    server_ip = input("Input the server ip:\n")

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
#msgFromClient = "Hello UDP Server"
#bytesToSend = str.encode(msgFromClient)
#UDPClientSocket.sendto(bytesToSend, (server_ip, server_port))

while(True):
    value = input("input the value to send\n")
    value = float(value)
    msg = "{}#{}".format(client_id, value)
    
    bytesToSend = str.encode(msg)
    UDPClientSocket.sendto(bytesToSend, (server_ip, server_port))

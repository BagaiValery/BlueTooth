import socket
from converter import convert_db_to_distance
from phone_coordinates import phone_coordinates
from generate_image import show_image
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

client_dictionary = {}

def run_server():

    # configuring
    server_ip = "192.168.137.243"
    port = 15000
    bufferSize  = 1024

    bKeepDefault = input("Keep default configuration? y/n: ")

    if(bKeepDefault == "n"):
        server_ip = input("Enter the server interface ip")

    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    UDPServerSocket.bind((server_ip, port))

    print("UDP server up and listening\n")

    while (True):
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

        message = bytesAddressPair[0].decode()
        address = bytesAddressPair[1]

        clientMsg = "Message from {} Client:{}".format(address, message)

        print(clientMsg)

        (client_id, value) = message.split("#", 1)

        client_dictionary[client_id] = float(value)

        print(client_dictionary)


run_server()
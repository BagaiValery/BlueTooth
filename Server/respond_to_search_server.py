import random
import socket

def respond_to_search():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', 5001))

    while True:
        message, address = server_socket.recvfrom(1024)
        print('got message from {}'.format(address))

        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

        message = b'hello' # bytes('Hello from {}'.format(local_ip), 'utf-8')
        server_socket.sendto(message, address)

respond_to_search()
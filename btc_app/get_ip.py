import socket
def get_local_ip():
    print(socket.gethostbyname(socket.gethostname()))

if __name__ == '__main__':
    get_local_ip()
from socket import (socket,
                    AF_INET,
                    SOCK_STREAM,
                    SHUT_RDWR)
from sys import getsizeof as sizeof
from json import dumps as to_json, loads as from_json

class Client(object):
    """docstring for Server"""
    def __init__(self, address, port, identifier):
        super(Client, self).__init__()
        self.address = address
        self.port = port
        self.identifier = identifier
        self.socket = socket(AF_INET, SOCK_STREAM)
    def connect(self):
        self.socket.connect((self.address, self.port))
        self.send_data({'name' : self.identifier})
    def receive_data(self):
        size = self.socket.recv(4)
        json_data = self.socket.recv(size)
        return from_json(json_data)
    def send_data(self, data, destination):
        json_data = to_json({'source' : self.identifier,
                             'destination' : destination,
                             'data' : data})
        self.socket.sendall(sizeof(json_data))
        self.socket.sendall(json_data)
    def close(self):
        self.socket.shutdown(SHUT_RDWR)
        self.close()
    def address_port(self):
        return self.socket.getsockname()

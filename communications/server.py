from socket import socket, SOMAXCONN, AF_INET, SOCK_STREAM, error as socket_error, SHUT_RDWR
from threading import RLock as Lock, Thread
from sys import getsizeof as sizeof
from json import dumps as to_json, loads as from_json
from struct import unpack, pack

class Server(Thread):
    """docstring for Server"""
    def __init__(self, address='0.0.0.0', port=0):
        super(Server, self).__init__()
        self.address = address
        self.port = port
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind((address, port))
        self.connections = dict()
        self.connections_lock = Lock()
        self.running = False
    def run(self):
        self.server_socket.listen(SOMAXCONN)
        self.running = True
        while self.running:
            try:
                client_socket = self.server_socket.accept()
            except socket_error as e:
                continue
            ClientHandler(client_socket[0], self).start()
        for _, handler in self.connections.iteritems():
            if handler.running:
                handler.join()
    def register_connection(self, name, handler):
        self.connections_lock.acquire()
        self.connections[name] = handler
        self.connections_lock.release()
    def get_destination_handler(self, name):
        handler = self.connections[name]
        if handler.running:
            return handler
        else:
            raise KeyError
    def close(self):
        self.running = False
        self.server_socket.shutdown(SHUT_RDWR)
        self.server_socket.close()
    def address_port(self):
        return self.server_socket.getsockname()
    def clients(self):
        for name, handler in self.connections.iteritems():
            if handler.running:
                print 'Name: ', name, ' via ', handler.address_port()
                
class ClientHandler(Thread):
    """docstring for ClientHandler"""
    def __init__(self, client_socket, server):
        super(ClientHandler, self).__init__()
        self.client_socket = client_socket
        self.server = server
        self.socket_rd_lock = Lock()
        self.socket_wr_lock = Lock()
        self.name = None
        self.running = False
    def run(self):
        login_data = self.receive_data()
        print 'Cliente conectado: ', login_data
        self.name = login_data['name']
        self.server.register_connection(self.name, self)
        self.running = True
        while self.running:
            try:
                data = self.receive_data()
                print 'Datos recibidos de ', self.name, ': ', data
            except socket_error as exception:
                self.running = False
            else:
                try:
                    handler = self.server.get_destination_handler(data['destination'])
                    handler.send_data(data)
                except KeyError as exception:
                    self.send_data({'error' : 'UnreachableHost'})
                    continue
                except socket_error as exception:
                    self.send_data({'error' : 'UnreachableHost'})
                    continue
        self.client_socket.shutdown(SHUT_RDWR)
        self.client_socket.close()
    def receive_raw_data(self):
        self.socket_rd_lock.acquire()
        size_buf = self.client_socket.recv(4)
        size = unpack('!i', size_buf[:4])[0]
        json_data = self.client_socket.recv(size)
        self.socket_rd_lock.release()
        return json_data
    def receive_data(self):
        return from_json(self.receive_raw_data())
    def send_data(self, data):
        json_data = to_json(data)
        self.send_raw_data(json_data)
    def send_raw_data(self, raw_data):
        self.socket_wr_lock.acquire()
        size = pack('!i', sizeof(raw_data))
        self.client_socket.sendall(size)
        self.client_socket.sendall(raw_data)
        self.socket_wr_lock.release()
    def address_port(self):
        return self.client_socket.getsockname()

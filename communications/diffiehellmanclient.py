from communications.client import Client
class DiffieHellmanClient(Client):
    """docstring for DiffieHellmanClient"""
    def __init__(self, address, prot, identifier, parameters):
        super(DiffieHellmanClient, self).__init__()
        self.modulus, self.base, self.private_key = parameters
        self.public_key = self.base**self.private_key % self.modulus
        self.destination_public_key = None
        self.shared_key = None
    def connect(self, destination):
        super(DiffieHellmanClient, self).connect()
        self.send_data(self.public_key)
        packet = self.receive_data()
        if packet['source'] == destination:
            self.destination_public_key = packet['data']
        self.shared_key = self.destination_public_key**self.private_key % self.modulus

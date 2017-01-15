from .client import Client
from Crypto.cryptomethods import PlainText

class CryptoUser(object):
    """docstring for CryptoUser"""
    def __init__(self, name, address='localhost', port=25000, cryptomethod=None):
        super(CryptoUser, self).__init__()
        if cryptomethod:
            self.cryptomethod = cryptomethod
        else:
            self.cryptomethod = PlainText()
        self.net_client = Client(address, port, name)
    def send(self, message, destination):
        encrypted_message = self.cryptomethod.encrypt(message.upper().replace(" ",""))
        self.net_client.send_data(encrypted_message, destination)
    def receive(self):
        encrypted_message = self.net_client.receive_data()
        encrypted_message['data'] = self.cryptomethod.decrypt(encrypted_message['data'])
        return encrypted_message
    def connect(self):
        self.net_client.connect()
    def close(self):
        self.net_client.close()

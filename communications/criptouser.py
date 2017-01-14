class CryptoUser(object):
    """docstring for CryptoUser"""
    def __init__(self, name, cryptomethod, net_client):
        super(CryptoUser, self).__init__()
        self.name = name
        self.cryptomethod = cryptomethod
        self.net_client = net_client
    def send(self, message):
        encrypted_message = self.cryptomethod.encrypt(message.upper().replace(" ",""))
        self.net_client.send_data(encrypted_message)
    def receive(self):
        encrypted_message = self.net_client.receive_data()
        return self.cryptomethod.decrypt(encrypted_message)

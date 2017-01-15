from .cryptomethod import CryptoMethod

class Cesar(CryptoMethod):
    """docstring for CryptoMethod"""
    def __init__(self):
        super(Cesar, self).__init__()
    def encrypt(self, message):
        return ''.join([chr(ord(x) + 1) if x != 'Z' else 'A' for x in message])
    def decrypt(self, message):
        return ''.join([chr(ord(x) - 1) if x != 'A' else 'Z' for x in message])

class Cesar(object):
    """docstring for CryptoMethod"""
    def __init__(self):
        super(Cesar, self).__init__()
    def encrypt(self, message):
        return [chr(ord(x) + 1) if x != 'Z' else 'A' for x in message]
    def decrypt(self, message):
        return [chr(ord(x) - 1) if x != 'A' else 'Z' for x in message]

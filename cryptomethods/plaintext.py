from .cryptomethod import CryptoMethod

class PlainText(CryptoMethod):
    """docstring for CryptoMethod"""
    def __init__(self):
        super(PlainText, self).__init__()
    def encrypt(self, message):
        return message
    def decrypt(self, message):
        return message

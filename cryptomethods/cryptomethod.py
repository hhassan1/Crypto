class CryptoMethod(object):
    """docstring for CryptoMethod"""
    def __init__(self):
        super(CryptoMethod, self).__init__()
    def encrypt(self, message):
        raise NotImplementedError
    def decrypt(self, message):
        raise NotImplementedError
        
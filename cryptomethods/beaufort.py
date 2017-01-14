class Beaufort(object):
    """docstring for CryptoMethod"""
    def __init__(self, keyword):
        super(Beaufort, self).__init__()
        self.keyword = keyword
        self.letter_count = ord('Z') - ord('A') + 1
    def encrypt(self, message):
        self.keyword = self.keyword * ((len(message) + 1)/len(self.keyword))
        return [chr(ord('A') + ((ord(x) - ord(y)) % self.letter_count))
                for (x, y) in zip(self.keyword, message)]
    def decrypt(self, message):
        return self.encrypt(message)

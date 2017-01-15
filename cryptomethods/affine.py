from .cryptomethod import CryptoMethod

class Affine(CryptoMethod):
    """docstring for CryptoMethod"""
    def __init__(self, a_key, b_key):
        super(Affine, self).__init__()
        self.a_key = a_key
        self.b_key = b_key
        self.letter_count = ord('Z') - ord('A') + 1
        self.inverse_a_key = self._inverse_a(a_key, self.letter_count)
    def encrypt(self, message):
        return ''.join([chr(ord('A') + (((ord(x) - ord('A'))*self.a_key + self.b_key) %
                                self.letter_count)) for x in message])
    def decrypt(self, message):
        return ''.join([chr(ord('A') + (((ord(x) - ord('A') - self.b_key)*self.inverse_a_key) %
                                self.letter_count)) for x in message])
    @staticmethod
    def _inverse_a(a, m):
        remainder = [a, m]
        bezout = [1, 0]
        i = 1
        while remainder[i] != 0:
            quotient = remainder[i-1] / remainder[i]
            remainder.append(remainder[i-1] - quotient*remainder[i])
            bezout.append(bezout[i-1] - quotient*bezout[i])
            i = i + 1
        return bezout[i-1]

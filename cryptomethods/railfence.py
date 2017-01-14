class RailFence(object):
    """docstring for CryptoMethod"""
    def __init__(self, rail_number):
        super(RailFence, self).__init__()
        self.rail_number = rail_number
        if rail_number < 1:
            raise ValueError
    def encrypt(self, message):
        if self.rail_number == 1:
            return message
        rails = self._create_rails(len(message))
        filled_rails = [[message[i] for i in rail] for rail in rails]
        return ''.join(filled_rails)
    def decrypt(self, message):
        if self.rail_number == 1:
            return message
        decrypted_message = [' ']*len(message)
        rails = self._create_rails(len(message))
        counter = 0
        for rail in rails:
            for i in rail:
                decrypted_message[counter] = message[i]
                counter += 1
        return ''.join(decrypted_message)
    def _create_rails(self, length):
        rails = []*self.rail_number
        pointer = 0
        direction = 1
        for i in range(length):
            rails[pointer] = i
            if pointer == self.rail_number - 1:
                direction *= -1
            pointer += direction
        return rails

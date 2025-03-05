#他人の丸パクリ　それがどうした僕ドラ
import random
import string
class RandomString:
    def __init__(self,number):
        self.number = number
        self.letters = string.ascii_letters
    def get_random_string(self):
        random_letters = random.choices(self.letters,k = self.number)
        random_string  = ''.join(random_letters)
        return random_string
import string
import secrets

class GenPassword():
    def __init__(self, length: int, numbers: bool, special: bool, caps: bool):
        self.length = length
        self.numbers = numbers
        self.special = special
        self.caps = caps
        
        self.punctuation = ".!@#$%^&*"
    
    def create_alphabet(self) -> str:
        alphabet = string.ascii_lowercase
        if self.caps:
            alphabet += string.ascii_letters
        else:
            alphabet += string.ascii_lowercase
        if self.numbers:
            alphabet += string.digits
        if self.special:
            alphabet += self.punctuation
        return alphabet

    def generate_password(self) -> str:
        alphabet = self.create_alphabet()
        
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(self.length))
            if any(c.islower() for c in password):
                if self.caps:
                    if not (any(c.isupper() for c in password)):
                        continue
                if self.numbers:
                    if not (any(c.isdigit() for c in password)):
                        continue
                if self.special:
                    if not (any(c in self.punctuation for c in password)):
                        continue
                break
        return password

class GenPassphrase():
    def __init__(self, length: int, separator: str, number: bool, capitalise: bool):
        self.length = length
        self.separator = separator
        self.number = number
        self.capitalise = capitalise
        
        self.words = self.read_words_txt()
        
    def read_words_txt(self) -> dict:
        d = {}
        with open("words.txt") as f:
            for line in f:
                (key, val) = line.split()
                d[int(key)] = val
        return d
    
    def generate_word_no(self) -> int:
        number = ""
        for i in range(5):
            number += str(secrets.randbelow(6) + 1)
        return int(number)
            
    def get_word(self, number: int) -> str:
        return self.words[number]
    
    def generate_passphrase(self) -> str:
        passphrase = ""
        for i in range(self.length):
            word = self.get_word(self.generate_word_no())
            if self.capitalise:
                word = word.capitalize()
            passphrase += word
            if i != self.length - 1:
                passphrase += self.separator
        if self.number:
            passphrase += str(secrets.randbelow(100))
        return passphrase
        
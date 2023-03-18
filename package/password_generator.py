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
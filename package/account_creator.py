from argon2 import PasswordHasher
from package.model import Account

class accountCreator():
    def __init__(self, email, password, name=None, pwrd_hint=None):
        self.email = email
        self.password = password
        self.name = name
        self.pwrd_hint = pwrd_hint
        self.passHashing()
        self.acc = Account.Account(self.email, self.pwrd_hash, self.name, self.pwrd_hint)

    def passHashing(self):
        ph = PasswordHasher()
        self.pwrd_hash = ph.hash(self.password)
        
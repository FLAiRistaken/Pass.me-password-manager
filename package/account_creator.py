from argon2 import PasswordHasher



class AccountCreator:
    def __init__(self, email, password, name=None, pwrd_hint=None):
        self.email = email
        self.password = password
        self.name = name
        self.pwrd_hint = pwrd_hint
        self.pass_hashing()
        self.acc = Account(
            self.email, self.pwrd_hash, self.name, self.pwrd_hint
        )

    def pass_hashing(self):
        ph = PasswordHasher()
        self.pwrd_hash = ph.hash(self.password)


class Account:
    def __init__(self, email, pwrd_hash, name=None, pwrd_hint=None):
        self.email = email
        self.name = name
        self.pwrd_hint = pwrd_hint
        self.pwrd_hash = pwrd_hash
        
    def __str__ (self):
        return f"[email] = {self.email}, [name] = {self.name}, [passHint] = {self.pwrd_hint}, [passHash] = {self.pwrd_hash}"
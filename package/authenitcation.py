import argon2.exceptions
from argon2 import low_level, Type



class Authentication:
    from package.db_connect import ApiConnect
    authenticated = False

    def __init__(self, api:ApiConnect, email:str = None, password:str = None):
        self.email = email
        self.password = password
        self.api = api

    def authenticate(self):
        ph = PasswordHasher(self.email, self.password)

        pwrd_hash = ph.password_hashing(ph.password, ph.email)

        return self.api.login_with_creds(self.email, pwrd_hash)

    def auth_with_tokens(self):
        return self.api.login_with_access_token()



class PasswordHasher:
    def __init__(self, email:str, password:str):
        self.email = email.encode('utf-8')
        self.password = password.encode('utf-8')
        self.hasher = low_level.hash_secret
        self.type = Type.ID
        self.time = 3
        self.memory = 65536
        self.para = 4
        self.length = 32
        self.version = 19


    def hashing(self, secret:bytes, salt:bytes):
        test = self.hasher(secret, salt, self.time, self.memory, self.para, self.length, self.type, self.version)
        return test

    def password_hashing(self, password, email):
        mkey = self.hashing(password, email)
        return (self.hashing(mkey, password)).decode('utf-8')

    def verify(self, hashed, password, email):
        mkey = self.hashing(password, email)
        return low_level.verify_secret(hashed.encode('utf-8'), mkey, self.type)

    def generate_mkey(self, password, email):
        return self.hashing(password, email)
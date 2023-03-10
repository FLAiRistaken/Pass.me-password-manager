import argon2.exceptions
from argon2 import low_level, Type



class Authentication:
    authenticated = False

    def __init__(self, email:str, password:str):
        self.email = email
        self.password = password
        self.pass_verify()

    def pass_verify(self):
        from package.db_connect import dbConnect
        db = dbConnect()
        sql = "SELECT pwrd_hash FROM user_auth WHERE email = (%s)"
        pwrd_hash = db.queryone(sql=(sql), params=(self.email,))
        ph = PasswordHasher(self.email, self.password)
        try:
            if ph.verify(pwrd_hash[0], ph.password, ph.email):
                self.authenticated = True
        except argon2.exceptions.VerifyMismatchError:
            self.authenticated = False
            print("Password does not match")
        except TypeError:
            self.authenticated = False
            print("Record not found")

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
        

    def hashing(self, secret, salt):
        test = self.hasher(secret, salt, self.time, self.memory, self.para, self.length, self.type, self.version)
        return test
    
    def password_hashing(self, password, email):
        mkey = self.hashing(password, email)
        return (self.hashing(mkey, password)).decode('utf-8')

    def verify(self, hashed, password, email):
        mkey = self.hashing(password, email)
        return low_level.verify_secret(hashed.encode('utf-8'), mkey, self.type)
from argon2 import PasswordHasher
import argon2.exceptions
from package import db_connect

class authentication():
    authenticated = None
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.passVerify()
        
    def passVerify(self):
        db = db_connect.dbConnect()
        sql = "SELECT pwrd_hash FROM user_auth WHERE email = (%s)"
        pwrd_hash = db.queryone(sql = (sql), params = (self.email,))
        ph = PasswordHasher()
        try:
            if ph.verify(pwrd_hash[0], self.password):
                self.authenticated = True
        except argon2.exceptions.VerifyMismatchError:
            self.authenticated = False

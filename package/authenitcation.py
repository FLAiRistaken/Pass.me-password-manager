import argon2.exceptions
from argon2 import PasswordHasher

from package import db_connect


class Authentication:
    authenticated = None

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.pass_verify()

    def pass_verify(self):
        db = db_connect.dbConnect()
        sql = "SELECT pwrd_hash FROM user_auth WHERE email = (%s)"
        pwrd_hash = db.queryone(sql=(sql), params=(self.email,))
        ph = PasswordHasher()
        try:
            if ph.verify(pwrd_hash[0], self.password):
                self.authenticated = True
        except argon2.exceptions.VerifyMismatchError:
            self.authenticated = False
            print("Password does not match")
        except TypeError:
            self.authenticated = False
            print("Record not found")

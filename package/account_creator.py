

class AccountCreator:
    from package.encryption import Encrypt
    def __init__(self, email, password, name=None, pwrd_hint=None):
        self.email = email
        self.password = password
        self.name = name
        self.pwrd_hint = pwrd_hint
        self.pass_hashing()
        enc = self.Encrypt()
        self.key = enc.create_encrypted_vault_key(self.get_mkey(), self.email)
        self.acc = Account(
            self.email, self.pwrd_hash, self.key[0].hex(), self.key[1].hex(), self.name, self.pwrd_hint
        )

    def pass_hashing(self):
        from package.authenitcation import PasswordHasher
        ph = PasswordHasher(self.email, self.password)
        self.pwrd_hash = ph.password_hashing(ph.password, ph.email)

    def get_mkey(self):
        from package.authenitcation import PasswordHasher
        ph = PasswordHasher(self.email, self.password)
        return ph.generate_mkey(ph.password, ph.email)


class Account:
    def __init__(self, email, pwrd_hash, vkey, iv, name=None, pwrd_hint=None):
        self.email = email
        self.name = name
        self.vkey = vkey
        self.iv = iv
        self.pwrd_hint = pwrd_hint
        self.pwrd_hash = pwrd_hash

    def __str__ (self):
        return f"[email] = {self.email}, [name] = {self.name}, [passHint] = {self.pwrd_hint}, [passHash] = {self.pwrd_hash}, [key] = {self.key}, [iv] = {self.iv}"
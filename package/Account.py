
class Account():
    def __init__(self, email, pwrd_hash, name=None, pwrd_hint=None):
        self.email = email
        self.name = name
        self.pwrd_hint = pwrd_hint
        self.pwrd_hash = pwrd_hash
        
    def __str__ (self):
        return f"[email] = {self.email}, [name] = {self.name}, [passHint] = {self.pwrd_hint}, [passHash] = {self.pwrd_hash}"
    
    
    
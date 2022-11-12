import mysql.connector
from package import Account

class dbConnect():
    def __init__(self):
        self.conn = mysql.connector.connect("198.12.124.54", "joe", "user", 3306)
        self.cursor = self.conn.cursor()
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, exc_trace):
        self.close()
        
    @property
    def connection(self):
        return self.conn
    
    @property
    def cursor(self):
        return self.cursor
    
    def commit(self):
        self.connection.commit()
        
    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()
        
    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())
    
    def fetchall(self):
        return self.cursor.fetchall()
    
    def fetchone(self):
        return self.cursor.fetchone()
    
    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()
    
    def new_user(self, account: Account.Account):
        sql_auth = "INSERT INTO user_auth (email, pwrd_hash) VALUES (?, ?)"
        self.execute( sql_auth, (account.email, account.pwrd_hash))
        sql_details = "INSERT INTO user_details (name, pwrd_hint) VALUES (?, ?)"
        self.execute( sql_details, (account.name, account.pwrd_hint))
        print("Account created successfully")
        self.close()
        

import mysql.connector
from package.account_creator import Account



class dbConnect():
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = "198.12.124.54", 
            user = "joe", 
            password = "Egg.man264.",
            database = "user", 
            port = 3306)
        self.mycursor = self.conn.cursor()
        
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
        self.mycursor.execute(sql, params or ())
    
    def fetchall(self):
        return self.mycursor.fetchall()
    
    def fetchone(self):
        return self.mycursor.fetchone()
    
    def queryall(self, sql, params=None):
        self.mycursor.execute(sql, params or ())
        return self.fetchall()

    def queryone(self, sql, params=None):
        self.mycursor.execute(sql, params or ())
        return self.fetchone()
    
    def new_user(self, account: Account):
        sql_auth = "INSERT INTO user_auth (email, pwrd_hash) VALUES (%s, %s)"
        self.execute( sql=(sql_auth), params=(account.email, account.pwrd_hash))
        self.commit()
        sql_details = "INSERT INTO user_details (name, pwrd_hint) VALUES (%s, %s)"
        self.execute( sql=(sql_details), params=(account.name, account.pwrd_hint))
        print("Account created successfully")
        self.close()
    
    # function that checks if email is already in use
    def check_email(self, email):
        sql = "SELECT email FROM user_auth WHERE email = (%s)"
        self.execute(sql=(sql), params=(email,))
        if self.fetchone() is None:
            return False
        else:
            return True
        


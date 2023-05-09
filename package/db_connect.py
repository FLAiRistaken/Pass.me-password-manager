from mysql import connector
import json
import requests

from package.account_creator import Account
from package.cache_item import CacheItem




class DBConnect():
    def __init__(self):
        self.conn = connector.connect(
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

#class to make api requests to api.passme.fun:8000
class ApiConnect():
    #initializes the class with the api url
    def __init__(self):
        self.url = "http://api.passme.fun:8000"
        self.result_tokentype:str = None
        self.result_access_token:str = None
        self.result_refresh_token:str = None

        self.c = CacheItem()
        self.c.create_refresh_cache()


    def request_post(self, endpoint, headers=None, data=None, json=None):
        reponse = requests.post(self.url + endpoint, headers=headers, data=data, json=json, timeout=30)
        return reponse.json()

    def request_get(self, endpoint, headers=None, data=None, json=None):
        response = requests.get(self.url + endpoint, headers=headers, data=data, json=json, timeout=30)
        return response.json()

    def login_with_creds(self, email, pwrd_hash):
        data = {
            "grant_type": "password",
            "username": email,
            "password": pwrd_hash,
            "scope": "",
            "client_id": "",
            "client_secret": ""
        }

        response = self.request_post("/api/users/auth/login", data=data, headers={"Content-Type": "application/x-www-form-urlencoded", "accept": "application/json"})

        if response['access_token'] is not None:
            self.result_tokentype = response['token_type']
            self.result_access_token = response['access_token']
            self.result_refresh_token = response['refresh_token']

            self.c.add_refresh_token(self.result_refresh_token)
            print('Added refresh token to cache')
            return True
        else:
            return False

    def login_with_access_token(self):

        if self.result_access_token is None:
            if self.result_refresh_token is None:
                try:
                    self.result_refresh_token = self.c.get_refresh_token()
                    if self.result_refresh_token is not None:
                        print('Found refresh token in cache')
                        return self.refresh_tokens()
                except:
                    print('Refresh token error')
                    return False

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.result_access_token}"
        }

        response = self.request_post("/api/users/auth/login", headers=headers)

        if 'access_token' in response:
            self.result_tokentype = response['token_type']
            self.result_access_token = response['access_token']
            self.result_refresh_token = response['refresh_token']

            self.c.add_refresh_token(self.result_refresh_token)
            print('Added refresh token to cache')

            return True
        else:
            return self.refresh_tokens()

    def refresh_tokens(self):
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.result_refresh_token,
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = self.request_post("/api/users/auth/login", data=data, headers=headers)

        if 'access_token' in response:
            self.result_tokentype = response['token_type']
            self.result_access_token = response['access_token']
            self.result_refresh_token = response['refresh_token']

            self.c.add_refresh_token(self.result_refresh_token)
            print('Added refresh token to cache')

            return True
        else:
            return False


    #function to create a new user using Account class
    def new_user(self, account: Account):
        data = {
            "auth": {
                "email": account.email,
                "verified": 'false',
                "pwrd_hash": account.pwrd_hash
            },
            "details": {
                "name": account.name,
                "pwrd_hint": account.pwrd_hint
            }
        }

        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }

        response:dict = self.request_post("/api/users/create", json=data, headers=headers)

        if 'access_token' in response:
            self.result_tokentype = response['token_type']
            self.result_access_token = response['access_token']
            self.result_refresh_token = response['refresh_token']

            self.c.add_refresh_token(self.result_refresh_token)
            print('Added refresh token to cache')

            return True
        elif ('detail' in response):
            return False
        else:
            return False


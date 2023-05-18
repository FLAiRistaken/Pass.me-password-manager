from mysql import connector
import json
import requests

from package.cache_item import CacheItem
from package.model.Items import *
from package.account_creator import Account


#class to make api requests to api.passme.fun:8000
class ApiConnect():
    #initializes the class with the api url
    def __init__(self):
        self.url = "http://api.passme.fun:8000"
        #self.url = "http://127.0.0.1:8000"
        self.result_tokentype:str = None
        self.result_access_token:str = None
        self.result_refresh_token:str = None

        self.c = CacheItem()
        self.c.create_refresh_cache()


    def request_post(self, endpoint, headers=None, data=None, json=None):
        reponse = requests.post(self.url + endpoint, headers=headers, data=data, json=json, timeout=30)
        return reponse.json()

    def request_delete(self, endpoint, headers=None, data=None, json=None):
        response = requests.delete(self.url + endpoint, headers=headers, data=data, json=json, timeout=30)
        return response.json()

    def request_put(self, endpoint, headers=None, data=None, json=None):
        response = requests.put(self.url + endpoint, headers=headers, data=data, json=json, timeout=30)
        return response.json()

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

    def get_user_name(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.result_access_token}"
        }

        response = self.request_get("/api/users/details/get", headers=headers)

        if 'detail' in response:
            if response['detail'] == 'Token has expired' or response['detail'] == 'Could not validate credentials' or response['detail'] == 'Not authenticated':
                try:
                    if self.login_with_access_token():
                        return self.get_user_name_and_email()
                    else:
                        raise Exception('Could not authenticate')
                except:
                    raise Exception('Could not authenticate')
            else:
                raise Exception('Account not found')
        else:
            return response['name']

    def get_user_email(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.result_access_token}"
        }

        response = self.request_get("/api/users/auth/get", headers=headers)

        if 'detail' in response:
            if response['detail'] == 'Token has expired' or response['detail'] == 'Could not validate credentials' or response['detail'] == 'Not authenticated':
                try:
                    if self.login_with_access_token():
                        return self.get_user_name_and_email()
                    else:
                        raise Exception('Could not authenticate')
                except:
                    raise Exception('Could not authenticate')
            else:
                raise Exception('Account not found')
        else:
            return response['email']


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

    def change_password(self, old_password, new_password):
        data = {
            "old_password": old_password,
            "new_password": new_password
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.result_access_token}"
        }

        response = self.request_post("/api/users/auth/update", json=data, headers=headers)

        if 'detail' in response:
            if response['detail'] == 'Token has expired' or response['detail'] == 'Could not validate credentials' or response['detail'] == 'Not authenticated':
                try:
                    if self.login_with_access_token():
                        return self.get_user_name_and_email()
                    else:
                        raise Exception('Could not authenticate')
                except:
                    raise Exception('Could not authenticate')
            elif response.status_code == 401:
                raise Exception('Old password is incorrect')
            else:
                raise Exception('Account not found')
        else:
            return response

    def get_vault(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.result_access_token}"
        }

        response = self.request_get("/api/vaults", headers=headers)

        if 'detail' in response:
            if response['detail'] == 'Token has expired' or response['detail'] == 'Could not validate credentials' or response['detail'] == 'Not authenticated':
                try:
                    if self.login_with_access_token() == True:
                        return self.get_vault()
                except Exception:
                    return {'detail': 'Can not authenticate'}
        else:
            return response

    def get_vault_items(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.result_access_token}"
        }

        response = self.request_get("/api/vaults/items", headers=headers)

        if 'detail' in response:
            if response['detail'] == 'Token has expired' or response['detail'] == 'Could not validate credentials' or response['detail'] == 'Not authenticated':
                try:
                    if self.login_with_access_token() == True:
                        return self.get_vault_items()
                except Exception:
                    return {'detail': 'Can not authenticate'}
        else:
            return response

    def item_to_dict(self, item: GeneralItem):
        if isinstance(item, LoginItem):
            return {
                "name": item.name,
                "email": item.email,
                "password": item.password,
                "website": item.website,
                "date_created": item.date_created,
                "date_modified": item.date_modified,
                "notes": item.note,
                "folder": item.folder,
                "recently_deleted": item.recently_deleted,
                "favourite": item.favourite,
            }
        elif isinstance(item, BankAccItem):
            return {
                "name": item.name,
                "name_on_account": item.name_on_account,
                "account_number": item.account_number,
                "sort_code": item.sort_code,
                "date_created": item.date_created,
                "date_modified": item.date_modified,
                "notes": item.note,
                "folder": item.folder,
                "recently_deleted": item.recently_deleted,
                "favourite": item.favourite,
            }
        elif isinstance(item, BankCardItem):
            return {
                "name": item.name,
                "name_on_card": item.name_on_card,
                "card_number": item.card_number,
                "exp_month": int(item.exp_month),
                "exp_year": int(item.exp_year),
                "brand": item.brand,
                "cvv": int(item.cvv),
                "date_created": item.date_created,
                "date_modified": item.date_modified,
                "notes": item.note,
                "folder": item.folder,
                "recently_deleted": item.recently_deleted,
                "favourite": item.favourite,
            }
        elif isinstance(item, IdentityItem):
            return {
                "name": item.name,
                "title": item.title,
                "first_name": item.first_name,
                "last_name": item.last_name,
                "email": item.email,
                "phone_no": item.phone_number,
                "nat_insur_no": item.nat_insur_no,
                "pass_no": item.pass_no,
                "license_no": item.license_no,
                "date_created": item.date_created,
                "date_modified": item.date_modified,
                "notes": item.note,
                "folder": item.folder,
                "recently_deleted": item.recently_deleted,
                "favourite": item.favourite,
            }
        elif isinstance(item, SecureNoteItem):
            return {
                "name": item.name,
                "notes": item.note,
                "date_created": item.date_created,
                "date_modified": item.date_modified,
                "folder": item.folder,
                "recently_deleted": item.recently_deleted,
                "favourite": item.favourite,
            }
        else:
            raise ValueError("Item is not a valid type")

    def item_to_dict_url(self, item):
        if isinstance(item, LoginItem):
            url = "/api/vaults/items/login/"
            item_dict = self.item_to_dict(item)
        elif isinstance(item, BankAccItem):
            url = "/api/vaults/items/bank/"
            item_dict = self.item_to_dict(item)
        elif isinstance(item, BankCardItem):
            url = "/api/vaults/items/card/"
            item_dict = self.item_to_dict(item)
        elif isinstance(item, IdentityItem):
            url = "/api/vaults/items/identity/"
            item_dict = self.item_to_dict(item)
        elif isinstance(item, SecureNoteItem):
            url = "/api/vaults/items/note/"
            item_dict = self.item_to_dict(item)
        else:
            raise ValueError("Item is not a valid type")

        return (url, item_dict)

    def item_to_id(self, item):
        return self.c.get_item_id(item.name)


    def add_item_to_vault(self, item):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.result_access_token}"
        }

        url, item_dict = self.item_to_dict_url(item)

        item_dict.pop('favourite')
        item_dict.pop('recently_deleted')


        response = self.request_post(url, json=item_dict, headers=headers)

        if 'detail' in response:
            if response['detail'] == 'Token has expired' or response['detail'] == 'Could not validate credentials' or response['detail'] == 'Not authenticated':
                try:
                    if self.login_with_access_token() == True:
                        return self.add_item_to_vault(item)
                except Exception:
                    raise Exception('Could not authenticate')
        elif 'status' in response:
            if response['status'] == 'Ok':
                return response
            else:
                raise Exception('Could not add item')

    def toggle_recently_deleted(self, item):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.result_access_token}"
        }

        url, item_dict = self.item_to_dict_url(item)
        item_id = self.item_to_id(item)

        response = self.request_put(url + "recentlyd/" + item_id, headers=headers)

        if 'detail' in response:
            if response['detail'] == 'Token has expired' or response['detail'] == 'Could not validate credentials' or response['detail'] == 'Not authenticated':
                try:
                    if self.login_with_access_token() == True:
                        return self.add_to_recently_deleted(item)
                except Exception:
                    raise Exception('Could not authenticate')
            elif response['detail'] == "Not found":
                raise Exception('Item not found')
            else:
                raise Exception('Could not toggle recently_deleted status')
        elif 'status' in response:
            if response['status'] == 'Ok':
                return response
            else:
                raise Exception('Could not toggle recently_deleted status')

    def toggle_favourite(self, item):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.result_access_token}"
        }

        url, item_dict = self.item_to_dict_url(item)
        item_id = self.item_to_id(item)

        response = self.request_put(url + "favourite/" + item_id, headers=headers)

        if 'detail' in response:
            if response['detail'] == 'Token has expired' or response['detail'] == 'Could not validate credentials' or response['detail'] == 'Not authenticated':
                try:
                    if self.login_with_access_token() == True:
                        return self.add_to_recently_deleted(item)
                except Exception:
                    raise Exception('Could not authenticate')
            elif response['detail'] == "Not found":
                raise Exception('Item not found')
            else:
                raise Exception('Could not toggle recently_deleted status')
        elif 'status' in response:
            if response['status'] == 'Ok':
                return True
            else:
                raise Exception('Could not toggle favourite status')

    def delete_item(self, item):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.result_access_token}"
        }

        item_id = self.item_to_id(item)
        url, item_dict = self.item_to_dict_url(item)

        response = self.request_delete(url + item_id, headers=headers)

        if 'detail' in response:
            if response['detail'] == 'Token has expired' or response['detail'] == 'Could not validate credentials' or response['detail'] == 'Not authenticated':
                try:
                    if self.login_with_access_token() == True:
                        return self.delete_item(item)
                except Exception:
                    raise Exception('Could not authenticate')
            elif response['detail'] == "Not found":
                raise Exception('Item not found')
            else:
                raise Exception('Could not toggle recently_deleted status')
        elif 'status' in response:
            if response['status'] == 'Ok':
                return True
            else:
                raise Exception('Could not delete item')

    def update_item(self, item):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.result_access_token}"
        }

        item_id = self.item_to_id(item)

        url, item_dict = self.item_to_dict_url(item)

        response = self.request_put(url + item_id, json=item_dict, headers=headers)

        if 'detail' in response:
            if response['detail'] == 'Token has expired' or response['detail'] == 'Could not validate credentials' or response['detail'] == 'Not authenticated':
                try:
                    if self.login_with_access_token() == True:
                        return self.update_item(item)
                except Exception:
                    raise Exception('Could not authenticate')
            elif response['detail'] == "Not found":
                raise Exception('Item not found')
            else:
                raise Exception('Could not toggle recently_deleted status')
        elif 'status' in response:
            if response['status'] == 'Ok':
                return response
            else:
                raise Exception('Could not update item')




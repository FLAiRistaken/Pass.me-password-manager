import json
import time
from typing import Dict, Any

from package.model.Items import *


class CacheItem():
    def __init__(self):
        self.create_cache()

    # a function that creates a .json file if one doesnt already exist
    def create_cache(self):
        try:
            with open('cache.json', 'r') as f:
                print('Cache file found...')
        except FileNotFoundError:
            print('Cache file not found, creating a new one...')
            with open('cache.json', 'w') as f:
                json.dump({}, f)

    def create_refresh_cache(self):
        try:
            with open('refresh_cache.json', 'r') as f:
                print('Refresh Cache file found...')
        except FileNotFoundError:
            print('Refresh Cache file not found, creating a new one...')
            with open('refresh_cache.json', 'w') as f:
                json.dump({}, f)

    def clear_cache(self):
        with open('cache.json', 'w') as f:
            json.dump({}, f)

    def vault_to_cache(self, items: Dict[str, list[Dict[str, Any]]]):
        self.clear_cache()
        if items is None:
            raise Exception("No vault found, please contact support.")
        for item_type in items.items():
            if item_type[1].__len__() == 0:
                continue
            for item in item_type[1]:
                if item['recently_deleted'] == True:
                    item.update({'recently_deleted': True})
                    item.update({'recently_deleted_date': item['recently_deleted_date']})
                if item['favourite'] == True:
                    item.update({'favourite': True})
                if item_type[0] == "login_items":
                    item.update({'type': 'login'})
                elif item_type[0] == "bank_items":
                    item.update({'type': 'bank_acc'})
                elif item_type[0] == "card_items":
                    item.update({'type': 'bank_card'})
                elif item_type[0] == "identity_items":
                    item.update({'type': 'identity'})
                elif item_type[0] == "secure_note_items":
                    item.update({'type': 'secure_note'})

                self.add_item(item)

    # a function that turns an item into a dictionary
    def item_to_dict(self, item: GeneralItem):
        if isinstance(item, LoginItem):
            return {
                "id": item.id,
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
                "type": "login"
            }
        elif isinstance(item, BankAccItem):
            return {
                "id": item.id,
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
                "type": "bank_acc"
            }
        elif isinstance(item, BankCardItem):
            return {
                "id": item.id,
                "name": item.name,
                "name_on_card": item.name_on_card,
                "card_number": item.card_number,
                "exp_month": item.exp_month,
                "exp_year": item.exp_year,
                "brand": item.brand,
                "cvv": item.cvv,
                "date_created": item.date_created,
                "date_modified": item.date_modified,
                "notes": item.note,
                "folder": item.folder,
                "recently_deleted": item.recently_deleted,
                "favourite": item.favourite,
                "type": "bank_card"
            }
        elif isinstance(item, IdentityItem):
            return {
                "id": item.id,
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
                "type": "identity"
            }
        elif isinstance(item, SecureNoteItem):
            return {
                "id": item.id,
                "name": item.name,
                "notes": item.note,
                "date_created": item.date_created,
                "date_modified": item.date_modified,
                "folder": item.folder,
                "recently_deleted": item.recently_deleted,
                "favourite": item.favourite,
                "type": "secure_note"
            }
        else:
            return {
                "id": item.id,
                "name": item.name,
                "date_created": item.date_created,
                "date_modified": item.date_modified,
                "notes": item.note,
                "folder": item.folder,
                "recently_deleted": item.recently_deleted,
                "favourite": item.favourite,
                "type": "general"
            }

    # a function that adds an item to the cache
    def add_item(self, item):
        if isinstance(item, GeneralItem):
            with open('cache.json', 'r') as f:
                data = json.load(f)
            data[item.name] = self.item_to_dict(item)
            with open('cache.json', 'w') as f:
                json.dump(data, f)
                print (f'Item {item.name} added to cache...')
        else:
            with open('cache.json', 'r') as f:
                data = json.load(f)
            data[item['name']] = item
            with open('cache.json', 'w') as f:
                json.dump(data, f)
                print (f'Item {item["name"]} added to cache...')

    def add_refresh_token(self, token):
        with open('refresh_cache.json', 'r') as f:
            data = json.load(f)
        try:
            del data['refresh_token']
        except KeyError:
            pass
        data["refresh_token"] = token
        with open('refresh_cache.json', 'w') as f:
            json.dump(data, f)
            print (f'Refresh token added to cache...')

    def add_vkey(self, vkey):
        with open('refresh_cache.json', 'r') as f:
            data = json.load(f)
        try:
            del data['vkey']
        except KeyError:
            pass
        data["vkey"] = vkey.hex()
        with open('refresh_cache.json', 'w') as f:
            json.dump(data, f)
            print (f'Vault key added to cache...')

    def remove_vkey(self):
        with open('refresh_cache.json', 'r') as f:
            data = json.load(f)
        try:
            del data['vkey']
        except KeyError:
            pass
        with open('refresh_cache.json', 'w') as f:
            json.dump(data, f)
            print (f'Vault key removed from cache...')

    def get_vkey(self):
        with open('refresh_cache.json', 'r') as f:
            data = json.load(f)
        try:
            return bytes.fromhex(data["vkey"])
        except KeyError:
            raise Exception("No vault key found, please login using credentials.")

    def check_vkey_exists(self):
        with open('refresh_cache.json', 'r') as f:
            data = json.load(f)
        try:
            data["vkey"]
            return True
        except KeyError:
            raise Exception("No vault key found, please login using credentials.")


    # a function that removes an item from the cache
    def remove_item(self, item):
        with open('cache.json', 'r') as f:
            data = json.load(f)
        del data[item.name]
        with open('cache.json', 'w') as f:
            json.dump(data, f)
            print (f'Item {item.name} removed from cache...')

    def remove_refresh_token(self):
        with open('refresh_cache.json', 'r') as f:
            data = json.load(f)
        del data["refresh_token"]
        with open('refresh_cache.json', 'w') as f:
            json.dump(data, f)
            print (f'Refresh token removed from cache...')

    # a function that updates an item in the cache
    def update_item(self, item):
        self.remove_item(item)
        self.add_item(item)
        print (f'Item {item.name} updated in cache...')

    def update_token(self, token):
        self.remove_refresh_token()
        self.add_refresh_token(token)
        print (f'Refresh token updated in cache...')

    def get_refresh_token(self):
        with open('refresh_cache.json', 'r') as f:
            data = json.load(f)
        return data["refresh_token"]

    # a function that returns a list of all items in the cache
    def get_all_items(self):
        with open('cache.json', 'r') as f:
            data = json.load(f)
        items = []
        print(data)
        for item in data:
            if data[item]['recently_deleted'] == False:
                items.append(self.json_to_item(data[item]))

        return items

    def get_item(self, key):
        with open('cache.json', 'r') as f:
            data = json.load(f)
        return data[key]

    def search_items(self, search_term:str) -> list:
        with open('cache.json', 'r') as f:
            data = json.load(f)
        items = []
        for item in data:
            if data[item]['recently_deleted'] == False:
                if search_term.lower() in data[item]['name'].lower():
                    items.append(self.json_to_item(data[item]))
        return items

    def get_item_id(self, key):
        with open('cache.json', 'r') as f:
            data = json.load(f)
        return data[key]['id']

    def get_recently_deleted(self):
        with open('cache.json', 'r') as f:
            data = json.load(f)
        items = []
        for item in data:
            if data[item]['recently_deleted'] == True:
                items.append(self.json_to_item(data[item]))
        return items

    def get_favourites(self):
        with open('cache.json', 'r') as f:
            data = json.load(f)
        items = []
        for item in data:
            if data[item]["favourite"] == True:
                items.append(self.json_to_item(data[item]))
        return items

    def get_items_by_type(self, type):
        with open('cache.json', 'r') as f:
            data = json.load(f)
        items = []
        for item in data:
            if data[item]["type"] == type:
                items.append(self.json_to_item(data[item]))
        return items

    # a function that returns a list of all items in a folder
    def get_items_in_folder(self, folder):
        with open('cache.json', 'r') as f:
            data = json.load(f)
        items = []
        for item in data:
            if data[item]['folder'] == folder:
                items.append(self.json_to_item(data[item]))
        return items

    def json_to_item(self, item_json):
        match item_json["type"]:
            case "login":
                return LoginItem(item_json["name"], item_json["email"], item_json["password"],
                                 item_json["website"], item_json["date_created"],
                                 item_json["date_modified"], item_json["notes"], item_json["folder"], item_json["id"],
                                 item_json["recently_deleted"], item_json["favourite"])
            case "bank_acc":
                return BankAccItem(item_json["name"], item_json["name_on_account"], item_json["account_number"],
                                    item_json["sort_code"], item_json["date_created"], item_json["date_modified"],
                                    item_json["notes"], item_json["folder"], item_json["id"], item_json["recently_deleted"],
                                    item_json["favourite"])
            case "bank_card":
                return BankCardItem(item_json["name"], item_json["name_on_card"], item_json["card_number"],
                                    item_json["exp_month"], item_json["exp_year"], item_json["brand"],
                                    item_json["cvv"], item_json["date_created"], item_json["date_modified"],
                                    item_json["notes"], item_json["folder"], item_json["id"], item_json["recently_deleted"],
                                    item_json["favourite"])
            case "identity":
                return IdentityItem(item_json["name"], item_json["title"], item_json["first_name"],
                                    item_json["last_name"], item_json["email"], item_json["phone_no"],
                                    item_json["nat_insur_no"], item_json["pass_no"], item_json["license_no"],
                                    item_json["date_created"], item_json["date_modified"], item_json["notes"],
                                    item_json["folder"], item_json["id"], item_json["recently_deleted"], item_json["favourite"])
            case "secure_note":
                return SecureNoteItem(item_json["name"], item_json["date_created"], item_json["date_modified"], item_json["notes"],
                                      item_json["folder"], item_json["id"], item_json["recently_deleted"], item_json["favourite"])
            case "general":
                return GeneralItem(item_json["name"], item_json["date_created"], item_json["date_modified"],
                                   item_json["notes"], item_json["folder"], item_json["id"], item_json["recently_deleted"],
                                   item_json["favourite"])

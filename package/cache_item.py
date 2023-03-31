import json
import time
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

    # a function that turns an item into a dictionary
    def item_to_dict(self, item: GeneralItem):
        if isinstance(item, LoginItem):
            return {
                "name": item.name,
                "email": item.email,
                "password": item.password,
                "website": item.website,
                "date_created": item.date_created,
                "date_modified": item.date_modified,
                "note": item.note,
                "folder": item.folder,
                "type": "login"
            }
        elif isinstance(item, BankAccItem):
            return {
                "name": item.name,
                "name_on_account": item.name_on_account,
                "account_number": item.account_number,
                "sort_code": item.sort_code,
                "date_created": item.date_created,
                "date_modified": item.date_modified,
                "note": item.note,
                "folder": item.folder,
                "type": "bank_acc"
            }
        elif isinstance(item, BankCardItem):
            return {
                "name": item.name,
                "name_on_card": item.name_on_card,
                "card_number": item.card_number,
                "exp_month": item.exp_month,
                "exp_year": item.exp_year,
                "brand": item.brand,
                "cvv": item.cvv,
                "date_created": item.date_created,
                "date_modified": item.date_modified,
                "note": item.note,
                "folder": item.folder,
                "type": "bank_card"
            }
        elif isinstance(item, IdentityItem):
            return {
                "name": item.name,
                "title": item.title,
                "first_name": item.first_name,
                "last_name": item.last_name,
                "email": item.email,
                "phone_number": item.phone_number,
                "nat_insur_no": item.nat_insur_no,
                "pass_no": item.pass_no,
                "license_no": item.license_no,
                "date_created": item.date_created,
                "date_modified": item.date_modified,
                "note": item.note,
                "folder": item.folder,
                "type": "identity"
            }
        elif isinstance(item, SecureNoteItem):
            return {
                "name": item.name,
                "note": item.note,
                "date_created": item.date_created,
                "date_modified": item.date_modified,
                "folder": item.folder,
                "type": "secure_note"
            }
        else:
            return {
                "name": item.name,
                "date_created": item.date_created,
                "date_modified": item.date_modified,
                "note": item.note,
                "folder": item.folder,
                "type": "general"
            }

    # a function that adds an item to the cache
    def add_item(self, item):
        with open('cache.json', 'r') as f:
            data = json.load(f)
        data[item.name] = self.item_to_dict(item)
        with open('cache.json', 'w') as f:
            json.dump(data, f)
            print (f'Item {item.name} added to cache...')

    # a function that removes an item from the cache
    def remove_item(self, item):
        with open('cache.json', 'r') as f:
            data = json.load(f)
        del data[item.name]
        with open('cache.json', 'w') as f:
            json.dump(data, f)
            print (f'Item {item.name} removed from cache...')

    # a function that updates an item in the cache
    def update_item(self, item):
        self.remove_item(item)
        self.add_item(item)
        print (f'Item {item.name} updated in cache...')

    # a function that returns a list of all items in the cache
    def get_all_items(self):
        with open('cache.json', 'r') as f:
            data = json.load(f)
        items = []
        print(data)
        for item in data:
            items.append(self.json_to_item(data[item]))

        return items

    # a function that returns a list of all items in a folder
    def get_items_in_folder(self, folder):
        with open('cache.json', 'r') as f:
            data = json.load(f)
        items = []
        for item in data:
            if data[item]['folder'] == folder:
                items.append(self.json_to_item(item))
        return items

    def json_to_item(self, item_json):
        match item_json["type"]:
            case "login":
                return LoginItem(item_json["name"], item_json["email"], item_json["password"],
                                 item_json["website"], item_json["date_created"],
                                 item_json["date_modified"], item_json["note"], item_json["folder"])
            case "bank_acc":
                return BankAccItem(item_json["name"], item_json["name_on_account"], item_json["account_number"],
                                    item_json["sort_code"], item_json["date_created"], item_json["date_modified"],
                                    item_json["note"], item_json["folder"])
            case "bank_card":
                return BankCardItem(item_json["name"], item_json["name_on_card"], item_json["card_number"],
                                    item_json["exp_month"], item_json["exp_year"], item_json["brand"],
                                    item_json["cvv"], item_json["date_created"], item_json["date_modified"],
                                    item_json["note"], item_json["folder"])
            case "identity":
                return IdentityItem(item_json["name"], item_json["title"], item_json["first_name"],
                                    item_json["last_name"], item_json["email"], item_json["phone_number"],
                                    item_json["nat_insur_no"], item_json["pass_no"], item_json["license_no"],
                                    item_json["date_created"], item_json["date_modified"], item_json["note"],
                                    item_json["folder"])
            case "secure_note":
                return SecureNoteItem(item_json["name"], item_json["note"], item_json["date_created"],
                                        item_json["date_modified"], item_json["folder"])
            case "general":
                return GeneralItem(item_json["name"], item_json["date_created"], item_json["date_modified"],
                                   item_json["note"], item_json["folder"])
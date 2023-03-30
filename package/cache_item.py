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
            case "general":
                return GeneralItem(item_json["name"], item_json["date_created"], item_json["date_modified"],
                                   item_json["note"], item_json["folder"])
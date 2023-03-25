import json
import time
from package.model import Items


class CacheItem():
    def __init__(self, item: Items.GeneralItem):
        self.item = item

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
    def item_to_dict(self):
        if isinstance(self.item, Items.LoginItem):
            return {
                "name": self.item.name,
                "email": self.item.email,
                "password": self.item.password,
                "website": self.item.website,
                "date_created": self.item.date_created,
                "date_modified": self.item.date_modified,
                "note": self.item.note,
                "folder": self.item.folder
            }
        else:
            return {
                "name": self.item.name,
                "date_created": self.item.date_created,
                "date_modified": self.item.date_modified,
                "note": self.item.note,
                "folder": self.item.folder
            }

    # a function that adds an item to the cache
    def add_item(self):
        with open('cache.json', 'r') as f:
            data = json.load(f)
        data[self.item.name] = self.item_to_dict()
        with open('cache.json', 'w') as f:
            json.dump(data, f)
            print (f'Item {self.item.name} added to cache...')

    # a function that removes an item from the cache
    def remove_item(self):
        with open('cache.json', 'r') as f:
            data = json.load(f)
        del data[self.item.name]
        with open('cache.json', 'w') as f:
            json.dump(data, f)
            print (f'Item {self.item.name} removed from cache...')

    # a function that updates an item in the cache
    def update_item(self):
        self.remove_item()
        self.add_item()
        print (f'Item {self.item.name} updated in cache...')

    # a function that returns a list of all items in the cache
    def get_all_items(self):
        with open('cache.json', 'r') as f:
            data = json.load(f)
        items: Items.GeneralItem = []
        for item in data:
            items.append(item)
        return items

    # a function that returns a list of all items in a folder
    def get_items_in_folder(self, folder):
        with open('cache.json', 'r') as f:
            data = json.load(f)
        items: Items.GeneralItem = []
        for item in data:
            if data[item]['folder'] == folder:
                items.append(item)
        return items
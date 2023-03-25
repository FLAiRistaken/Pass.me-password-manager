import datetime

class GeneralItem():
    def __init__(self, name, date_created, date_modified, note=None, folder=None):
        self.name = name
        self.note = note
        self.folder = folder
        self.date_created = date_created
        self.date_modified = date_modified


class LoginItem(GeneralItem):
    def __init__(self, name, email, password, website, date_created, date_modified, note=None, folder=None):
        super().__init__(name, date_created, date_modified, note, folder)
        self.email = email
        self.password = password
        self.website = website

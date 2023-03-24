class GeneralItem():
    def __init__(self, note=None, folder=None):
        self.note = note
        self.folder = folder


class LoginItem(GeneralItem):
    def __init__(self, email=None, password=None, website=None, note=None, folder=None):
        super().__init__(note, folder)
        self.email = email
        self.password = password
        self.website = website
        self.note = note
        self.folder = folder

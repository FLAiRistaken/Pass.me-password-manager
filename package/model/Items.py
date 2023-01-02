class GeneralItem():
    def __init__(self, note=None, tags=None):
        self.note = note
        self.tags = tags


class LoginItem(GeneralItem):
    def __init__(self, email=None, password=None, website=None, note=None, tags=None):
        super().__init__(note, tags)
        self.email = email
        self.password = password
        self.website = website
        self.note = note
        self.tags = tags

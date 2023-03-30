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

class BankAccItem(GeneralItem):
    def __init__(self, name, name_on_account, account_number, sort_code, date_created, date_modified, note=None, folder=None):
        super().__init__(name, date_created, date_modified, note, folder)
        self.name_on_account = name_on_account
        self.account_number = account_number
        self.sort_code = sort_code

class BankCardItem(GeneralItem):
    def __init__(self, name, name_on_card, card_number, exp_month, exp_year, brand, cvv, date_created, date_modified, note=None, folder=None):
        super().__init__(name, date_created, date_modified, note, folder)
        self.name_on_card = name_on_card
        self.card_number = card_number
        self.exp_month = exp_month
        self.exp_year = exp_year
        self.brand = brand
        self.cvv = cvv

class IdentityItem(GeneralItem):
    def __init__(self, name, title, first_name, last_name, email, phone_number, nat_insur_no, pass_no, license_no, date_created, date_modified, note=None, folder=None):
        super().__init__(name, date_created, date_modified, note, folder)
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.nat_insur_no = nat_insur_no
        self.pass_no = pass_no
        self.license_no = license_no
        self.phone_number = phone_number
        self.email = email

class SecureNote(GeneralItem):
    def __init__(self, name, date_created, date_modified, note, folder=None):
        super().__init__(name, date_created, date_modified, note, folder)
        self.note = note
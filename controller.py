import datetime
import sys
import time
import json


from PySide6.QtCore import (QEasingCurve, QPropertyAnimation, QRect,
                            QRegularExpression, QSize, Qt, QTimer, Signal, Slot)
from PySide6.QtGui import (QFont, QPixmap, QRegularExpressionValidator,
                           QValidator, QClipboard, QAction)

from package.account_creator import Account, AccountCreator
from package.authenitcation import Authentication
from package.password_generator import GenPassword, GenPassphrase
from package.db_connect import ApiConnect
from package.mail import mail
from package.model.Items import *
from package.cache_item import CacheItem

from package.view import *

class Controller():
    def __init__(self):
        self.cache = CacheItem()
        self.api = ApiConnect()

        self.login = self.Login(self)
        self.create = self.Create(self)
        self.main_w = self.MainW(self)
        self.pass_gen = self.PassGen(self)
        self.msg_box = self.MessagegBox(self)
        self.list_item = self.ListI(self)

    def refresh_items(self):
        self.cache.vault_to_cache(self.api.get_vault_items())
        self.main_w.refresh_items()

    def refresh_faves(self):
        self.cache.vault_to_cache(self.api.get_vault_items())
        self.main_w.show_favourites(refresh=True)

    def fav_item(self, item):
        try:
            self.api.toggle_favourite(item)
        except Exception as e:
            return False
        else:
            self.refresh_faves()
            return True


    class Login(LoginWindow):
        def __init__(self, controller = None):
            super().__init__()
            self.is_error_box_shown = False
            self.controller:Controller = controller

            # button connects to functions, allows button presses to function
            self.btnCreate.clicked.connect(self.show_create)
            self.btnLogin.clicked.connect(self.login_button)
            self.btnHint.clicked.connect(self.hint_clicked)
            self.btnClose.clicked.connect(sys.exit)
            self.btnBack.clicked.connect(self.back_clicked)
            # self.btnGetHint.clicked.connect(self.send_hint)

            QTimer.singleShot(0, self.token_login)

        def show_error_box(self, text=None):
            self.error_box.show()
            self.lblError.setText(text)
            anim = QPropertyAnimation(self.error_box, b"geometry", self.widget)
            anim.setStartValue(QRect(280, 600, 491, 45))
            anim.setEndValue(QRect(280, 650, 491, 45))
            anim.setDuration(400)
            anim.setEasingCurve(QEasingCurve.InOutCubic)
            self.is_error_box_shown = True
            anim.start()

        def hide_error_box(self):
            anim = QPropertyAnimation(self.error_box, b"geometry", self.widget)
            anim.setStartValue(QRect(280, 650, 491, 45))
            anim.setEndValue(QRect(280, 600, 491, 45))
            anim.setDuration(400)
            anim.setEasingCurve(QEasingCurve.InOutCubic)
            self.is_error_box_shown = False
            anim.start()

        def show_create(self, checked):
            self.controller.create.show()
            self.hide()

        def hint_clicked(self):
            self.rightBox.setEnabled(False)
            self.rightBox.hide()
            self.rightBox_Hint.setEnabled(True)
            self.rightBox_Hint.show()

        def back_clicked(self):
            self.rightBox_Hint.setEnabled(False)
            self.rightBox_Hint.hide()
            self.rightBox.setEnabled(True)
            self.rightBox.show()

        # function to send verification email
        def send_hint(self):
            m = mail()
            m.send_mail("    ", "Verification Code", "Your verification code is: ")
            QtWidgets.QMessageBox.information(
                self,
                "Verification Code Sent",
                "A verification code has been sent to your email",
            )

        def token_login(self):
            auth = Authentication(self.controller.api)
            token_auth = auth.auth_with_tokens()
            if token_auth is False:
                self.show_error_box("Failed to authenticate, please use login credentials.")
            else:
                print("Logging in...")
                self.controller.refresh_items()
                self.main_window = self.controller.main_w
                self.main_window.show()
                self.hide()

        def login_button(self):
            # m = mail()
            emailval = self.lineEdit_Email.text()
            passval = self.lineEdit_MastPassword.text()
            auth = Authentication(self.controller.api, emailval, passval).authenticate()
            if auth is True:
                print("Logging in...")
                self.controller.refresh_items()
                #  m.sendMail("flairx@protonmail.com", "Logged into pass.me",
                #              ("Logged into pass.me at: " + str(datetime.datetime.now)))
                self.main_window = self.controller.main_w
                self.main_window.show()
                self.hide()
            else:
                self.show_error_box("Failed to authenticate")


    class Create(CreateWindow):
        def __init__(self, controller = None):
            super().__init__()
            self.is_error_box_shown = False
            self.controller:Controller = controller

            rx_email = QRegularExpression("[^@]+@[^@]+\.[^@]+")
            le_email_validator = QRegularExpressionValidator(rx_email)
            self.lineEdit_Email.setValidator(le_email_validator)
            self.lineEdit_Email.textChanged.connect(self.email_changed)

            rx_pass = QRegularExpression(
                "((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{12,64})"
            )
            le_password_validator = QRegularExpressionValidator(rx_pass)
            self.lineEdit_MastPassword.setValidator(le_password_validator)
            self.lineEdit_MastPassword.textChanged.connect(self.password_changed)
            self.lineEdit_MastPassword2.textChanged.connect(self.password_verify_changed)

            self.btnCreate.setEnabled(False)

            self.btnLogin.clicked.connect(self.show_login)
            self.btnCreate.clicked.connect(self.createAccButton)
            self.btnClose.clicked.connect(sys.exit)

            self.lineEditGreen = (
                "background-color: rgba(55, 184, 29, 100);\n"
                "border-radius:6px;\n"
                "padding-bottom:1px;\n"
                "padding-left:3px"
            )
            self.lineEditRed = (
                "background-color: rgba(255, 0, 0, 100);\n"
                "border-radius:6px;\n"
                "padding-bottom:1px;\n"
                "padding-left:3px"
            )

        # function that animates error_box to slide down when called
        def show_error_box(self, text=None):
            self.errror_box.show()
            self.lblError.setText(text)
            anim = QPropertyAnimation(self.errror_box, b"geometry", self.widget)
            anim.setStartValue(QRect(280, 600, 491, 45))
            anim.setEndValue(QRect(280, 650, 491, 45))
            anim.setDuration(400)
            anim.setEasingCurve(QEasingCurve.InOutCubic)
            self.is_error_box_shown = True
            anim.start()

        def hide_error_box(self):
            anim = QPropertyAnimation(self.errror_box, b"geometry", self.widget)
            anim.setStartValue(QRect(280, 650, 491, 45))
            anim.setEndValue(QRect(280, 600, 491, 45))
            anim.setDuration(400)
            anim.setEasingCurve(QEasingCurve.InOutCubic)
            self.is_error_box_shown = False
            anim.start()

        def email_changed(self):
            if self.lineEdit_Email.hasAcceptableInput():
                self.lineEdit_Email.setToolTip("Valid Email")
                self.lineEdit_Email.setStyleSheet(self.lineEditGreen)
                self.check_fields()
                if self.is_error_box_shown is True:
                    self.hide_error_box()
            else:
                if self.is_error_box_shown:
                    self.lblError.setText(
                        "Invalid Email. Please use an email with correct format"
                    )
                else:
                    self.show_error_box(
                        "Invalid Email. Please use an email with correct format"
                    )
                self.lineEdit_Email.setToolTip("Invalid Email")
                self.lineEdit_Email.setStyleSheet(self.lineEditRed)
                self.btnCreate.setEnabled(False)

        def password_changed(self):
            if self.lineEdit_MastPassword.hasAcceptableInput():
                self.lineEdit_MastPassword.setToolTip("Valid Password")
                self.lineEdit_MastPassword.setStyleSheet(self.lineEditGreen)
                self.check_fields()
                if self.is_error_box_shown is True:
                    self.hide_error_box()
            else:
                if self.is_error_box_shown:
                    self.lblError.setText(
                        "Invalid Password. Please use a password that contains 12 characters,\nat least 1 uppercase letter, 1 lowercase letter, 1 number, and 1 special character"
                    )
                else:
                    self.show_error_box(
                        "Invalid Password. Please use a password that contains 12 characters,\nat least 1 uppercase letter, 1 lowercase letter, 1 number, and 1 special character"
                    )
                self.lineEdit_MastPassword.setToolTip("Invalid Password")
                self.lineEdit_MastPassword.setStyleSheet(self.lineEditRed)
                self.btnCreate.setEnabled(False)

        def password_verify_changed(self):
            if self.lineEdit_MastPassword2.text() == self.lineEdit_MastPassword.text():
                self.lineEdit_MastPassword2.setToolTip("Passwords Match")
                self.lineEdit_MastPassword2.setStyleSheet(self.lineEditGreen)
                self.check_fields()
                if self.is_error_box_shown is True:
                    self.hide_error_box()
            else:
                if self.is_error_box_shown:
                    self.lblError.setText(
                        "Entered passwords do not match. Please try again"
                    )
                else:
                    self.show_error_box("Entered passwords do not match. Please try again")
                self.lineEdit_MastPassword2.setToolTip("Passwords Do Not Match")
                self.lineEdit_MastPassword2.setStyleSheet(self.lineEditRed)
                self.btnCreate.setEnabled(False)

        # function to check each field for valid input and then enable the create account button
        def check_fields(self):
            if (
                self.lineEdit_Email.hasAcceptableInput()
                and self.lineEdit_MastPassword.hasAcceptableInput()
                and self.lineEdit_MastPassword2.text() == self.lineEdit_MastPassword.text()
            ):
                self.btnCreate.setEnabled(True)
                if self.is_error_box_shown is True:
                    self.hide_error_box()
            else:
                self.btnCreate.setEnabled(False)

        def show_login(self, checked):
            self.w = LoginWindow()
            self.w.show()
            self.close()

        def createAccButton(self):
            api = self.controller.api
            emailval = self.lineEdit_Email.text().lower()
            passval = self.lineEdit_MastPassword.text()
            nameval = self.lineEdit_Name.text()
            hintval = self.lineEdit_PassHint.text()
            ac = AccountCreator(emailval, passval, nameval, hintval)
            if api.new_user(ac):
                self.w = LoginWindow()
                self.w.show()
                self.close()
            else:

                self.show_error_box("That email is already in use. Please use a different email.")



    class MainW(MainWindow):
        def __init__(self, controller = None):
            super().__init__()
            self.controller:Controller = controller
            self.faves_display = False

            self.btnGenerator.clicked.connect(self.show_generator)
            self.btnNew.clicked.connect(self.show_new_item_screen)
            self.lvItems.currentItemChanged.connect(self.show_item_details)
            self.btnFavorites.clicked.connect(self.show_favourites)
            self.btnAll_Items.clicked.connect(self.refresh_items)
            self.btnRecently_Deleted.clicked.connect(self.show_recently_deleted)
            self.comboCategories.currentIndexChanged.connect(self.sort_by_type)

            self.add_profile_menu_actions()


            self.cache = self.controller.cache
            self.sort_by_type()

        def add_profile_menu_actions(self):
            settings = QAction("Settings", self)
            logout = QAction("Logout", self)
            app_exit = QAction("Exit", self)

            logout.triggered.connect(self.logout)
            app_exit.triggered.connect(sys.exit)

            self.btnProfile.addAction(settings)
            self.btnProfile.addAction(logout)
            self.btnProfile.addAction(app_exit)

        def logout(self):
            self.cache.remove_refresh_token()
            self.w = self.controller.login
            self.w.show()
            self.hide()

        def show_generator(self):
            self.w = self.controller.pass_gen
            self.w.show()

        def show_new_item_screen(self):
            self.w = self.controller.NewItemCont(controller=self.controller)
            self.w.add_widget(self.controller.NewItem(controller=self.controller, parent=self.w))
            self.w.show()

        def add_item_to_list(self, item):
            list_item = self.controller.ListI()
            list_item.set_text(item.name, "Testing")
            q_list_item = QListWidgetItem(self.lvItems)
            q_list_item.setSizeHint(QSize(150, 60))
            self.lvItems.addItem(q_list_item)
            self.lvItems.setItemWidget(q_list_item, list_item)

        # function to add list of items to the list view
        def add_item_list_to_list(self, items):
            for item in items:
                self.add_item_to_list(item)

        def refresh_items(self):
            self.faves_display = False
            self.comboCategories.setCurrentIndex(0)
            self.clear_item_details()
            self.lvItems.clear()
            self.cached_items_list = self.cache.get_all_items()
            self.add_item_list_to_list(self.cached_items_list)

        def show_favourites(self, refresh:bool=False):
            if refresh is True and self.faves_display is True:
                self.lvItems.clear()
                self.clear_item_details()
                self.cached_items_list = self.cache.get_favourites()
                self.add_item_list_to_list(self.cached_items_list)
            elif refresh is True and self.faves_display is False:
                self.cached_items_list = self.cache.get_all_items()
            else:
                self.faves_display = True
                self.comboCategories.setCurrentIndex(0)
                self.lvItems.clear()
                self.clear_item_details()
                self.cached_items_list = self.cache.get_favourites()
                self.add_item_list_to_list(self.cached_items_list)

        def sort_by_type(self):
            self.faves_display = False
            combo_text = self.comboCategories.currentText()
            match combo_text:
                case "All Categories":
                    self.refresh_items()
                    return
                case "Logins":
                    item_type = "login"
                case "Identities":
                    item_type = "identity"
                case "Bank cards":
                    item_type = "bank_card"
                case "Bank accounts":
                    item_type = "bank_account"
                case "Secure notes":
                    item_type = "secure_note"

            self.clear_item_details()
            self.lvItems.clear()
            self.cached_items_list = self.controller.cache.get_items_by_type(item_type)
            self.add_item_list_to_list(self.cached_items_list)

        def show_recently_deleted(self):
            self.lvItems.clear()
            self.clear_item_details()
            self.cached_items_list = self.cache.get_recently_deleted()
            self.add_item_list_to_list(self.cached_items_list)

        def clear_item_details(self):
            old_widget = self.right_box.layout().itemAt(0).widget()
            self.right_box.layout().replaceWidget(old_widget, QWidget())
            old_widget.deleteLater()

        def show_item_details(self):
            if self.lvItems.currentItem() is not None:
                item = self.cached_items_list[self.lvItems.currentIndex().row()]
                item_details = self.get_item_type(item)
                item_details.set_item_details()
                old_widget = self.right_box.layout().itemAt(0).widget()
                self.right_box.layout().replaceWidget(old_widget, item_details)
                old_widget.deleteLater()
                item_details.show()

        def get_item_type(self, item):
            # using isinstance, determine the type of item and return it
            if isinstance(item, LoginItem):
                return self.controller.LoginDetails(controller=self.controller, item=item)
            elif isinstance(item, BankAccItem):
                return self.controller.BankDetails(controller=self.controller, item=item)
            elif isinstance(item, BankCardItem):
                return self.controller.CardDetails(controller=self.controller, item=item)
            elif isinstance(item, IdentityItem):
                return self.controller.IdentityDetails(controller=self.controller, item=item)
            elif isinstance(item, SecureNoteItem):
                return self.controller.NoteDetails(controller=self.controller, item=item)

        def item_list_clicked(self):
            self.show_item_details()


    class ListI(ListItem):
        def __init__(self, controller = None):
            super().__init__()
            self.controller:Controller = controller

        def set_text(self, name, details):
            self.lbl_Item_Name.setText(name)
            self.lbl_Item_Details.setText(details)


    class PassGen(PasswordGeneratorWidget):
        def __init__(self, controller=None):
            super().__init__()
            self.controller:Controller = controller
            self.clipboard = QApplication.clipboard()

            self.check_radios()
            self.generate()

            self.btnClose.clicked.connect(self.close_self)
            self.rad_password.clicked.connect(self.check_radios)
            self.rad_passphrase.clicked.connect(self.check_radios)
            self.rad_password.clicked.connect(self.generate)
            self.rad_passphrase.clicked.connect(self.generate)
            self.btn_gen_pass.clicked.connect(self.generate)
            self.btn_copy.clicked.connect(self.copy_to_clipboard)

        def close_self(self):
            self.hide()

        def copy_to_clipboard(self):
            text = self.le_password.text()
            self.clipboard.clear()
            self.clipboard.setText(text)
            self.msg_box.set_text("Copied to Clipboard ✓")
            self.msg_box.show()
            timer = QTimer(self)
            timer.singleShot(2000, lambda: self.msg_box.hide())

        def check_radios(self):
            if self.rad_password.isChecked():
                if self.gridLayout_3.count() > 3:
                    old_widget = self.gridLayout_3.itemAt(3).widget()
                    self.gridLayout_3.replaceWidget(self.gridLayout_3.itemAt(3).widget(), self.controller.PassOpt())
                    old_widget.deleteLater()
                    self.set_event_listeners()
                else:
                    self.gridLayout_3.addWidget(self.controller.PassOpt())
                    self.set_event_listeners()
            elif self.rad_passphrase.isChecked():
                if self.gridLayout_3.count() > 3:
                    old_widget = self.gridLayout_3.itemAt(3).widget()
                    self.gridLayout_3.replaceWidget(self.gridLayout_3.itemAt(3).widget(), self.controller.PhraseOpt())
                    old_widget.deleteLater()
                    self.set_event_listeners()
                else:
                    self.gridLayout_3.addWidget(self.controller.PhraseOpt())
                    self.set_event_listeners()

        def set_event_listeners(self):
            for i in self.gridLayout_3.itemAt(3).widget().children()[0].children():
                if isinstance(i, QCheckBox):
                    i.clicked.connect(self.generate)
                elif isinstance(i, QComboBox):
                    i.currentIndexChanged.connect(self.generate)
                elif isinstance(i, QSlider):
                    i.valueChanged.connect(self.generate)

        def get_values(self):
            return self.gridLayout_3.itemAt(3).widget().get_values()

        def generate(self):
            if self.rad_password.isChecked():
                password = GenPassword(*self.get_values()).generate_password()
                self.le_password.setText(password)
                self.add_to_list(password, str(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')))
            elif self.rad_passphrase.isChecked():
                passphrase = GenPassphrase(*self.get_values()).generate_passphrase()
                self.le_password.setText(passphrase)
                self.add_to_list(passphrase, str(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')))

        def add_to_list(self, password: str, date: str):
            pass_item = self.controller.PassHistItem()
            pass_item.set_text(password, date)
            q_list_item = QListWidgetItem(self.listWidget)
            q_list_item.setSizeHint(QSize(200, 60))
            self.listWidget.addItem(q_list_item)
            self.listWidget.setItemWidget(q_list_item, pass_item)


    class PassOpt(PasswordOptions):
        def __init__(self, controller=None):
            super().__init__()
            self.controller:Controller = controller

        def get_values(self) -> tuple[int, bool, bool, bool]:
            return self.slide_len.value(), self.chk_nums.isChecked(), self.chk_spec.isChecked(), self.chk_capitals.isChecked()

        def check_fields(self):
            if (self.slide_len.valueChanged or self.chk_spec.clicked or self.chk_nums.clicked or self.chk_capitals.clicked):
                return True


    class PhraseOpt(PassphraseOptions):
        def __init__(self, controller=None):
            super().__init__()
            self.controller:Controller = controller

        def get_values(self) -> tuple[int, str, bool, bool]:
            return self.slide_word_no.value(), self.combo_separator.currentText(), self.chk_num.isChecked(), self.chk_capitalise.isChecked()

        def check_fields(self):
            if (self.slide_word_no.valueChanged or self.combo_separator.currentIndexChanged or self.chk_num.clicked or self.chk_capitalise.clicked):
                return True


    class PassHistItem(PassHistListItem):
        def __init__(self, controller=None):
            super().__init__()
            self.controller:Controller = controller

        def set_text(self, password: str, date: str):
            self.lbl_password.setText(password)
            self.lbl_gen_date.setText(date)


    class NewItemCont(NewItemWidgetContainer):
        def __init__(self, controller=None):
            super().__init__()
            self.controller:Controller = controller
            self.msg_box:Controller.MessagegBox = self.controller.msg_box
            self.original_size = self.size()

        def orig_size(self):
            self.resize(self.original_size)

        def add_widget(self, widget: QWidget):
                self.resize(widget.size())
                self.layout().addWidget(widget)

        def display_msg_box(self, text: str):
            self.msg_box.set_text(text)
            self.msg_box.show_message()


    class NewItem(NewItemScreen):
        def __init__(self, controller=None, parent=None):
            super().__init__(parent)
            self.controller:Controller = controller

            self.btnClose.clicked.connect(self.close_self)
            self.btn_item_login.clicked.connect(self.show_login)
            self.btn_item_bank_acc.clicked.connect(self.show_bank_acc)
            self.btn_item_bank_card.clicked.connect(self.show_bank_card)
            self.btn_item_identity.clicked.connect(self.show_identity)
            self.btn_item_note.clicked.connect(self.show_secure_note)

        def show_login(self):
            print ("Loading new login item screen...")
            self.w = self.controller.NewLogin(controller=self.controller, parent=self.parent())
            self.parent().add_widget(self.w)
            self.hide()

        def show_bank_acc(self):
            print ("Loading new bank account item screen...")
            self.w = self.controller.NewBank(controller=self.controller, parent=self.parent())
            self.parent().add_widget(self.w)
            self.hide()

        def show_bank_card(self):
            print ("Loading new bank card item screen...")
            self.w = self.controller.NewCard(controller=self.controller, parent=self.parent())
            self.parent().add_widget(self.w)
            self.hide()

        def show_identity(self):
            print ("Loading new identity item screen...")
            self.w = self.controller.NewIdentity(controller=self.controller, parent=self.parent())
            self.parent().add_widget(self.w)
            self.hide()

        def show_secure_note(self):
            print ("Loading new secure note item screen...")
            self.w = self.controller.NewNote(controller=self.controller, parent=self.parent())
            self.parent().add_widget(self.w)
            self.hide()

        def close_self(self):
            self.parent().close()
            self.parent().deleteLater()
            self.deleteLater()


    class NewLogin(NewLoginItemScreen):
        def __init__(self, controller=None, parent=None):
            super().__init__(parent)
            self.controller:Controller = controller

            self.btn_back.clicked.connect(self.show_new_item_screen)
            self.btn_save.clicked.connect(self.save_item)

        def show_new_item_screen(self):
            self.hide()
            self.parent().orig_size()
            self.parent().findChild(NewItemScreen).show()

        def save_item(self):
            name = self.le_name.text()
            email = self.le_email.text()
            password = self.le_password.text()
            website = self.le_website.text()
            notes = self.te_notes.toPlainText()
            folder = self.combo_folders.currentText()

            if (name == "" and (email == "" or password == "" or website == "" or notes == "")):
                self.parent().display_msg_box("Please enter a name\n and fill at least other 1 field")
                return

            curr_date = str(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
            item = LoginItem(name, email, password, website, curr_date, curr_date, notes, folder)


            try:
                self.controller.api.add_item_to_vault(item)
            except Exception as e:
                print(e)
                self.parent().display_msg_box(e.args[0])
                return

            cache = self.controller.cache
            cache.add_item(item)

            self.controller.main_w.refresh_items()

            self.parent().display_msg_box("Item saved ✓")

            self.parent().close()


    class NewCard(NewBankCardItemScreen):
        def __init__(self, controller=None, parent=None):
            super().__init__(parent)
            self.controller:Controller = controller

            self.btn_back.clicked.connect(self.show_new_item_screen)
            self.btn_save.clicked.connect(self.save_item)

        def show_new_item_screen(self):
            self.hide()
            self.parent().findChild(NewItemScreen).show()

        def save_item(self):
            name = self.le_name.text()
            name_on_card = self.le_name_on_card.text()
            card_number = self.le_card_number.text()
            brand = self.combo_brand.currentText()
            exp_month = self.combo_exp_month.currentText()
            exp_year = self.combo_exp_year.currentText()
            cvv = self.le_cvv.text()
            notes = self.te_notes.toPlainText()
            folder = self.combo_folders.currentText()

            curr_date = str(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
            item = BankCardItem(name, name_on_card, card_number, exp_month, exp_year, brand, cvv, curr_date, curr_date, notes, folder)

            try:
                self.controller.api.add_item_to_vault(item)
            except Exception as e:
                print(e)
                self.parent().display_msg_box(e.args[0])
                return

            cache = self.controller.cache
            cache.add_item(item)

            self.controller.main_w.refresh_items()

            self.parent().display_msg_box("Item saved ✓")

            self.parent().close()


    class NewBank(NewBankAccItemScreen):
        def __init__(self, controller=None, parent=None):
            super().__init__(parent)
            self.controller:Controller = controller

            self.btn_back.clicked.connect(self.show_new_item_screen)
            self.btn_save.clicked.connect(self.save_item)

        def show_new_item_screen(self):
            self.hide()
            self.parent().findChild(NewItemScreen).show()

        def save_item(self):
            name = self.le_name.text()
            name_on_account = self.le_acc_name.text()
            account_number = self.le_account_number.text()
            sort_code = self.le_sortcode.text()
            notes = self.te_notes.toPlainText()
            folder = self.combo_folders.currentText()

            curr_date = str(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
            item = BankAccItem(name, name_on_account, account_number, sort_code, curr_date, curr_date, notes, folder)


            try:
                self.controller.api.add_item_to_vault(item)
            except Exception as e:
                print(e)
                self.parent().display_msg_box(e.args[0])
                return

            cache = self.controller.cache
            cache.add_item(item)

            self.controller.main_w.refresh_items()

            self.parent().display_msg_box("Item saved ✓")

            self.parent().close()


    class NewIdentity(NewIdentityItemScreen):
        def __init__(self, controller=None, parent=None):
            super().__init__(parent)
            self.controller:Controller = controller

            self.btn_back.clicked.connect(self.show_new_item_screen)
            self.btn_save.clicked.connect(self.save_item)

        def show_new_item_screen(self):
            self.hide()
            self.parent().findChild(NewItemScreen).show()

        def save_item(self):
            name = self.le_name.text()
            title = self.combo_title.currentText()
            first_name = self.le_first_name.text()
            last_name = self.le_surname.text()
            email = self.le_email.text()
            phone = self.le_phone.text()
            nat_insur_no = self.le_nat_insur.text()
            passport_no = self.le_pass_num.text()
            license_no = self.le_license_num.text()
            notes = self.te_notes.toPlainText()

            curr_date = str(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
            item = IdentityItem(name, title, first_name, last_name, email, phone, nat_insur_no, passport_no, license_no, curr_date, curr_date, notes, folder=None)

            try:
                self.controller.api.add_item_to_vault(item)
            except Exception as e:
                print(e)
                self.parent().display_msg_box(e.args[0])
                return

            cache = self.controller.cache
            cache.add_item(item)

            self.controller.main_w.refresh_items()

            self.parent().display_msg_box("Item saved ✓")

            self.parent().close()


    class NewNote(NewSecureNoteItemScreen):
        def __init__(self, controller=None, parent=None):
            super().__init__(parent)
            self.controller:Controller = controller

            self.btn_back.clicked.connect(self.show_new_item_screen)
            self.btn_save.clicked.connect(self.save_item)

        def show_new_item_screen(self):
            self.hide()
            self.parent().findChild(NewItemScreen).show()

        def save_item(self):
            name = self.le_name.text()
            notes = self.te_notes.toPlainText()
            folder = self.combo_folders.currentText()

            curr_date = str(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))

            item = SecureNoteItem(name, curr_date, curr_date, notes, folder)

            try:
                self.controller.api.add_item_to_vault(item)
            except Exception as e:
                print(e)
                self.parent().display_msg_box(e.args[0])
                return

            cache = self.controller.cache
            cache.add_item(item)

            self.controller.main_w.refresh_items()

            self.parent().display_msg_box("Item saved ✓")

            self.parent().close()


    class LoginDetails(LoginItemDetails):
        def __init__(self, controller=None, item=None):
            super().__init__()
            self.controller:Controller = controller
            self.item:LoginItem = item
            self.btn_fav_style = self.btn_fav.styleSheet()
            self.fav = self.item.favourite

            self.toggle_fav_style()

            self.btn_fav.clicked.connect(self.api_fav)

        def set_item_details(self):
            self.lbl_item_name.setText(self.item.name)
            self.le_email.setText(self.item.email)
            self.le_password.setText(self.item.password)
            self.le_website.setText(self.item.website)
            self.te_notes.setText(self.item.note)
            self.combo_folders.setCurrentText(self.item.folder)
            self.lbl_create_value.setText(self.item.date_created)
            self.lbl_modified_value.setText(self.item.date_modified)

        def toggle_fav_style(self):
            if self.fav:
                self.btn_fav.setText("★")
                self.btn_fav.setObjectName("btn_fav")
                self.btn_fav.setStyleSheet("#btn_fav {background-color: rgba(152, 108, 144, 140);} #btn_fav:hover {background-color: rgba(152, 108, 144, 115)}")
            else:
                self.btn_fav.setText("☆")
                self.btn_fav.setStyleSheet(self.btn_fav_style)

        def toggle_fav(self):
            if self.fav:
                self.fav = False
                self.toggle_fav_style()
            else:
                self.fav = True
                self.toggle_fav_style()

        def api_fav(self):
            if self.controller.fav_item(self.item):
                self.toggle_fav()
            else:
                self.controller.msg_box.set_text("Error: Could not favourite item")
                self.controller.msg_box.show_message()


    class CardDetails(BankCardItemDetails):
        def __init__(self, controller=None, item=None):
            super().__init__()
            self.controller:Controller = controller
            self.item:BankCardItem = item
            self.btn_fav_style = self.btn_fav.styleSheet()
            self.fav = self.item.favourite

            self.toggle_fav_style()

            self.btn_fav.clicked.connect(self.api_fav)

        def set_item_details(self):
            self.lbl_item_name.setText(self.item.name)
            self.le_name_on_card.setText(self.item.name_on_card)
            self.le_card_number.setText(self.item.card_number)
            self.combo_exp_month.setCurrentText(self.item.exp_month)
            self.combo_exp_year.setCurrentText(self.item.exp_year)
            self.combo_brand.setCurrentText(self.item.brand)
            self.le_cvv.setText(self.item.cvv)
            self.te_notes.setText(self.item.note)
            self.combo_folders.setCurrentText(self.item.folder)

        def toggle_fav_style(self):
            if self.fav:
                self.btn_fav.setText("★")
                self.btn_fav.setObjectName("btn_fav")
                self.btn_fav.setStyleSheet("#btn_fav {background-color: rgba(152, 108, 144, 140);} #btn_fav:hover {background-color: rgba(152, 108, 144, 115)}")
            else:
                self.btn_fav.setText("☆")
                self.btn_fav.setStyleSheet(self.btn_fav_style)

        def toggle_fav(self):
            if self.fav:
                self.fav = False
                self.toggle_fav_style()
            else:
                self.fav = True
                self.toggle_fav_style()

        def api_fav(self):
            if self.controller.fav_item(self.item):
                self.toggle_fav()
            else:
                self.controller.msg_box.set_text("Error: Could not favourite item")
                self.controller.msg_box.show_message()


    class BankDetails(BankAccItemDetails):
        def __init__(self, controller=None, item=None):
            super().__init__()
            self.controller:Controller = controller
            self.item:BankAccItem = item
            self.btn_fav_style = self.btn_fav.styleSheet()
            self.fav = self.item.favourite

            self.toggle_fav_style()

            self.btn_fav.clicked.connect(self.api_fav)

        def set_item_details(self):
            self.lbl_item_name.setText(self.item.name)
            self.le_acc_name.setText(self.item.name_on_account)
            self.le_acc_no.setText(self.item.account_number)
            self.le_sortcode.setText(self.item.sort_code)
            self.te_notes.setText(self.item.note)
            self.combo_folders.setCurrentText(self.item.folder)

        def toggle_fav_style(self):
            if self.fav:
                self.btn_fav.setText("★")
                self.btn_fav.setObjectName("btn_fav")
                self.btn_fav.setStyleSheet("#btn_fav {background-color: rgba(152, 108, 144, 140);} #btn_fav:hover {background-color: rgba(152, 108, 144, 115)}")
            else:
                self.btn_fav.setText("☆")
                self.btn_fav.setStyleSheet(self.btn_fav_style)

        def toggle_fav(self):
            if self.fav:
                self.fav = False
                self.toggle_fav_style()
            else:
                self.fav = True
                self.toggle_fav_style()

        def api_fav(self):
            if self.controller.fav_item(self.item):
                self.toggle_fav()
            else:
                self.controller.msg_box.set_text("Error: Could not favourite item")
                self.controller.msg_box.show_message()


    class IdentityDetails(IdentityItemDetails):
        def __init__(self, controller=None, item=None):
            super().__init__()
            self.controller:Controller = controller
            self.item:IdentityItem = item
            self.btn_fav_style = self.btn_fav.styleSheet()
            self.fav = self.item.favourite

            self.toggle_fav_style()

            self.btn_fav.clicked.connect(self.api_fav)

        def set_item_details(self):
            self.lbl_item_name.setText(self.item.name)
            self.combo_title.setCurrentText(self.item.title)
            self.le_first_name.setText(self.item.first_name)
            self.le_surname.setText(self.item.last_name)
            self.le_email.setText(self.item.email)
            self.le_phone_no.setText(self.item.phone_number)
            self.le_nat_insur_no.setText(self.item.nat_insur_no)
            self.le_pass_no.setText(self.item.pass_no)
            self.le_license_no.setText(self.item.license_no)
            self.te_notes.setText(self.item.note)

        def toggle_fav_style(self):
            if self.fav:
                self.btn_fav.setText("★")
                self.btn_fav.setObjectName("btn_fav")
                self.btn_fav.setStyleSheet("#btn_fav {background-color: rgba(152, 108, 144, 140);} #btn_fav:hover {background-color: rgba(152, 108, 144, 115)}")
            else:
                self.btn_fav.setText("☆")
                self.btn_fav.setStyleSheet(self.btn_fav_style)

        def toggle_fav(self):
            if self.fav:
                self.fav = False
                self.toggle_fav_style()
            else:
                self.fav = True
                self.toggle_fav_style()

        def api_fav(self):
            if self.controller.fav_item(self.item):
                self.toggle_fav()
            else:
                self.controller.msg_box.set_text("Error: Could not favourite item")
                self.controller.msg_box.show_message()


    class NoteDetails(SecureNoteDetails):
        def __init__(self, controller=None, item=None):
            super().__init__()
            self.controller:Controller = controller
            self.item:SecureNoteItem = item
            self.btn_fav_style = self.btn_fav.styleSheet()
            self.fav = self.item.favourite

            self.toggle_fav_style()

            self.btn_fav.clicked.connect(self.api_fav)

        def set_item_details(self):
            self.lbl_item_name.setText(self.item.name)
            self.te_notes.setText(self.item.note)
            self.combo_folders.setCurrentText(self.item.folder)

        def toggle_fav_style(self):
            if self.fav:
                self.btn_fav.setText("★")
                self.btn_fav.setObjectName("btn_fav")
                self.btn_fav.setStyleSheet("#btn_fav {background-color: rgba(152, 108, 144, 140);} #btn_fav:hover {background-color: rgba(152, 108, 144, 115)}")
            else:
                self.btn_fav.setText("☆")
                self.btn_fav.setStyleSheet(self.btn_fav_style)

        def toggle_fav(self):
            if self.fav:
                self.fav = False
                self.toggle_fav_style()
            else:
                self.fav = True
                self.toggle_fav_style()

        def api_fav(self):
            if self.controller.fav_item(self.item):
                self.toggle_fav()
            else:
                self.controller.msg_box.set_text("Error: Could not favourite item")
                self.controller.msg_box.show_message()




    class MessagegBox(MsgBox):
        def __init__(self, controller=None):
            super().__init__()
            self.controller:Controller = controller

        def set_text(self, text: str):
            self.lbl_msg.setText(text)

        def show_message(self):
            self.show()
            timer = QTimer(self)
            timer.singleShot(2000, lambda: self.hide())

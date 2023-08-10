import datetime
import sys
import time
import json


from PySide6.QtCore import (QEasingCurve, QPropertyAnimation, QRect,
                            QRegularExpression, QSize, Qt, QTimer, Signal, Slot, QPoint)
from PySide6.QtGui import (QFont, QPixmap, QRegularExpressionValidator,
                           QValidator, QClipboard, QAction, QIcon)
from PySide6.QtWidgets import (QMessageBox)
from zxcvbn import zxcvbn
from package.account_creator import Account, AccountCreator
from package.authenitcation import Authentication, PasswordHasher
from package.password_generator import GenPassword, GenPassphrase
from package.db_connect import ApiConnect
from package.mail import mail
from package.model.Items import *
from package.cache_item import CacheItem
from package.encryption import Encrypt

from package.view import *

class Controller():
    def __init__(self):
        self.cache = CacheItem()
        self.api = ApiConnect()
        self.enc = Encrypt()

        self.login = self.Login(self)
        self.create = self.Create(self)
        self.main_w = self.MainW(self)
        self.pass_gen = self.PassGen(self)
        self.msg_box = self.MessagegBox(self)
        self.list_item = self.ListI(self)
        self.settings = self.SettingsW(self)

    def refresh_items(self):
        self.cache.vault_to_cache(self.api.get_vault_items())
        self.main_w.refresh_items()

    def refresh_faves(self):
        self.cache.vault_to_cache(self.api.get_vault_items())
        self.main_w.show_favourites(refresh=True)

    def refresh_cache(self):
        self.cache.vault_to_cache(self.api.get_vault_items())
        self.main_w.soft_refresh()

    def background_cache_refresh(self):
        self.cache.vault_to_cache(self.api.get_vault_items())

    def change_password(self, old_pass:str, new_pass:str):
        old_pass_hash = PasswordHasher(self.settings.user_email, old_pass).password_hashing(old_pass.encode('utf-8'), self.settings.user_email.encode('utf-8'))
        new_pass_hash = PasswordHasher(self.settings.user_email, new_pass).password_hashing(new_pass.encode('utf-8'), self.settings.user_email.encode('utf-8'))
        new_vkey = self.enc.create_encrypted_vault_key(PasswordHasher(self.settings.user_email, new_pass).generate_mkey(new_pass.encode('utf-8'), self.settings.user_email.encode('utf-8')), self.settings.user_email)
        try:
            self.api.change_password(old_pass_hash, new_pass_hash, new_vkey[0].hex(), new_vkey[1].hex())
        except Exception as e:
            if e == "Old password is incorrect":
                self.settings.display_msg_box("Old password is incorrect")
                return False
            else:
                self.settings.display_msg_box("An error occurred while changing\n your password. Please try again later.")
                return False
        else:
            self.cache.remove_refresh_token()
            return True

    def check_mast_pass_matches(self, password):
        pass_hash = PasswordHasher(self.settings.user_email, password).password_hashing(password.encode('utf-8'), self.settings.user_email.encode('utf-8'))
        try:
            if self.api.check_password(pass_hash) == "Incorrect password":
                return False
            else:
                return True
        except Exception as e:
            return False


    def delete_account(self):
        try:
            self.api.delete_account()
        except Exception as e:
            self.settings.display_msg_box("An error occurred while deleting\n your account. Please try again later.")
            return False
        else:
            self.cache.remove_refresh_token()
            return True

    def fav_item(self, item):
        try:
            self.api.toggle_favourite(item)
        except Exception as e:
            return False
        else:
            self.background_cache_refresh()
            self.main_w.refresh_item_details()
            return True

    def add_to_recently_deleted(self, item):
        try:
            self.api.toggle_recently_deleted(item)
        except Exception as e:
            return False
        else:
            if self.main_w.curr_display == "Recently Deleted":
                self.background_cache_refresh()
                self.main_w.refresh()
                return True
            else:
                self.background_cache_refresh()
                self.main_w.refresh()
                return True

    def create_q_message_box(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        return msg.exec_()

    def show_settings(self):
        try:
            user_name = self.api.get_user_name()
        except Exception as e:
            self.msg_box.set_text(str(e))
            self.msg_box.show()
            return
        try:
            user_email = self.api.get_user_email()
        except Exception as e:
            self.msg_box.set_text(str(e))
            self.msg_box.show()
            return

        if user_email == "" or user_email == None:
            self.msg_box.set_text("An error occurred while getting your account details. Please try again later.")
            self.msg_box.show()
            return

        if user_name == "" or user_name == None:
            self.settings.user_name = "Hello User!"
            self.settings.user_email = user_email
        else:
            self.settings.user_name = "Hello, " + user_name
            self.settings.user_email = user_email

        self.settings.set_user_details()
        self.settings.show()

    def perm_delete(self, item):
        yesno = self.create_q_message_box("Are you sure?", f"You are about to delete {item.name} permanently. This action cannot be undone. Are you sure you want to continue?")
        if yesno == QMessageBox.Yes:
            try:
                self.api.delete_item(item)
            except Exception as e:
                return False
            else:
                self.background_cache_refresh()
                self.main_w.refresh_recently_deleted()
                return True


    def edit_item(self, item):
        try:
            self.api.update_item(item)
        except Exception as e:
            return False
        else:
            self.refresh_cache()
            return True

    def card_exp_month_converter_str(self, month):
        match month:
            case "01 - January":
                return "01"
            case "02 - February":
                return "02"
            case "03 - March":
                return "03"
            case "04 - April":
                return "04"
            case "05 - May":
                return "05"
            case "06 - June":
                return "06"
            case "07 - July":
                return "07"
            case "08 - August":
                return "08"
            case "09 - September":
                return "09"
            case "10 - October":
                return "10"
            case "11 - November":
                return "11"
            case "12 - December":
                return "12"
            case _:
                return "00"

    def card_exp_month_converter_num(self, month):
        match month:
            case "1":
                return "01 - January"
            case "2":
                return "02 - February"
            case "3":
                return "03 - March"
            case "4":
                return "04 - April"
            case "5":
                return "05 - May"
            case "6":
                return "06 - June"
            case "7":
                return "07 - July"
            case "8":
                return "08 - August"
            case "9":
                return "09 - September"
            case "10":
                return "10 - October"
            case "11":
                return "11 - November"
            case "12":
                return "12 - December"
            case _:
                return "00"

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
            self.lineEdit_Email.textChanged.connect(self.hide_error_box)
            self.lineEdit_MastPassword.textChanged.connect(self.hide_error_box)
            # self.btnGetHint.clicked.connect(self.send_hint)

            QTimer.singleShot(0, self.token_login)

        def reset_fields(self):
            self.lineEdit_Email.clear()
            self.lineEdit_MastPassword.clear()
            self.lblError_2.clear()
            self.hide_error_box()

        def show_error_box(self, text=None):
            self.error_box.show()
            self.lblError_2.setText(text)
            anim = QPropertyAnimation(self.error_box, b"geometry", self.widget)
            anim.setStartValue(QRect(290, 356, 491, 45))
            anim.setEndValue(QRect(290, 383, 491, 45))
            anim.setDuration(400)
            anim.setEasingCurve(QEasingCurve.InOutCubic)
            self.is_error_box_shown = True
            anim.start()

        def hide_error_box(self):
            if not self.is_error_box_shown:
                return
            anim = QPropertyAnimation(self.error_box, b"geometry", self.widget)
            anim.setStartValue(QRect(290, 383, 491, 45))
            anim.setEndValue(QRect(290, 346, 491, 45))
            anim.setDuration(400)
            anim.setEasingCurve(QEasingCurve.InOutCubic)
            self.is_error_box_shown = False
            anim.start()

        def show_create(self):
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

        def clear_fields(self):
            self.lineEdit_Email.clear()
            self.lineEdit_MastPassword.clear()

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
            self.controller.msg_box.set_text("Logging in with tokens...")
            self.controller.msg_box.show_message()
            auth = Authentication(self.controller.api)
            token_auth = auth.auth_with_tokens()
            if token_auth is False:
                self.show_error_box("Failed to authenticate, please use login credentials.")
            else:
                self.show_error_box("Logging in...")
                try:
                    self.controller.refresh_items()
                except Exception as e:
                    self.show_error_box(str(e))
                    return

                self.main_window = self.controller.main_w
                self.main_window.set_profile_name()
                self.main_window.show()
                self.hide()

        def login_button(self):
            emailval = self.lineEdit_Email.text()
            passval = self.lineEdit_MastPassword.text()
            auth = False
            if emailval == "" or passval == "":
                self.show_error_box("Please enter your email and password")
                return
            try:
                auth = Authentication(self.controller.api, emailval, passval).authenticate()
            except Exception as e:
                self.show_error_box(str(e))
                return
            if auth is True:
                self.show_error_box("Logging in...")
                try:
                    self.controller.refresh_items()
                except Exception as e:
                    self.show_error_box(str(e))
                    return
                #  m.sendMail("flairx@protonmail.com", "Logged into pass.me",
                #              ("Logged into pass.me at: " + str(datetime.datetime.now)))
                self.main_window = self.controller.main_w
                self.main_window.set_profile_name()
                self.main_window.show()
                self.clear_fields()
                self.hide()
            elif auth is False:
                self.show_error_box("Login failed. Please try again.")


    class Create(CreateWindow):
        def __init__(self, controller = None):
            super().__init__()
            self.is_error_box_shown = False
            self.controller:Controller = controller

            rx_email = QRegularExpression("[^@]+@[^@]+\.[^@]+")
            le_email_validator = QRegularExpressionValidator(rx_email)
            self.lineEdit_Email.setValidator(le_email_validator)
            self.lineEdit_Email.textChanged.connect(self.email_changed)
            self.passStrengthBar.setValue(0)

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

            self.icon_visible = QIcon()
            self.icon_notvisible = QIcon()
            self.icon_visible.addFile(u":/create_acc/eye-visible.png", QSize(), QIcon.Normal, QIcon.Off)
            self.icon_notvisible.addFile(u":/create_acc/eye-notvisible.png", QSize(), QIcon.Normal, QIcon.On)
            self.btn_show_pass.clicked.connect(self.toggle_password_visibility)

            self.lineEditDefault = self.lineEdit_Email.styleSheet()
            self.lineEditDefault_pass = self.lineEdit_MastPassword.styleSheet()
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
            self.lineEditGreen_pass = (
                "background-color: rgba(55, 184, 29, 100);\n"
                "border-top-left-radius:6px;\n"
                "border-bottom-left-radius:6px;\n"
                "padding-bottom:1px;\n"
                "padding-left:3px"
            )
            self.lineEditRed_pass = (
                "background-color: rgba(255, 0, 0, 100);\n"
                "border-top-left-radius:6px;\n"
                "border-bottom-left-radius:6px;\n"
                "padding-bottom:1px;\n"
                "padding-left:3px"
            )

        def toggle_password_visibility(self):
            if self.lineEdit_MastPassword.echoMode() == QLineEdit.Password:
                self.lineEdit_MastPassword.setEchoMode(QLineEdit.Normal)
                self.btn_show_pass.setIcon(self.icon_notvisible)
            else:
                self.lineEdit_MastPassword.setEchoMode(QLineEdit.Password)
                self.btn_show_pass.setIcon(self.icon_visible)

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
            self.password_verify_changed()
            result = zxcvbn(self.lineEdit_MastPassword.text())
            score = result.get("score")
            self.passStrengthBar.setValue(100/4*score)
            if self.lineEdit_MastPassword.hasAcceptableInput():
                self.lineEdit_MastPassword.setToolTip("Valid Password")
                self.lineEdit_MastPassword.setStyleSheet(self.lineEditGreen_pass)
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
                self.lineEdit_MastPassword.setStyleSheet(self.lineEditRed_pass)
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

        def show_login(self):
            self.w = self.controller.login
            self.clear_fields()
            self.w.show()
            self.hide()

        def clear_fields(self):
            self.lineEdit_Email.clear()
            self.lineEdit_MastPassword.clear()
            self.lineEdit_MastPassword2.clear()
            self.lineEdit_Name.clear()
            self.lineEdit_PassHint.clear()
            self.lineEdit_Email.setStyleSheet(self.lineEditDefault)
            self.lineEdit_MastPassword.setStyleSheet(self.lineEditDefault_pass)
            self.btn_show_pass.setIcon(self.icon_visible)
            self.lineEdit_MastPassword.setEchoMode(QLineEdit.Password)
            self.lineEdit_MastPassword2.setStyleSheet(self.lineEditDefault)
            self.hide_error_box()

        def createAccButton(self):
            api = self.controller.api
            emailval = self.lineEdit_Email.text().lower()
            passval = self.lineEdit_MastPassword.text()
            nameval = self.lineEdit_Name.text()
            hintval = self.lineEdit_PassHint.text()
            ac = AccountCreator(emailval, passval, nameval, hintval).acc
            if api.new_user(ac):
                self.controller.login.show()
                self.hide()
                self.controller.msg_box.set_text("Account created successfully!")
                self.controller.msg_box.show()
            else:

                self.show_error_box("That email is already in use. Please use a different email.")


    class MainW(MainWindow):
        def __init__(self, controller = None):
            super().__init__()
            self.controller:Controller = controller
            self.btn_inactive = self.btnAll_Items.styleSheet()
            self.btn_active = "#btn_active {background-color: rgba(152, 108, 144, 140);} #btn_active:hover {background-color: rgba(152, 108, 144, 115)}"
            self.curr_display = "All Items"

            self.btnGenerator.clicked.connect(self.show_generator)
            self.btnNew.clicked.connect(self.show_new_item_screen)
            self.lvItems.currentItemChanged.connect(self.show_item_details)
            self.btnFavorites.clicked.connect(self.show_favourites)
            self.btnAll_Items.clicked.connect(self.show_all_items)
            self.btnRecently_Deleted.clicked.connect(self.show_recently_deleted)
            self.comboCategories.currentIndexChanged.connect(self.sort_by_type)
            self.lineEdit_Search.textChanged.connect(self.search)
            self.btn_business.clicked.connect(self.show_business_folder)
            self.btn_education.clicked.connect(self.show_education_folder)
            self.btn_entertainment.clicked.connect(self.show_entertainment_folder)
            self.btn_finance.clicked.connect(self.show_finance_folder)
            self.btn_games.clicked.connect(self.show_games_folder)
            self.btn_email.clicked.connect(self.show_email_folder)
            self.btn_social.clicked.connect(self.show_social_folder)


            self.add_profile_menu_actions()
            self.set_active_button()

            self.cache = self.controller.cache
            self.refresh()

        def search(self):
            search_text = self.lineEdit_Search.text()

            if search_text == "":
                self.refresh()
                return

            items = self.controller.cache.search_items(search_text)
            if items.__len__() == 0:
                self.lvItems.clear()
                return
            else:
                self.clear_item_details()
                self.lvItems.clear()
                self.add_item_list_to_list(items)


        def add_profile_menu_actions(self):
            settings = QAction("Settings", self)
            logout = QAction("Logout", self)
            app_exit = QAction("Exit", self)

            logout.triggered.connect(self.logout)
            app_exit.triggered.connect(sys.exit)
            settings.triggered.connect(self.show_settings)

            self.btnProfile.addAction(settings)
            self.btnProfile.addAction(logout)
            self.btnProfile.addAction(app_exit)

        def set_profile_name(self):
            name = self.controller.api.get_user_name()
            if name != "" or name is not None:
                self.btnProfile.setText(f"  Hello,  {name}")
            else:
                self.btnProfile.setText("  Hello, User")


        def logout(self):
            self.cache.remove_refresh_token()
            self.controller.api.clear_results()
            self.w = self.controller.login
            self.w.show()
            self.hide()

        def show_generator(self):
            self.curr_display = "Generator"
            self.set_active_button()
            self.w = self.controller.pass_gen
            self.w.show()

        def show_new_item_screen(self):
            self.w = self.controller.NewItemCont(controller=self.controller)
            self.w.add_widget(self.controller.NewItem(controller=self.controller, parent=self.w))
            self.w.show()

        def add_item_to_list(self, item):
            list_item = self.controller.ListI()
            list_item.set_text(item.name, item.date_modified[:10])
            q_list_item = QListWidgetItem(self.lvItems)
            q_list_item.setSizeHint(QSize(150, 60))
            self.lvItems.addItem(q_list_item)
            self.lvItems.setItemWidget(q_list_item, list_item)

        # function to add list of items to the list view
        def add_item_list_to_list(self, items):
            for item in items:
                self.add_item_to_list(item)

        def soft_refresh(self):
            self.lvItems.clear()
            self.cached_items_list = self.cache.get_all_items()
            self.add_item_list_to_list(self.cached_items_list)

        def refresh_items(self):
            self.curr_display = "All Items"
            self.comboCategories.setCurrentIndex(0)
            self.clear_item_details()
            self.lvItems.clear()
            self.cached_items_list = self.cache.get_all_items()
            self.add_item_list_to_list(self.cached_items_list)

        def refresh_recently_deleted(self):
            self.curr_display = "Recently Deleted"
            self.comboCategories.setCurrentIndex(0)
            self.clear_item_details()
            self.lvItems.clear()
            self.cached_items_list = self.cache.get_recently_deleted()
            self.add_item_list_to_list(self.cached_items_list)

        def refresh_item_details(self):
            index = self.lvItems.currentIndex()
            self.lvItems.clearSelection()
            self.lvItems.setCurrentIndex(index)


        def refresh(self):
            match self.curr_display:
                case "All Items":
                    self.refresh_items()
                case "Recently Deleted":
                    self.show_recently_deleted()
                case "Favourites":
                    self.show_favourites()
                case "Logins":
                    self.sort_by_type()
                case "Bank cards":
                    self.sort_by_type()
                case "Bank accounts":
                    self.sort_by_type()
                case "Secure notes":
                    self.sort_by_type()
                case "Identities":
                    self.sort_by_type()

        def set_active_button(self):
            self.btnAll_Items.setStyleSheet(self.btn_inactive)
            self.btnFavorites.setStyleSheet(self.btn_inactive)
            self.btnRecently_Deleted.setStyleSheet(self.btn_inactive)
            self.btnGenerator.setStyleSheet(self.btn_inactive)
            self.btn_business.setStyleSheet(self.btn_inactive)
            self.btn_education.setStyleSheet(self.btn_inactive)
            self.btn_social.setStyleSheet(self.btn_inactive)
            self.btn_email.setStyleSheet(self.btn_inactive)
            self.btn_entertainment.setStyleSheet(self.btn_inactive)
            self.btn_finance.setStyleSheet(self.btn_inactive)
            self.btn_games.setStyleSheet(self.btn_inactive)
            self.btnAll_Items.setObjectName("btnAll_Items")
            self.btnFavorites.setObjectName("btnFavorites")
            self.btnRecently_Deleted.setObjectName("btnRecently_Deleted")
            self.btnGenerator.setObjectName("btnGenerator")
            self.btn_business.setObjectName("btn_business")
            self.btn_education.setObjectName("btn_education")
            self.btn_social.setObjectName("btn_social")
            self.btn_email.setObjectName("btn_email")
            self.btn_entertainment.setObjectName("btn_entertainment")
            self.btn_finance.setObjectName("btn_finance")
            self.btn_games.setObjectName("btn_games")
            match self.curr_display:
                case "All Items":
                    self.btnAll_Items.setObjectName("btn_active")
                    self.btnAll_Items.setStyleSheet(self.btn_active)
                case "Recently Deleted":
                    self.btnRecently_Deleted.setObjectName("btn_active")
                    self.btnRecently_Deleted.setStyleSheet(self.btn_active)
                case "Favourites":
                    self.btnFavorites.setObjectName("btn_active")
                    self.btnFavorites.setStyleSheet(self.btn_active)
                case "Generator":
                    self.btnGenerator.setObjectName("btn_active")
                    self.btnGenerator.setStyleSheet(self.btn_active)
                case "Business":
                    self.btn_business.setObjectName("btn_active")
                    self.btn_business.setStyleSheet(self.btn_active)
                case "Education":
                    self.btn_education.setObjectName("btn_active")
                    self.btn_education.setStyleSheet(self.btn_active)
                case "Social":
                    self.btn_social.setObjectName("btn_active")
                    self.btn_social.setStyleSheet(self.btn_active)
                case "Email":
                    self.btn_email.setObjectName("btn_active")
                    self.btn_email.setStyleSheet(self.btn_active)
                case "Entertainment":
                    self.btn_entertainment.setObjectName("btn_active")
                    self.btn_entertainment.setStyleSheet(self.btn_active)
                case "Finance":
                    self.btn_finance.setObjectName("btn_active")
                    self.btn_finance.setStyleSheet(self.btn_active)
                case "Games":
                    self.btn_games.setObjectName("btn_active")
                    self.btn_games.setStyleSheet(self.btn_active)

        def show_all_items(self):
            self.curr_display = "All Items"
            self.set_active_button()
            self.refresh()

        def show_favourites(self, refresh:bool=False):
            if refresh is True and self.curr_display_display == "Favourites":
                self.lvItems.clear()
                self.clear_item_details()
                self.cached_items_list = self.cache.get_favourites()
                self.add_item_list_to_list(self.cached_items_list)
            elif refresh is True and self.curr_display_display != "Favourites":
                self.cached_items_list = self.cache.get_all_items()
            else:
                self.curr_display = "Favourites"
                self.set_active_button()
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
                    self.curr_display = "All Items"
                    self.refresh_items()
                    return
                case "Logins":
                    self.curr_display = "Logins"
                    item_type = "login"
                case "Identities":
                    self.curr_display = "Identities"
                    item_type = "identity"
                case "Bank cards":
                    self.curr_display = "Bank cards"
                    item_type = "bank_card"
                case "Bank accounts":
                    self.curr_display = "Bank accounts"
                    item_type = "bank_account"
                case "Secure notes":
                    self.curr_display = "Secure notes"
                    item_type = "secure_note"

            self.clear_item_details()
            self.lvItems.clear()
            self.cached_items_list = self.controller.cache.get_items_by_type(item_type)
            self.add_item_list_to_list(self.cached_items_list)

        def sort_by_folder(self, folder):
            self.faves_display = False
            self.curr_display = folder
            self.set_active_button()
            self.clear_item_details()
            self.lvItems.clear()
            self.cached_items_list = self.controller.cache.get_items_in_folder(folder)
            self.add_item_list_to_list(self.cached_items_list)

        def show_business_folder(self):
            self.sort_by_folder("Business")

        def show_education_folder(self):
            self.sort_by_folder("Education")

        def show_social_folder(self):
            self.sort_by_folder("Social")

        def show_email_folder(self):
            self.sort_by_folder("Email")

        def show_entertainment_folder(self):
            self.sort_by_folder("Entertainment")

        def show_finance_folder(self):
            self.sort_by_folder("Finance")

        def show_games_folder(self):
            self.sort_by_folder("Games")

        def show_recently_deleted(self):
            self.curr_display = "Recently Deleted"
            self.set_active_button()
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

        def show_settings(self):
            self.curr_display = "Settings"
            self.set_active_button()
            self.controller.show_settings()


    class SettingsW(SettingsWidget):
        def __init__(self, controller=None):
            super().__init__()
            self.controller:Controller = controller
            self.msg_box:Controller.MessagegBox = self.controller.msg_box
            self.user_name = ""
            self.user_email = ""

            self.btn_general.setEnabled(False)
            self.btn_chg_email.setEnabled(False)

            self.show_acc_settings()
            self.set_user_details()

            rx_pass = QRegularExpression(
                "((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{12,64})"
            )
            le_password_validator = QRegularExpressionValidator(rx_pass)
            self.le_new_pass.setValidator(le_password_validator)

            self.btn_account.clicked.connect(self.show_acc_settings)
            self.btn_close.clicked.connect(self.close_event)
            self.btn_logout.clicked.connect(self.controller.main_w.logout)
            self.btn_chg_pass.clicked.connect(self.show_pass_change)
            self.btn_chg_email.clicked.connect(self.show_email_change)
            self.btn_back_email.clicked.connect(self.show_acc_settings)
            self.btn_back_pass.clicked.connect(self.show_acc_settings)
            self.btn_back_del.clicked.connect(self.show_acc_settings)
            self.btn_back_conf_del.clicked.connect(self.show_acc_settings)
            self.btn_del_acc.clicked.connect(self.show_delete_account)
            self.btn_change_pass.clicked.connect(self.check_pass_fields)
            self.btn_del_acc_2.clicked.connect(self.del_acc_check_pass)
            self.btn_conf_del.clicked.connect(self.delete_account)

        def del_acc_check_pass(self):
            entered_pass = self.le_pass_del_acc.text()
            if entered_pass == "":
                self.display_msg_box("Please enter your password")
                return
            if self.controller.check_mast_pass_matches(entered_pass) is False:
                self.display_msg_box("Incorrect password")
                return
            self.show_conf_delete_account()

        def delete_account(self):
            if self.le_conf_del.text() == "":
                self.display_msg_box("Please type 'delete' to confirm account deletion")
                return
            if self.le_conf_del.text() != "delete":
                self.display_msg_box("Incorrect confirmation text")
                return
            if self.controller.delete_account() is False:
                return
            self.display_msg_box("Account successfully deleted")
            self.clear_fields()
            self.hide()
            self.controller.main_w.logout()



        def change_password(self):
            old_pass = self.le_old_pass.text()
            new_pass = self.le_new_pass.text()
            ver_pass = self.le_new_pass_ver.text()

            if old_pass == "" or new_pass == "" or ver_pass == "":
                self.display_msg_box("Please fill in all fields")
                return

            if new_pass != ver_pass:
                self.display_msg_box("New passwords do not match")
                return

            if not self.controller.change_password(old_pass, new_pass):
                return

            self.clear_fields()

            self.msg_box.show_message("Password successfully changed!")

        def check_pass_fields(self):
            if self.le_old_pass != "" and self.le_new_pass.hasAcceptableInput() and self.le_new_pass_ver != "":
                if self.le_new_pass.text() == self.le_new_pass_ver.text():
                    self.change_password()
                else:
                    self.display_msg_box("New passwords do not match")
            elif self.le_new_pass.hasAcceptableInput():
                self.display_msg_box("Please fill in all fields")
            else:
                self.display_msg_box("Ensure password meets requirements:\n - 12-64 characters\n - 1 uppercase\n - 1 lowercase\n - 1 number\n - 1 special character")


        def set_user_details(self):
            self.lbl_user_name.setText(self.user_name)
            self.lbl_user_email.setText(self.user_email)
            self.lbl_user_name_pass_reset.setText(self.user_name)
            self.lbl_user_email_pass_reset.setText(self.user_email)
            self.lbl_user_name_email_reset.setText(self.user_name)
            self.lbl_user_email_email_reset.setText(self.user_email)
            self.lbl_user_name_del_acc.setText(self.user_name)
            self.lbl_user_email_del_acc.setText(self.user_email)
            self.lbl_user_name_conf_del.setText(self.user_name)
            self.lbl_user_email_conf_del.setText(self.user_email)

        def show_delete_account(self):
            self.clear_fields()
            self.lbl_curr_page.setText("Delete Account")
            self.stacked_widget.setCurrentIndex(3)

        def show_conf_delete_account(self):
            self.clear_fields()
            self.lbl_curr_page.setText("Confirm Account Deletion")
            self.stacked_widget.setCurrentIndex(4)

        def show_pass_change(self):
            self.clear_fields()
            self.lbl_curr_page.setText("Change Master Password")
            self.stacked_widget.setCurrentIndex(1)

        def show_email_change(self):
            self.clear_fields()
            self.lbl_curr_page.setText("Change Email")
            self.stacked_widget.setCurrentIndex(2)

        def show_acc_settings(self):
            self.clear_fields()
            self.lbl_curr_page.setText("Account Settings")
            self.stacked_widget.setCurrentIndex(0)

        def clear_fields(self):
            self.le_new_pass.setText("")
            self.le_new_pass_ver.setText("")
            self.le_old_pass.setText("")
            self.le_new_email.setText("")
            self.le_new_email_ver.setText("")
            self.le_old_email.setText("")
            self.le_pass_del_acc.setText("")
            self.le_conf_del.setText("")

        def close_event(self):
            self.clear_fields()
            self.lbl_curr_page.setText("Account Settings")
            self.stacked_widget.setCurrentIndex(0)
            self.hide()

        def display_msg_box(self, text: str):
            self.msg_box.set_text(text)
            self.msg_box.show_message()


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
            cache.vault_to_cache(self.controller.api.get_vault_items())

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
            exp_month = self.controller.card_exp_month_converter_str(self.combo_exp_month.currentText())
            exp_year = self.combo_exp_year.currentText()
            cvv = self.le_cvv.text()
            notes = self.te_notes.toPlainText()
            folder = self.combo_folders.currentText()

            if exp_month == "00" or exp_year == "- Select -" or brand == "- Select -":
                self.controller.msg_box.set_text("Error: Please select a\nvalue from each combo box")
                self.controller.msg_box.show_message()
                return

            curr_date = str(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
            item = BankCardItem(name, name_on_card, card_number, exp_month, exp_year, brand, cvv, curr_date, curr_date, notes, folder)

            try:
                self.controller.api.add_item_to_vault(item)
            except Exception as e:
                print(e)
                self.parent().display_msg_box(e.args[0])
                return

            cache = self.controller.cache
            cache.vault_to_cache(self.controller.api.get_vault_items())

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
            cache.vault_to_cache(self.controller.api.get_vault_items())

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
            cache.vault_to_cache(self.controller.api.get_vault_items())

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
            cache.vault_to_cache(self.controller.api.get_vault_items())

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
            self.recently_del = self.item.recently_deleted
            self.is_editing = False

            self.toggle_fav_style()

            self.btn_fav.clicked.connect(self.api_fav)
            self.btn_edit.clicked.connect(self.enable_edit)

            if self.recently_del:
                self.set_recently_del_style()

        def set_recently_del_style(self):
            self.lbl_date_modified.setText("Date deleted:")
            self.lbl_date_created.hide()
            self.lbl_create_value.hide()

            self.btn_fav.setText("Delete")
            self.btn_fav.setFont(QFont("Arial", 12, QFont.Bold))

            self.btn_fav.setStyleSheet("#btn_fav:clicked {background-color: rgba(176, 11, 4, 200);} #btn_fav:hover {background-color: rgba(176, 11, 4, 110)}")
            self.btn_edit.setText("Restore")

            self.btn_edit.clicked.disconnect(self.enable_edit)
            self.btn_edit.clicked.connect(self.api_delete)

            self.btn_fav.clicked.disconnect(self.api_fav)
            self.btn_fav.clicked.connect(self.api_perm_delete)

        def api_perm_delete(self):
            if self.controller.perm_delete(self.item):
                self.controller.msg_box.set_text("Item permanently deleted")
                self.controller.msg_box.show_message()
            else:
                self.controller.msg_box.set_text("Error: Could not permanently\n delete item")
                self.controller.msg_box.show_message()

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
                self.item.favourite = False
                self.toggle_fav_style()
            else:
                self.fav = True
                self.item.favourite = True
                self.toggle_fav_style()

        def api_fav(self):
            if self.controller.fav_item(self.item):
                self.toggle_fav()
            else:
                self.controller.msg_box.set_text("Error: Could not favourite item")
                self.controller.msg_box.show_message()

        def disable_edit(self):
            self.is_editing = False
            self.te_notes.setReadOnly(True)
            self.combo_folders.setEnabled(False)
            self.le_email.setReadOnly(True)
            self.le_password.setReadOnly(True)
            self.le_website.setReadOnly(True)
            self.btn_edit.setText("Edit")
            self.btn_fav.setFont(QFont("Arial", 12, QFont.Normal))
            self.toggle_fav_style()
            self.btn_edit.clicked.disconnect(self.api_edit)
            self.btn_fav.clicked.disconnect(self.api_delete)
            self.btn_edit.clicked.connect(self.enable_edit)
            self.btn_fav.clicked.connect(self.api_fav)

        def enable_edit(self):
            self.is_editing = True
            self.te_notes.setReadOnly(False)
            self.combo_folders.setEnabled(True)
            self.le_email.setReadOnly(False)
            self.le_password.setReadOnly(False)
            self.le_website.setReadOnly(False)
            self.btn_edit.setText("Save")
            self.btn_fav.setText("Delete")
            self.btn_fav.setFont(QFont("Arial", 12, QFont.Bold))
            self.btn_fav.setStyleSheet("#btn_fav:clicked {background-color: rgba(176, 11, 4, 200);} #btn_fav:hover {background-color: rgba(176, 11, 4, 110)}")
            self.btn_edit.clicked.disconnect(self.enable_edit)
            self.btn_fav.clicked.disconnect(self.api_fav)
            self.btn_edit.clicked.connect(self.api_edit)
            self.btn_fav.clicked.connect(self.api_delete)

        def api_edit(self):
            if self.controller.edit_item(self.save_item_changes()):
                self.controller.msg_box.set_text("Item edited successfully")
                self.controller.msg_box.show_message()
                self.disable_edit()
                self.controller.refresh_items()
            else:
                self.controller.msg_box.set_text("Error: Could not edit item")
                self.controller.msg_box.show_message()
                self.disable_edit()

        def api_delete(self):
            if self.controller.add_to_recently_deleted(self.item):
                if self.item.recently_deleted:
                    self.controller.msg_box.set_text("Item restored")
                else:
                    self.controller.msg_box.set_text("Item added to recently deleted")
                self.controller.msg_box.show_message()
            else:
                self.controller.msg_box.set_text("Error: Could not delete item")
                self.controller.msg_box.show_message()

        def save_item_changes(self) -> LoginItem:
            notes = self.te_notes.toPlainText()
            folder = self.combo_folders.currentText()
            email = self.le_email.text()
            password = self.le_password.text()
            website = self.le_website.text()

            item = self.item

            curr_date = str(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))

            item.note = notes
            item.folder = folder
            item.date_modified = curr_date
            item.email = email
            item.password = password
            item.website = website


            return item


    class CardDetails(BankCardItemDetails):
        def __init__(self, controller=None, item=None):
            super().__init__()
            self.controller:Controller = controller
            self.item:BankCardItem = item
            self.btn_fav_style = self.btn_fav.styleSheet()
            self.fav = self.item.favourite
            self.recently_del = self.item.recently_deleted
            self.is_editing = False

            self.toggle_fav_style()

            self.btn_fav.clicked.connect(self.api_fav)
            self.btn_edit.clicked.connect(self.enable_edit)

            if self.recently_del:
                self.set_recently_del_style()

        def set_recently_del_style(self):
            self.lbl_date_modified.setText("Date deleted:")
            self.lbl_date_created.hide()
            self.lbl_create_value.hide()

            self.btn_fav.setText("Delete")
            self.btn_fav.setFont(QFont("Arial", 12, QFont.Bold))

            self.btn_fav.setStyleSheet("#btn_fav:clicked {background-color: rgba(176, 11, 4, 200);} #btn_fav:hover {background-color: rgba(176, 11, 4, 110)}")
            self.btn_edit.setText("Restore")

            self.btn_edit.clicked.disconnect(self.enable_edit)
            self.btn_edit.clicked.connect(self.api_delete)

            self.btn_fav.clicked.disconnect(self.api_fav)
            self.btn_fav.clicked.connect(self.api_perm_delete)

        def api_perm_delete(self):
            if self.controller.perm_delete(self.item):
                self.controller.msg_box.set_text("Item permanently deleted")
                self.controller.msg_box.show_message()
            else:
                self.controller.msg_box.set_text("Error: Could not permanently\n delete item")
                self.controller.msg_box.show_message()

        def set_item_details(self):
            self.lbl_item_name.setText(self.item.name)
            self.le_name_on_card.setText(self.item.name_on_card)
            self.le_card_number.setText(self.item.card_number)
            self.combo_exp_month.setCurrentText(self.controller.card_exp_month_converter_num(self.item.exp_month))
            self.combo_exp_year.setCurrentText(self.item.exp_year)
            self.combo_brand.setCurrentText(self.item.brand)
            self.le_cvv.setText(self.item.cvv)
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
                self.item.favourite = False
                self.toggle_fav_style()
            else:
                self.fav = True
                self.item.favourite = True
                self.toggle_fav_style()

        def api_fav(self):
            if self.controller.fav_item(self.item):
                self.toggle_fav()
            else:
                self.controller.msg_box.set_text("Error: Could not favourite item")
                self.controller.msg_box.show_message()

        def disable_edit(self):
            self.is_editing = False

            self.te_notes.setReadOnly(True)
            self.combo_folders.setEnabled(False)
            self.le_name_on_card.setReadOnly(True)
            self.le_card_number.setReadOnly(True)
            self.combo_exp_month.setEnabled(False)
            self.combo_exp_year.setEnabled(False)
            self.combo_brand.setEnabled(False)
            self.le_cvv.setReadOnly(True)

            self.btn_edit.setText("Edit")
            self.btn_fav.setFont(QFont("Arial", 12, QFont.Normal))
            self.toggle_fav_style()

            self.btn_edit.clicked.disconnect(self.api_edit)
            self.btn_fav.clicked.disconnect(self.api_delete)
            self.btn_edit.clicked.connect(self.enable_edit)
            self.btn_fav.clicked.connect(self.api_fav)

        def enable_edit(self):
            self.is_editing = True

            self.te_notes.setReadOnly(False)
            self.combo_folders.setEnabled(True)
            self.le_name_on_card.setReadOnly(False)
            self.le_card_number.setReadOnly(False)
            self.combo_exp_month.setEnabled(True)
            self.combo_exp_year.setEnabled(True)
            self.combo_brand.setEnabled(True)
            self.le_cvv.setReadOnly(False)

            self.btn_edit.setText("Save")
            self.btn_fav.setText("Delete")
            self.btn_fav.setFont(QFont("Arial", 12, QFont.Bold))
            self.btn_fav.setStyleSheet("#btn_fav:clicked {background-color: rgba(176, 11, 4, 200);} #btn_fav:hover {background-color: rgba(176, 11, 4, 110)}")
            self.btn_edit.clicked.disconnect(self.enable_edit)
            self.btn_fav.clicked.disconnect(self.api_fav)
            self.btn_edit.clicked.connect(self.api_edit)
            self.btn_fav.clicked.connect(self.api_delete)

        def api_edit(self):
            if self.controller.edit_item(self.save_item_changes()):
                self.controller.msg_box.set_text("Item edited successfully")
                self.controller.msg_box.show_message()
                self.disable_edit()
                self.controller.refresh_items()
            else:
                self.controller.msg_box.set_text("Error: Could not edit item")
                self.controller.msg_box.show_message()
                self.disable_edit()

        def api_delete(self):
            if self.controller.add_to_recently_deleted(self.item):
                if self.item.recently_deleted:
                    self.controller.msg_box.set_text("Item restored")
                else:
                    self.controller.msg_box.set_text("Item added to recently deleted")
                self.controller.msg_box.show_message()
            else:
                self.controller.msg_box.set_text("Error: Could not delete item")
                self.controller.msg_box.show_message()

        def save_item_changes(self) -> BankCardItem:
            notes = self.te_notes.toPlainText()
            folder = self.combo_folders.currentText()
            name_on_card = self.le_name_on_card.text()
            card_number = self.le_card_number.text()
            exp_month = self.controller.card_exp_month_converter_str(self.combo_exp_month.currentText())
            exp_year = self.combo_exp_year.currentText()
            brand = self.combo_brand.currentText()
            cvv = self.le_cvv.text()

            if exp_month == "00" or exp_year == "- Select -" or brand == "- Select -":
                self.controller.msg_box.set_text("Error: Please select a\nvalue from each combo box")
                self.controller.msg_box.show_message()
                return

            item = self.item

            curr_date = str(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))

            item.note = notes
            item.folder = folder
            item.date_modified = curr_date
            item.name_on_card = name_on_card
            item.card_number = card_number
            item.exp_month = exp_month
            item.exp_year = exp_year
            item.brand = brand
            item.cvv = cvv

            return item


    class BankDetails(BankAccItemDetails):
        def __init__(self, controller=None, item=None):
            super().__init__()
            self.controller:Controller = controller
            self.item:BankAccItem = item
            self.btn_fav_style = self.btn_fav.styleSheet()
            self.fav = self.item.favourite
            self.recently_del = self.item.recently_deleted
            self.is_editing = False

            self.toggle_fav_style()

            self.btn_fav.clicked.connect(self.api_fav)
            self.btn_edit.clicked.connect(self.enable_edit)

            if self.recently_del:
                self.set_recently_del_style()

        def set_recently_del_style(self):
            self.lbl_date_modified.setText("Date deleted:")
            self.lbl_date_created.hide()
            self.lbl_create_value.hide()

            self.btn_fav.setText("Delete")
            self.btn_fav.setFont(QFont("Arial", 12, QFont.Bold))

            self.btn_fav.setStyleSheet("#btn_fav:clicked {background-color: rgba(176, 11, 4, 200);} #btn_fav:hover {background-color: rgba(176, 11, 4, 110)}")
            self.btn_edit.setText("Restore")

            self.btn_edit.clicked.disconnect(self.enable_edit)
            self.btn_edit.clicked.connect(self.api_delete)

            self.btn_fav.clicked.disconnect(self.api_fav)
            self.btn_fav.clicked.connect(self.api_perm_delete)

        def api_perm_delete(self):
            if self.controller.perm_delete(self.item):
                self.controller.msg_box.set_text("Item permanently deleted")
                self.controller.msg_box.show_message()
            else:
                self.controller.msg_box.set_text("Error: Could not permanently\n delete item")
                self.controller.msg_box.show_message()

        def set_item_details(self):
            self.lbl_item_name.setText(self.item.name)
            self.le_acc_name.setText(self.item.name_on_account)
            self.le_acc_no.setText(self.item.account_number)
            self.le_sortcode.setText(self.item.sort_code)
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
                self.item.favourite = False
                self.toggle_fav_style()
            else:
                self.fav = True
                self.item.favourite = True
                self.toggle_fav_style()

        def api_fav(self):
            if self.controller.fav_item(self.item):
                self.toggle_fav()
            else:
                self.controller.msg_box.set_text("Error: Could not favourite item")
                self.controller.msg_box.show_message()

        def disable_edit(self):
            self.is_editing = False
            self.te_notes.setReadOnly(True)
            self.combo_folders.setEnabled(False)
            self.le_acc_name.setReadOnly(True)
            self.le_acc_no.setReadOnly(True)
            self.le_sortcode.setReadOnly(True)
            self.btn_edit.setText("Edit")
            self.btn_fav.setFont(QFont("Arial", 12, QFont.Normal))
            self.toggle_fav_style()
            self.btn_edit.clicked.disconnect(self.api_edit)
            self.btn_fav.clicked.disconnect(self.api_delete)
            self.btn_edit.clicked.connect(self.enable_edit)
            self.btn_fav.clicked.connect(self.api_fav)

        def enable_edit(self):
            self.is_editing = True
            self.te_notes.setReadOnly(False)
            self.combo_folders.setEnabled(True)
            self.le_acc_name.setReadOnly(False)
            self.le_acc_no.setReadOnly(False)
            self.le_sortcode.setReadOnly(False)
            self.btn_edit.setText("Save")
            self.btn_fav.setText("Delete")
            self.btn_fav.setFont(QFont("Arial", 12, QFont.Bold))
            self.btn_fav.setStyleSheet("#btn_fav:clicked {background-color: rgba(176, 11, 4, 200);} #btn_fav:hover {background-color: rgba(176, 11, 4, 110)}")
            self.btn_edit.clicked.disconnect(self.enable_edit)
            self.btn_fav.clicked.disconnect(self.api_fav)
            self.btn_edit.clicked.connect(self.api_edit)
            self.btn_fav.clicked.connect(self.api_delete)

        def api_edit(self):
            if self.controller.edit_item(self.save_item_changes()):
                self.controller.msg_box.set_text("Item edited successfully")
                self.controller.msg_box.show_message()
                self.disable_edit()
                self.controller.refresh_items()
            else:
                self.controller.msg_box.set_text("Error: Could not edit item")
                self.controller.msg_box.show_message()
                self.disable_edit()

        def api_delete(self):
            if self.controller.add_to_recently_deleted(self.item):
                if self.item.recently_deleted:
                    self.controller.msg_box.set_text("Item restored")
                else:
                    self.controller.msg_box.set_text("Item added to recently deleted")
                self.controller.msg_box.show_message()
            else:
                self.controller.msg_box.set_text("Error: Could not delete item")
                self.controller.msg_box.show_message()

        def save_item_changes(self) -> BankAccItem:
            notes = self.te_notes.toPlainText()
            folder = self.combo_folders.currentText()
            acc_name = self.le_acc_name.text()
            acc_no = self.le_acc_no.text()
            sortcode = self.le_sortcode.text()

            item = self.item

            curr_date = str(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))

            item.note = notes
            item.folder = folder
            item.date_modified = curr_date
            item.name_on_account = acc_name
            item.account_number = acc_no
            item.sort_code = sortcode

            return item


    class IdentityDetails(IdentityItemDetails):
        def __init__(self, controller=None, item=None):
            super().__init__()
            self.controller:Controller = controller
            self.item:IdentityItem = item
            self.btn_fav_style = self.btn_fav.styleSheet()
            self.fav = self.item.favourite
            self.recently_del = self.item.recently_deleted
            self.is_editing = False

            self.toggle_fav_style()

            self.btn_fav.clicked.connect(self.api_fav)
            self.btn_edit.clicked.connect(self.enable_edit)

            if self.recently_del:
                self.set_recently_del_style()

        def set_recently_del_style(self):
            self.lbl_date_modified_2.setText("Date deleted:")
            self.lbl_date_created_2.hide()
            self.lbl_create_value_2.hide()

            self.btn_fav.setText("Delete")
            self.btn_fav.setFont(QFont("Arial", 12, QFont.Bold))

            self.btn_fav.setStyleSheet("#btn_fav:clicked {background-color: rgba(176, 11, 4, 200);} #btn_fav:hover {background-color: rgba(176, 11, 4, 110)}")
            self.btn_edit.setText("Restore")

            self.btn_edit.clicked.disconnect(self.enable_edit)
            self.btn_edit.clicked.connect(self.api_delete)

            self.btn_fav.clicked.disconnect(self.api_fav)
            self.btn_fav.clicked.connect(self.api_perm_delete)

        def api_perm_delete(self):
            if self.controller.perm_delete(self.item):
                self.controller.msg_box.set_text("Item permanently deleted")
                self.controller.msg_box.show_message()
            else:
                self.controller.msg_box.set_text("Error: Could not permanently\n delete item")
                self.controller.msg_box.show_message()

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
            self.lbl_create_value_2.setText(self.item.date_created)
            self.lbl_modified_value_2.setText(self.item.date_modified)

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
                self.item.favourite = False
                self.toggle_fav_style()
            else:
                self.fav = True
                self.item.favourite = True
                self.toggle_fav_style()

        def api_fav(self):
            if self.controller.fav_item(self.item):
                self.toggle_fav()
            else:
                self.controller.msg_box.set_text("Error: Could not favourite item")
                self.controller.msg_box.show_message()

        def disable_edit(self):
            self.is_editing = False
            self.te_notes.setReadOnly(True)
            self.combo_title.setEnabled(False)
            self.le_first_name.setReadOnly(True)
            self.le_surname.setReadOnly(True)
            self.le_email.setReadOnly(True)
            self.le_phone_no.setReadOnly(True)
            self.le_nat_insur_no.setReadOnly(True)
            self.le_pass_no.setReadOnly(True)
            self.le_license_no.setReadOnly(True)
            self.btn_edit.setText("Edit")
            self.btn_fav.setFont(QFont("Arial", 12, QFont.Normal))
            self.toggle_fav_style()
            self.btn_edit.clicked.disconnect(self.api_edit)
            self.btn_fav.clicked.disconnect(self.api_delete)
            self.btn_edit.clicked.connect(self.enable_edit)
            self.btn_fav.clicked.connect(self.api_fav)

        def enable_edit(self):
            self.is_editing = True
            self.te_notes.setReadOnly(False)
            self.combo_title.setEnabled(True)
            self.le_first_name.setReadOnly(False)
            self.le_surname.setReadOnly(False)
            self.le_email.setReadOnly(False)
            self.le_phone_no.setReadOnly(False)
            self.le_nat_insur_no.setReadOnly(False)
            self.le_pass_no.setReadOnly(False)
            self.le_license_no.setReadOnly(False)
            self.btn_edit.setText("Save")
            self.btn_fav.setText("Delete")
            self.btn_fav.setFont(QFont("Arial", 12, QFont.Bold))
            self.btn_fav.setStyleSheet("#btn_fav:clicked {background-color: rgba(176, 11, 4, 200);} #btn_fav:hover {background-color: rgba(176, 11, 4, 110)}")
            self.btn_edit.clicked.disconnect(self.enable_edit)
            self.btn_fav.clicked.disconnect(self.api_fav)
            self.btn_edit.clicked.connect(self.api_edit)
            self.btn_fav.clicked.connect(self.api_delete)

        def api_edit(self):
            if self.controller.edit_item(self.save_item_changes()):
                self.controller.msg_box.set_text("Item edited successfully")
                self.controller.msg_box.show_message()
                self.disable_edit()
                self.controller.refresh_items()
            else:
                self.controller.msg_box.set_text("Error: Could not edit item")
                self.controller.msg_box.show_message()
                self.disable_edit()

        def api_delete(self):
            if self.controller.add_to_recently_deleted(self.item):
                if self.item.recently_deleted:
                    self.controller.msg_box.set_text("Item restored")
                else:
                    self.controller.msg_box.set_text("Item added to recently deleted")
                self.controller.msg_box.show_message()
            else:
                self.controller.msg_box.set_text("Error: Could not delete item")
                self.controller.msg_box.show_message()

        def save_item_changes(self) -> IdentityItem:
            notes = self.te_notes.toPlainText()
            title = self.combo_title.currentText()
            fname = self.le_first_name.text()
            sname = self.le_surname.text()
            email = self.le_email.text()
            phone_no = self.le_phone_no.text()
            nat_no = self.le_nat_insur_no.text()
            pass_no = self.le_pass_no.text()
            lic_no = self.le_license_no.text()

            item = self.item

            curr_date = str(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))

            item.note = notes
            item.title = title
            item.first_name = fname
            item.surname = sname
            item.email = email
            item.phone_number = phone_no
            item.nat_insur_no = nat_no
            item.passport_no = pass_no
            item.license_no = lic_no
            item.date_modified = curr_date

            return item


    class NoteDetails(SecureNoteDetails):
        def __init__(self, controller=None, item=None):
            super().__init__()
            self.controller:Controller = controller
            self.item:SecureNoteItem = item
            self.btn_fav_style = self.btn_fav.styleSheet()
            self.fav = self.item.favourite
            self.recently_del = self.item.recently_deleted
            self.is_editing = False

            self.toggle_fav_style()

            self.btn_fav.clicked.connect(self.api_fav)
            self.btn_edit.clicked.connect(self.enable_edit)

            if self.recently_del:
                self.set_recently_del_style()

        def set_recently_del_style(self):
            self.lbl_date_modified.setText("Date deleted:")
            self.lbl_date_created.hide()
            self.lbl_create_value.hide()

            self.btn_fav.setText("Delete")
            self.btn_fav.setFont(QFont("Arial", 12, QFont.Bold))

            self.btn_fav.setStyleSheet("#btn_fav:clicked {background-color: rgba(176, 11, 4, 200);} #btn_fav:hover {background-color: rgba(176, 11, 4, 110)}")
            self.btn_edit.setText("Restore")

            self.btn_edit.clicked.disconnect(self.enable_edit)
            self.btn_edit.clicked.connect(self.api_delete)

            self.btn_fav.clicked.disconnect(self.api_fav)
            self.btn_fav.clicked.connect(self.api_perm_delete)


        def set_item_details(self):
            self.lbl_item_name.setText(self.item.name)
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
                self.item.favourite = False
                self.toggle_fav_style()
            else:
                self.fav = True
                self.item.favourite = True
                self.toggle_fav_style()

        def api_fav(self):
            if self.controller.fav_item(self.item):
                self.toggle_fav()
            else:
                self.controller.msg_box.set_text("Error: Could not favourite item")
                self.controller.msg_box.show_message()

        def disable_edit(self):
            self.is_editing = False
            self.te_notes.setReadOnly(True)
            self.combo_folders.setEnabled(False)
            self.btn_edit.setText("Edit")
            self.btn_fav.setFont(QFont("Arial", 12, QFont.Normal))
            self.toggle_fav_style()
            self.btn_edit.clicked.disconnect(self.api_edit)
            self.btn_fav.clicked.disconnect(self.api_delete)
            self.btn_edit.clicked.connect(self.enable_edit)
            self.btn_fav.clicked.connect(self.api_fav)

        def enable_edit(self):
            self.is_editing = True
            self.te_notes.setReadOnly(False)
            self.combo_folders.setEnabled(True)
            self.btn_edit.setText("Save")
            self.btn_fav.setText("Delete")
            self.btn_fav.setFont(QFont("Arial", 12, QFont.Bold))
            self.btn_fav.setStyleSheet("#btn_fav:clicked {background-color: rgba(176, 11, 4, 200);} #btn_fav:hover {background-color: rgba(176, 11, 4, 110)}")
            self.btn_edit.clicked.disconnect(self.enable_edit)
            self.btn_fav.clicked.disconnect(self.api_fav)
            self.btn_edit.clicked.connect(self.api_edit)
            self.btn_fav.clicked.connect(self.api_delete)

        def api_edit(self):
            if self.controller.edit_item(self.save_item_changes()):
                self.controller.msg_box.set_text("Item edited successfully")
                self.controller.msg_box.show_message()
                self.disable_edit()
            else:
                self.controller.msg_box.set_text("Error: Could not edit item")
                self.controller.msg_box.show_message()
                self.disable_edit()

        def api_delete(self):
            if self.controller.add_to_recently_deleted(self.item):
                if self.item.recently_deleted:
                    self.controller.msg_box.set_text("Item restored")
                else:
                    self.controller.msg_box.set_text("Item added to recently deleted")
                self.controller.msg_box.show_message()
            else:
                self.controller.msg_box.set_text("Error: Could not delete item")
                self.controller.msg_box.show_message()

        def api_perm_delete(self):
            if self.controller.perm_delete(self.item):
                self.controller.msg_box.set_text("Item permanently deleted")
                self.controller.msg_box.show_message()
            else:
                self.controller.msg_box.set_text("Error: Could not permanently\n delete item")
                self.controller.msg_box.show_message()


        def save_item_changes(self) -> SecureNoteItem:
            notes = self.te_notes.toPlainText()
            folder = self.combo_folders.currentText()
            item = self.item

            curr_date = str(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))

            item.note = notes
            item.folder = folder
            item.date_modified = curr_date

            return item


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
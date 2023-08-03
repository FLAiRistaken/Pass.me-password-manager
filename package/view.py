import datetime
import sys
import time
import json

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import (QEasingCurve, QPropertyAnimation, QRect,
                            QRegularExpression, QSize, Qt, QTimer, Signal, Slot)
from PySide6.QtGui import (QFont, QPixmap, QRegularExpressionValidator,
                           QValidator, QClipboard, QAction)
from PySide6.QtWidgets import (QGridLayout, QLabel, QLineEdit, QListWidgetItem,
                               QWidget, QCheckBox, QComboBox, QSlider, QApplication, QMenu, QMainWindow)

from package.account_creator import Account, AccountCreator
from package.authenitcation import Authentication
from package.password_generator import GenPassword, GenPassphrase
from package.db_connect import ApiConnect
from package.mail import mail
from package.model.Items import *
from package.cache_item import CacheItem
from package.ui import (create_acc_screen, item_in_list, login_screen,
                        main_screen, password_generator_widget, widget_password_options,
                        widget_passphrase_options, widget_msg_box, pass_hist_list_item,
                        new_item_screen, new_login_screen, new_item_widget_container,
                        login_item_details_main, new_bank_acc_screen, new_bank_card_screen,
                        new_identity_screen, new_secure_note_screen, secure_note_details,
                        bank_acc_item_details, bank_card_item_details, identity_item_details,
                        settings_widget, widget_bottom_msg_box)


class LoginWindow(QtWidgets.QDialog, login_screen.Ui_Form):
    def __init__(self, parent=None):
        self.visible_icon = QPixmap("eye-visible.png")
        self.hidden_icon = QPixmap("eye-notvisible.png")
        super(LoginWindow, self).__init__(parent)
        # sets up the Login Screens UI
        self.setupUi(self)

        # hides the hint screen state
        self.rightBox_Hint.hide()

        self.lineEdit_MastPassword.addAction(
            self.visible_icon, QLineEdit.TrailingPosition
        )
        # self.lineEdit_MastPassword.triggered.connect(self.togglePasswordAction)
        # self.pass_shown = False

        # makes window borderless
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.center()
        self.old_pos = self.pos()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
        self.drag_pos = event.globalPosition().toPoint()
        event.accept()

class CreateWindow(QWidget, create_acc_screen.Ui_Form):
    def __init__(self, parent=None):
        super(CreateWindow, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.center()
        self.old_pos = self.pos()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
        self.drag_pos = event.globalPosition().toPoint()
        event.accept()

class MainWindow(QWidget, main_screen.Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.center()
        self.old_pos = self.pos()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
        self.drag_pos = event.globalPosition().toPoint()
        event.accept()

class SettingsWidget(QWidget, settings_widget.Ui_Form):
    def __init__(self, parent=None):
        super(SettingsWidget, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.center()
        self.old_pos = self.pos()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
        self.drag_pos = event.globalPosition().toPoint()
        event.accept()

class ListItem(QWidget, item_in_list.Ui_Form):
    def __init__(self, parent=None):
        super(ListItem, self).__init__(parent)
        self.setupUi(self)
        self.lbl_Item_Name.setText("Testing")
        self.lbl_Item_Details.setText("Test")

    def set_text(self, name, details):
        self.lbl_Item_Name.setText(name)
        self.lbl_Item_Details.setText(details)

class PasswordGeneratorWidget(QWidget, password_generator_widget.Ui_Form):
    def __init__(self, parent=None):
        super(PasswordGeneratorWidget, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.center()
        self.old_pos = self.pos()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
        self.drag_pos = event.globalPosition().toPoint()
        event.accept()

class PasswordOptions(QWidget, widget_password_options.Ui_Form):
    def __init__(self, parent=None):
        super(PasswordOptions, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

class PassphraseOptions(QWidget, widget_passphrase_options.Ui_Form):
    def __init__(self, parent=None):
        super(PassphraseOptions, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

class MsgBox(QWidget, widget_msg_box.Ui_Form):
    def __init__(self, parent=None):
        super(MsgBox, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

class BottMsgBox(QWidget, widget_bottom_msg_box.Ui_Form):
    def __init__(self, parent=None):
        super(BottMsgBox, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

class PassHistListItem(QWidget, pass_hist_list_item.Ui_Form):
    def __init__(self, parent=None):
        super(PassHistListItem, self).__init__(parent)
        self.setupUi(self)


class NewItemWidgetContainer(QWidget, new_item_widget_container.Ui_Form):
    def __init__(self, parent=None):
        super(NewItemWidgetContainer, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.center()
        self.old_pos = self.pos()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
        self.drag_pos = event.globalPosition().toPoint()
        event.accept()

class NewItemScreen(QWidget, new_item_screen.Ui_Form):
    def __init__(self, parent=None):
        super(NewItemScreen, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

class NewLoginItemScreen(QWidget, new_login_screen.Ui_Form):
    def __init__(self, parent=None):
        super(NewLoginItemScreen, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

class NewBankCardItemScreen(QWidget, new_bank_card_screen.Ui_Form):
    def __init__(self, parent=None):
        super(NewBankCardItemScreen, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

class NewBankAccItemScreen(QWidget, new_bank_acc_screen.Ui_Form):
    def __init__(self, parent=None):
        super(NewBankAccItemScreen, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

class NewIdentityItemScreen(QWidget, new_identity_screen.Ui_Form):
    def __init__(self, parent=None):
        super(NewIdentityItemScreen, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

class NewSecureNoteItemScreen(QWidget, new_secure_note_screen.Ui_Form):
    def __init__(self, parent=None):
        super(NewSecureNoteItemScreen, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


class LoginItemDetails(QWidget, login_item_details_main.Ui_Form):
    def __init__(self, parent=None):
        super(LoginItemDetails, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

class BankAccItemDetails(QWidget, bank_acc_item_details.Ui_Form):
    def __init__(self, parent=None):
        super(BankAccItemDetails, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


class BankCardItemDetails(QWidget, bank_card_item_details.Ui_Form):
    def __init__(self, parent=None):
        super(BankCardItemDetails, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


class IdentityItemDetails(QWidget, identity_item_details.Ui_Form):
    def __init__(self, parent=None):
        super(IdentityItemDetails, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

class SecureNoteDetails(QWidget, secure_note_details.Ui_Form):
    def __init__(self, parent=None):
        super(SecureNoteDetails, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

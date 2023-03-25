import datetime
import sys
import time

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import (QEasingCurve, QPropertyAnimation, QRect,
                            QRegularExpression, QSize, Qt, QTimer)
from PySide6.QtGui import (QFont, QPixmap, QRegularExpressionValidator,
                           QValidator, QClipboard)
from PySide6.QtWidgets import (QGridLayout, QLabel, QLineEdit, QListWidgetItem,
                               QWidget, QCheckBox, QComboBox, QSlider, QApplication)

from package.account_creator import Account, AccountCreator
from package.authenitcation import Authentication
from package.password_generator import GenPassword, GenPassphrase
from package.db_connect import DBConnect
from package.mail import mail
from package.model import Items
from package.ui import (create_acc_screen, item_in_list, login_screen,
                        main_screen, password_generator_widget, widget_password_options,
                        widget_passphrase_options, widget_msg_box, pass_hist_list_item,
                        new_item_screen, new_login_screen, new_item_widget_container)


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
            self.visibleIcon, QLineEdit.TrailingPosition
        )
        # self.lineEdit_MastPassword.triggered.connect(self.togglePasswordAction)
        # self.pass_shown = False

        self.msg_box = MsgBox(self)
        self.msg_box.hide()
        #self.msg_box.move((self.screen().availableGeometry().center() / 2) - self.msg_box.rect().center())

        # makes window borderless
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # runs @center, allows window to be moved without a frame
        self.center()
        self.old_pos = self.pos()

        # button connects to functions, allows button presses to function
        self.btnCreate.clicked.connect(self.show_create)
        self.btnLogin.clicked.connect(self.login_button)
        self.btnHint.clicked.connect(self.hint_clicked)
        self.btnClose.clicked.connect(sys.exit)
        self.btnBack.clicked.connect(self.back_clicked)
        # self.btnGetHint.clicked.connect(self.send_hint)

    def show_error_box(self):
        self.error_box.show()
        anim = QPropertyAnimation(self.error_box, b"geometry", self.widget)
        anim.setStartValue(QRect(290, 356, 491, 40))
        anim.setEndValue(QRect(290, 385, 491, 40))
        anim.setDuration(400)
        anim.setEasingCurve(QEasingCurve.InOutCubic)
        anim.start()

    #
    def show_create(self, checked):
        self.w = CreateWindow()
        self.w.show()
        self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mouse_press_event(self, event):
        self.drag_pos = event.globalPosition().toPoint()

    def mouse_move_event(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
        self.drag_pos = event.globalPosition().toPoint()
        event.accept()

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

    def login_button(self):
        # m = mail()
        emailval = self.lineEdit_Email.text()
        passval = self.lineEdit_MastPassword.text()
        auth = Authentication(emailval, passval)
        if auth.authenticated == True:
            print("Logging in...")
            #  m.sendMail("flairx@protonmail.com", "Logged into pass.me",
            #              ("Logged into pass.me at: " + str(datetime.datetime.now)))
            self.accept()
        else:
            self.error_box.text = "Failed to authenticate"
            self.show_error_box()


class CreateWindow(QWidget, create_acc_screen.Ui_Form):
    def __init__(self, parent=None):
        super(CreateWindow, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.is_error_box_shown = False

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

        self.center()
        self.old_pos = self.pos()

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
        db = DBConnect()
        emailval = self.lineEdit_Email.text().lower()
        passval = self.lineEdit_MastPassword.text()
        nameval = self.lineEdit_Name.text()
        hintval = self.lineEdit_PassHint.text()
        if db.check_email(emailval) == True:
            self.lineEdit_Email.setStyleSheet(self.lineEditRed)
            self.lineEdit_Email.setToolTip("Email already in use")
            self.show_error_box(
                "ERROR: Email already in use, please use a different email address"
            )
            self.btnCreate.setEnabled(False)
            return
        ac = AccountCreator(emailval, passval, nameval, hintval)
        db.new_user(ac.acc)

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mouse_press_event(self, event):
        self.drag_pos = event.globalPosition().toPoint()

    def mouse_move_event(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
        self.drag_pos = event.globalPosition().toPoint()
        event.accept()


class MainWindow(QWidget, main_screen.Ui_Main):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()
        self.old_pos = self.pos()

        self.btnGenerator.clicked.connect(self.show_generator)
        self.btnNew.clicked.connect(self.show_new_item_screen)

        myListItem = ListItem()
        myQListWidgetItem = QListWidgetItem(self.lvItems)
        myQListWidgetItem.setSizeHint(QSize(150, 60))
        self.lvItems.addItem(myQListWidgetItem)
        self.lvItems.setItemWidget(myQListWidgetItem, myListItem)
        # self.label.setPixmap(icons/"search_icon.png")

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mouse_press_event(self, event):
        self.drag_pos = event.globalPosition().toPoint()

    def mouse_move_event(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
        self.drag_pos = event.globalPosition().toPoint()
        event.accept()

    def show_generator(self):
        self.w = PasswordGeneratorWidget()
        self.w.show()

    def show_new_item_screen(self):
        self.w = NewItemWidgetContainer()
        self.w.add_widget(NewItemScreen(self.w))
        self.w.show()


class ListItem(QWidget, item_in_list.Ui_Item_In_List):
    def __init__(self, parent=None):
        super(ListItem, self).__init__(parent)
        self.setupUi(self)
        self.lbl_Item_Name.setText("Testing")
        self.lbl_Item_Details.setText("Test")

class PasswordGeneratorWidget(QWidget, password_generator_widget.Ui_Form):
    def __init__(self, parent=None):
        super(PasswordGeneratorWidget, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()
        self.old_pos = self.pos()

        self.msg_box = MsgBox(self)
        self.msg_box.hide()
        self.msg_box.move((self.screen().availableGeometry().center() / 2) - self.msg_box.rect().center())

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
        self.deleteLater()
        self.close()

    def copy_to_clipboard(self):
        text = self.le_password.text()
        self.clipboard.clear()
        self.clipboard.set_text(text)
        self.msg_box.set_text("Copied to Clipboard ✓")
        self.msg_box.show()
        timer = QTimer(self)
        timer.singleShot(2000, lambda: self.msg_box.hide())

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mouse_press_event(self, event):
        self.drag_pos = event.globalPosition().toPoint()

    def mouse_move_event(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
        self.drag_pos = event.globalPosition().toPoint()
        event.accept()

    def check_radios(self):
        if self.rad_password.isChecked():
            if self.gridLayout_3.count() > 3:
                old_widget = self.gridLayout_3.itemAt(3).widget()
                self.gridLayout_3.replaceWidget(self.gridLayout_3.itemAt(3).widget(), PasswordOptions())
                old_widget.deleteLater()
                self.set_event_listeners()
            else:
                self.gridLayout_3.addWidget(PasswordOptions())
                self.set_event_listeners()
        elif self.rad_passphrase.isChecked():
            if self.gridLayout_3.count() > 3:
                old_widget = self.gridLayout_3.itemAt(3).widget()
                self.gridLayout_3.replaceWidget(self.gridLayout_3.itemAt(3).widget(), PassphraseOptions())
                old_widget.deleteLater()
                self.set_event_listeners()
            else:
                self.gridLayout_3.addWidget(PassphraseOptions())
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
        return self.gridLayout_3.itemAt(3).widget().getValues()

    def generate(self):
        if self.rad_password.isChecked():
            password = GenPassword(*self.get_values()).generate_password()
            self.le_password.setText(password)
            self.add_to_list(password, str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        elif self.rad_passphrase.isChecked():
            passphrase = GenPassphrase(*self.get_values()).generate_passphrase()
            self.le_password.setText(passphrase)
            self.add_to_list(passphrase, str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    def add_to_list(self, password: str, date: str):
        pass_item = PassHistListItem()
        pass_item.set_text(password, date)
        q_list_item = QListWidgetItem(self.listWidget)
        q_list_item.setSizeHint(QSize(200, 60))
        self.listWidget.addItem(q_list_item)
        self.listWidget.setItemWidget(q_list_item, pass_item)


class PasswordOptions(QWidget, widget_password_options.Ui_Form):
    def __init__(self, parent=None):
        super(PasswordOptions, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def get_values(self) -> tuple[int, bool, bool, bool]:
        return self.slide_len.value(), self.chk_nums.isChecked(), self.chk_spec.isChecked(), self.chk_capitals.isChecked()

    def check_fields(self):
        if (self.slide_len.valueChanged or self.chk_spec.clicked or self.chk_nums.clicked or self.chk_capitals.clicked):
            return True

class PassphraseOptions(QWidget, widget_passphrase_options.Ui_Form):
    def __init__(self, parent=None):
        super(PassphraseOptions, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def get_values(self) -> tuple[int, str, bool, bool]:
        return self.slide_word_no.value(), self.combo_separator.currentText(), self.chk_num.isChecked(), self.chk_capitalise.isChecked()

    def check_fields(self):
        if (self.slide_word_no.valueChanged or self.combo_separator.currentIndexChanged or self.chk_num.clicked or self.chk_capitalise.clicked):
            return True

class MsgBox(QWidget, widget_msg_box.Ui_Form):
    def __init__(self, parent=None):
        super(MsgBox, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def set_text(self, text: str):
        self.lbl_msg.setText(text)

class PassHistListItem(QWidget, pass_hist_list_item.Ui_Form):
    def __init__(self, parent=None):
        super(PassHistListItem, self).__init__(parent)
        self.setupUi(self)

    def set_text(self, password: str, date: str):
        self.lbl_password.setText(password)
        self.lbl_gen_date.setText(date)

class NewItemScreen(QWidget, new_item_screen.Ui_Form):
    def __init__(self, parent=None):
        super(NewItemScreen, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.btnClose.clicked.connect(self.close_self)
        self.btn_item_login.clicked.connect(self.show_login)

    def show_login(self):
        print ("Loading new login item screen...")
        self.w = NewLoginItemScreen()
        self.parent().add_widget(self.w)
        self.hide()

    def close_self(self):
        self.parent().close()
        self.parent().deleteLater()
        self.deleteLater()

class NewLoginItemScreen(QWidget, new_login_screen.Ui_Form):
    def __init__(self, parent=None):
        super(NewLoginItemScreen, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.btn_back.clicked.connect(self.show_new_item_screen)
        self.btn_save.clicked.connect(self.save_item)

    def show_new_item_screen(self):
        self.hide()
        self.parent().findChild(NewItemScreen).show()

    def save_item(self):
        name = self.le_name.text()
        email = self.le_email.text()
        password = self.le_password.text()
        website = self.le_website.text()
        notes = self.te_notes.toPlainText()
        folder = self.combo_folder.currentText()


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

    def mouse_press_event(self, event):
        self.drag_pos = event.globalPosition().toPoint()

    def mouse_move_event(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
        self.drag_pos = event.globalPosition().toPoint()
        event.accept()

    def add_widget(self, widget: QWidget):
            self.resize(widget.size())
            self.layout().add_widget(widget)


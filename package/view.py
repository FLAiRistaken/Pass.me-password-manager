import datetime
import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QRegularExpression, QSize, QPropertyAnimation, QPoint, QRect, QEasingCurve
from PySide6.QtGui import QPixmap, QRegularExpressionValidator, QValidator
from PySide6.QtWidgets import QLineEdit, QWidget, QListWidgetItem

from package import account_creator, authenitcation, db_connect, mail
from package.ui import (
    create_acc_screen,
    login_screen,
    main_screen,
    item_in_list,
)


class LoginWindow(QtWidgets.QDialog, login_screen.Ui_Form):
    def __init__(self, parent=None):
        self.visibleIcon = QPixmap("eye-visible.png")
        self.hiddenIcon = QPixmap("eye-notvisible.png")
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

        # makes window borderless
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # runs @center, allows window to be moved without a frame
        self.center()
        self.oldPos = self.pos()

        # button connects to functions, allows button presses to function
        self.btnCreate.clicked.connect(self.showCreate)
        self.btnLogin.clicked.connect(self.loginButton)
        self.btnHint.clicked.connect(self.hintClicked)
        self.btnClose.clicked.connect(sys.exit)
        self.btnBack.clicked.connect(self.backClicked)
        # self.btnGetHint.clicked.connect(self.sendHint)

    #
    def showCreate(self, checked):
        self.w = CreateWindow()
        self.w.show()
        self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()

    def hintClicked(self):
        self.rightBox.setEnabled(False)
        self.rightBox.hide()
        self.rightBox_Hint.setEnabled(True)
        self.rightBox_Hint.show()

    def backClicked(self):
        self.rightBox_Hint.setEnabled(False)
        self.rightBox_Hint.hide()
        self.rightBox.setEnabled(True)
        self.rightBox.show()

    # function to send verification email
    def sendHint(self):
        m = mail.mail()
        m.sendMail("    ", "Verification Code", "Your verification code is: ")
        QtWidgets.QMessageBox.information(
            self,
            "Verification Code Sent",
            "A verification code has been sent to your email",
        )

    def loginButton(self):
        # m = mail.mail()
        emailval = self.lineEdit_Email.text()
        passval = self.lineEdit_MastPassword.text()
        auth = authenitcation.Authentication(emailval, passval)
        if auth.authenticated == True:
            print("Logging in...")
            #  m.sendMail("flairx@protonmail.com", "Logged into pass.me",
            #              ("Logged into pass.me at: " + str(datetime.datetime.now)))
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, "Login Failed", "Logging in failed, please try again"
            )


class CreateWindow(QWidget, create_acc_screen.Ui_Form):
    def __init__(self, parent=None):
        super(CreateWindow, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

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
        self.oldPos = self.pos()

        self.btnCreate.setEnabled(False)

        self.btnLogin.clicked.connect(self.showLogin)
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
    def show_error_box(self):
        self.errror_box.show()
        anim = QPropertyAnimation(self.errror_box, b"geometry", self.widget)
        anim.setStartValue(QRect(280, 600, 491, 45))
        anim.setEndValue(QRect(280, 650, 491, 45))
        anim.setDuration(1000)
        anim.setEasingCurve(QEasingCurve.InOutCubic)
        anim.start()
        
        

    def email_changed(self):
        if self.lineEdit_Email.hasAcceptableInput():
            self.lineEdit_Email.setToolTip("Valid Email")
            self.lineEdit_Email.setStyleSheet(self.lineEditGreen)
            self.checkFields()
        else:
            self.lineEdit_Email.setToolTip("Invalid Email")
            self.lineEdit_Email.setStyleSheet(self.lineEditRed)
            self.btnCreate.setEnabled(False)

    def password_changed(self):
        if self.lineEdit_MastPassword.hasAcceptableInput():
            self.lineEdit_MastPassword.setToolTip("Valid Password")
            self.lineEdit_MastPassword.setStyleSheet(self.lineEditGreen)
            self.checkFields()
        else:
            self.lineEdit_MastPassword.setToolTip("Invalid Password")
            self.lineEdit_MastPassword.setStyleSheet(self.lineEditRed)
            self.btnCreate.setEnabled(False)

    def password_verify_changed(self):
        if self.lineEdit_MastPassword2.text() == self.lineEdit_MastPassword.text():
            self.lineEdit_MastPassword2.setToolTip("Passwords Match")
            self.lineEdit_MastPassword2.setStyleSheet(self.lineEditGreen)
            self.checkFields()
        else:
            self.lineEdit_MastPassword2.setToolTip("Passwords Do Not Match")
            self.lineEdit_MastPassword2.setStyleSheet(self.lineEditRed)
            self.btnCreate.setEnabled(False)

    # function to check each field for valid input and then enable the create account button
    def checkFields(self):
        if (self.lineEdit_Email.hasAcceptableInput() and self.lineEdit_MastPassword.hasAcceptableInput() and self.lineEdit_MastPassword2.text() == self.lineEdit_MastPassword.text()):
            self.btnCreate.setEnabled(True)
        else:
            self.btnCreate.setEnabled(False)

    def showLogin(self, checked):
        self.w = LoginWindow()
        self.w.show()
        self.close()

    def createAccButton(self):
        db = db_connect.dbConnect()
        emailval = self.lineEdit_Email.text().lower()
        passval = self.lineEdit_MastPassword.text()
        nameval = self.lineEdit_Name.text()
        hintval = self.lineEdit_PassHint.text()
        if (db.check_email(emailval) == True):
            self.lineEdit_Email.setStyleSheet(self.lineEditRed)
            self.lineEdit_Email.setToolTip("Email already in use")
            self.lblError.setText("ERROR: Email already in use, please use a different email address")
            self.show_error_box()
            self.btnCreate.setEnabled(False)
            return
        ac = account_creator.AccountCreator(emailval, passval, nameval, hintval)
        db.new_user(ac.acc)

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()


class MainWindow(QWidget, main_screen.Ui_Main):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.center()
        self.oldPos = self.pos()
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

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()


class ListItem(QWidget, item_in_list.Ui_Item_In_List):
    def __init__(self, parent=None):
        super(ListItem, self).__init__(parent)
        self.setupUi(self)
        self.lbl_Item_Name.setText("Testing")
        self.lbl_Item_Details.setText("Test")

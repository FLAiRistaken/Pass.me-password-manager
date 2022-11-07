

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QWidget)
from PySide6 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(860, 767)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, -10, 781, 761))
        font = QFont()
        font.setFamilies([u"Nexa-Trial"])
        self.widget.setFont(font)
        self.widget.setStyleSheet(u"QPushButton#btnCreate{\n"
"	background-color:rgba(148, 105, 141, 255);\n"
"	color:rgba(255, 255, 255, 220);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#btnCreate:pressed{\n"
"\n"
"	background-color:rgba(74, 53, 70, 255);\n"
"\n"
"}\n"
"QPushButton#btnCreate:hover{\n"
"	background-color:rgba(111, 77, 104, 255);\n"
"}\n"
"QPushButton#btnLogin{\n"
"	background-color:rgba(170, 170, 170, 255);\n"
"	color:rgba(255, 255, 255, 200);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#btnLogin:hover{\n"
"	background-color:rgba(140, 140, 140, 255);\n"
"}\n"
"\n"
"QProgressBar#passStrengthBar{\n"
"	background-color: rgba(140, 140, 140, 255);\n"
"}\n"
"QProgressBar#passStrengthBar::chunk{\n"
"	background-color: rgba(110, 77, 103, 220);\n"
"	border-radius:5px;\n"
"}")
        self.rightBox = QLabel(self.widget)
        self.rightBox.setObjectName(u"rightBox")
        self.rightBox.setGeometry(QRect(280, 120, 481, 590))
        self.rightBox.setStyleSheet(u"background-color: rgba(255, 255, 255, 255);\n"
"border-radius:10px")
        self.leftBox = QLabel(self.widget)
        self.leftBox.setObjectName(u"leftBox")
        self.leftBox.setGeometry(QRect(10, 85, 281, 660))
        self.leftBox.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(92, 61, 88, 255));\n"
"border-radius: 10px;\n"
"")
        self.lblLogin = QLabel(self.widget)
        self.lblLogin.setObjectName(u"lblLogin")
        self.lblLogin.setGeometry(QRect(310, 160, 401, 71))
        font1 = QFont()
        font1.setFamilies([u"Nexa-Trial"])
        font1.setPointSize(40)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.lblLogin.setFont(font1)
        self.lblLogin.setStyleSheet(u"color: rgba(0, 0, 0, 220);")
        self.lineEdit_MastPassword = QLineEdit(self.widget)
        self.lineEdit_MastPassword.setObjectName(u"lineEdit_MastPassword")
        self.lineEdit_MastPassword.setGeometry(QRect(310, 390, 351, 30))
        font2 = QFont()
        font2.setFamilies([u".AppleSystemUIFont"])
        self.lineEdit_MastPassword.setFont(font2)
        self.lineEdit_MastPassword.setStyleSheet(u"background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.lineEdit_MastPassword.setEchoMode(QLineEdit.Password)
        self.lblMasterPassword = QLabel(self.widget)
        self.lblMasterPassword.setObjectName(u"lblMasterPassword")
        self.lblMasterPassword.setGeometry(QRect(320, 370, 111, 16))
        self.lblMasterPassword.setFont(font)
        self.lblMasterPassword.setStyleSheet(u"color:rgba(0, 0, 0, 200)")
        self.lineEdit_Email = QLineEdit(self.widget)
        self.lineEdit_Email.setObjectName(u"lineEdit_Email")
        self.lineEdit_Email.setGeometry(QRect(310, 240, 351, 30))
        self.lineEdit_Email.setFont(font2)
        self.lineEdit_Email.setStyleSheet(u"background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.lineEdit_Email.setEchoMode(QLineEdit.Normal)
        self.lblEmail = QLabel(self.widget)
        self.lblEmail.setObjectName(u"lblEmail")
        self.lblEmail.setGeometry(QRect(320, 220, 41, 16))
        self.lblEmail.setFont(font)
        self.lblEmail.setStyleSheet(u"color:rgba(0, 0, 0, 200)")
        self.btnCreate = QPushButton(self.widget)
        self.btnCreate.setObjectName(u"btnCreate")
        self.btnCreate.setGeometry(QRect(310, 650, 351, 32))
        font3 = QFont()
        font3.setFamilies([u"Nexa-Trial"])
        font3.setPointSize(16)
        font3.setItalic(False)
        self.btnCreate.setFont(font3)
        self.btnCreate.setStyleSheet(u"")
        self.lblNew = QLabel(self.widget)
        self.lblNew.setObjectName(u"lblNew")
        self.lblNew.setGeometry(QRect(540, 136, 91, 20))
        self.lblNew.setFont(font)
        self.lblNew.setStyleSheet(u"color: rgba(0, 0, 0, 170);")
        self.btnLogin = QPushButton(self.widget)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(640, 130, 111, 31))
        font4 = QFont()
        font4.setFamilies([u"Nexa-Trial"])
        font4.setPointSize(13)
        font4.setItalic(False)
        self.btnLogin.setFont(font4)
        self.btnLogin.setStyleSheet(u"")
        self.lblTitle = QLabel(self.widget)
        self.lblTitle.setObjectName(u"lblTitle")
        self.lblTitle.setGeometry(QRect(30, 120, 201, 61))
        font5 = QFont()
        font5.setFamilies([u"Nexa-Trial"])
        font5.setPointSize(50)
        font5.setBold(False)
        font5.setItalic(False)
        self.lblTitle.setFont(font5)
        self.lblTitle.setStyleSheet(u"color:rgba(255, 255, 255, 225);")
        self.lblSubTitle = QLabel(self.widget)
        self.lblSubTitle.setObjectName(u"lblSubTitle")
        self.lblSubTitle.setGeometry(QRect(30, 190, 251, 101))
        font6 = QFont()
        font6.setFamilies([u"Nexa-Trial"])
        font6.setPointSize(26)
        self.lblSubTitle.setFont(font6)
        self.lblSubTitle.setStyleSheet(u"color:rgba(255, 255, 255, 225)")
        self.lblSubTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lblSubTitle.setIndent(0)
        self.lineEdit_Name = QLineEdit(self.widget)
        self.lineEdit_Name.setObjectName(u"lineEdit_Name")
        self.lineEdit_Name.setGeometry(QRect(310, 310, 351, 30))
        self.lineEdit_Name.setFont(font2)
        self.lineEdit_Name.setStyleSheet(u"background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.lineEdit_Name.setEchoMode(QLineEdit.Normal)
        self.lblName = QLabel(self.widget)
        self.lblName.setObjectName(u"lblName")
        self.lblName.setGeometry(QRect(320, 290, 41, 16))
        self.lblName.setFont(font)
        self.lblName.setStyleSheet(u"color:rgba(0, 0, 0, 200)")
        self.lineEdit_MastPassword2 = QLineEdit(self.widget)
        self.lineEdit_MastPassword2.setObjectName(u"lineEdit_MastPassword2")
        self.lineEdit_MastPassword2.setGeometry(QRect(310, 500, 351, 30))
        self.lineEdit_MastPassword2.setFont(font2)
        self.lineEdit_MastPassword2.setStyleSheet(u"background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.lineEdit_MastPassword2.setEchoMode(QLineEdit.Password)
        self.passStrengthBar = QProgressBar(self.widget)
        self.passStrengthBar.setObjectName(u"passStrengthBar")
        self.passStrengthBar.setGeometry(QRect(310, 460, 351, 21))
        self.passStrengthBar.setStyleSheet(u"background-color: rgb(110, 77, 103);")
        self.passStrengthBar.setValue(24)
        self.passStrengthBar.setTextVisible(True)
        self.passStrengthBar.setInvertedAppearance(False)
        self.lblMasterPassword2 = QLabel(self.widget)
        self.lblMasterPassword2.setObjectName(u"lblMasterPassword2")
        self.lblMasterPassword2.setGeometry(QRect(320, 480, 161, 16))
        self.lblMasterPassword2.setFont(font)
        self.lblMasterPassword2.setStyleSheet(u"color:rgba(0, 0, 0, 200)")
        self.lineEdit_MastPassword2_2 = QLineEdit(self.widget)
        self.lineEdit_MastPassword2_2.setObjectName(u"lineEdit_MastPassword2_2")
        self.lineEdit_MastPassword2_2.setGeometry(QRect(310, 570, 351, 30))
        self.lineEdit_MastPassword2_2.setFont(font2)
        self.lineEdit_MastPassword2_2.setStyleSheet(u"background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.lineEdit_MastPassword2_2.setEchoMode(QLineEdit.Normal)
        self.lblPasswordHint = QLabel(self.widget)
        self.lblPasswordHint.setObjectName(u"lblPasswordHint")
        self.lblPasswordHint.setGeometry(QRect(320, 550, 141, 16))
        self.lblPasswordHint.setFont(font)
        self.lblPasswordHint.setStyleSheet(u"color:rgba(0, 0, 0, 200)")
        self.lblEmailDesc = QLabel(self.widget)
        self.lblEmailDesc.setObjectName(u"lblEmailDesc")
        self.lblEmailDesc.setGeometry(QRect(320, 270, 171, 16))
        font7 = QFont()
        font7.setFamilies([u"Nexa-Trial"])
        font7.setPointSize(12)
        self.lblEmailDesc.setFont(font7)
        self.lblEmailDesc.setStyleSheet(u"color: rgba(0, 0, 0, 120);")
        self.lblNameDesc = QLabel(self.widget)
        self.lblNameDesc.setObjectName(u"lblNameDesc")
        self.lblNameDesc.setGeometry(QRect(320, 340, 221, 16))
        self.lblNameDesc.setFont(font7)
        self.lblNameDesc.setStyleSheet(u"color: rgba(0, 0, 0, 120);")
        self.lblPassDesc = QLabel(self.widget)
        self.lblPassDesc.setObjectName(u"lblPassDesc")
        self.lblPassDesc.setGeometry(QRect(320, 420, 251, 41))
        self.lblPassDesc.setFont(font7)
        self.lblPassDesc.setStyleSheet(u"color: rgba(0, 0, 0, 120);")
        self.lblHintDesc = QLabel(self.widget)
        self.lblHintDesc.setObjectName(u"lblHintDesc")
        self.lblHintDesc.setGeometry(QRect(320, 590, 351, 41))
        self.lblHintDesc.setFont(font7)
        self.lblHintDesc.setStyleSheet(u"color: rgba(0, 0, 0, 120);")
        self.lblNameOpt = QLabel(self.widget)
        self.lblNameOpt.setObjectName(u"lblNameOpt")
        self.lblNameOpt.setGeometry(QRect(360, 290, 51, 16))
        font8 = QFont()
        font8.setFamilies([u".AppleSystemUIFont"])
        font8.setPointSize(9)
        self.lblNameOpt.setFont(font8)
        self.lblNameOpt.setStyleSheet(u"color: rgba(0, 0, 0, 120);")
        self.lblHintOpt = QLabel(self.widget)
        self.lblHintOpt.setObjectName(u"lblHintOpt")
        self.lblHintOpt.setGeometry(QRect(460, 550, 51, 16))
        self.lblHintOpt.setFont(font8)
        self.lblHintOpt.setStyleSheet(u"color: rgba(0, 0, 0, 120);")
        self.lblEmailReq = QLabel(self.widget)
        self.lblEmailReq.setObjectName(u"lblEmailReq")
        self.lblEmailReq.setGeometry(QRect(358, 220, 51, 16))
        self.lblEmailReq.setFont(font8)
        self.lblEmailReq.setStyleSheet(u"color: rgba(0, 0, 0, 120);")
        self.lblPassReq1 = QLabel(self.widget)
        self.lblPassReq1.setObjectName(u"lblPassReq1")
        self.lblPassReq1.setGeometry(QRect(435, 370, 51, 16))
        self.lblPassReq1.setFont(font8)
        self.lblPassReq1.setStyleSheet(u"color: rgba(0, 0, 0, 120);")
        self.lblPassReq2 = QLabel(self.widget)
        self.lblPassReq2.setObjectName(u"lblPassReq2")
        self.lblPassReq2.setGeometry(QRect(485, 480, 51, 16))
        self.lblPassReq2.setFont(font8)
        self.lblPassReq2.setStyleSheet(u"color: rgba(0, 0, 0, 120);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.rightBox.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.leftBox.setText("")
        self.lblLogin.setText(QCoreApplication.translate("Form", u"create your pass.me", None))
        self.lineEdit_MastPassword.setPlaceholderText("")
        self.lblMasterPassword.setText(QCoreApplication.translate("Form", u"master password", None))
        self.lineEdit_Email.setPlaceholderText("")
        self.lblEmail.setText(QCoreApplication.translate("Form", u"email", None))
        self.btnCreate.setText(QCoreApplication.translate("Form", u"create account", None))
        self.lblNew.setText(QCoreApplication.translate("Form", u"exisiting user?", None))
        self.btnLogin.setText(QCoreApplication.translate("Form", u"log in", None))
        self.lblTitle.setText(QCoreApplication.translate("Form", u"pass.me", None))
        self.lblSubTitle.setText(QCoreApplication.translate("Form", u"<html><head/><body>\n"
"<p style=\"line-height:0.4\"><span>\n"
"welcome to the \n"
"</span></p>\n"
"<p style=\"line-height:0.4\"><span>\n"
"pass.me app\n"
"</span></p>\n"
"</body></html>", None))
        self.lineEdit_Name.setPlaceholderText("")
        self.lblName.setText(QCoreApplication.translate("Form", u"name", None))
        self.lineEdit_MastPassword2.setPlaceholderText("")
        self.lblMasterPassword2.setText(QCoreApplication.translate("Form", u"re-type master password", None))
        self.lineEdit_MastPassword2_2.setPlaceholderText("")
        self.lblPasswordHint.setText(QCoreApplication.translate("Form", u"master password hint", None))
        self.lblEmailDesc.setText(QCoreApplication.translate("Form", u"your email is used to login.", None))
        self.lblNameDesc.setText(QCoreApplication.translate("Form", u"what we will call you.", None))
        self.lblPassDesc.setText(QCoreApplication.translate("Form", u"used to access your pass.me. \n"
"NOTE: if forgotten, cannot be recovered", None))
        self.lblHintDesc.setText(QCoreApplication.translate("Form", u"can help you remeber your master password if forgotten", None))
        self.lblNameOpt.setText(QCoreApplication.translate("Form", u"(optional)", None))
        self.lblHintOpt.setText(QCoreApplication.translate("Form", u"(optional)", None))
        self.lblEmailReq.setText(QCoreApplication.translate("Form", u"(required)", None))
        self.lblPassReq1.setText(QCoreApplication.translate("Form", u"(required)", None))
        self.lblPassReq2.setText(QCoreApplication.translate("Form", u"(required)", None))
    # retranslateUi
    
if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        try:
           sys.exit(app.exec())
        except SystemExit:
         print ("Closing window")




from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget, QProgressBar)
from PySide6 import QtCore, QtGui, QtWidgets
import sys

class Ui_Login(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(834, 479)
        Form.setMinimumSize(QSize(834, 479))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(834, 479))
        font = QFont()
        font.setFamilies([u"Nexa-Trial"])
        self.widget.setFont(font)
        self.widget.setStyleSheet(u"QPushButton#btnLogin{\n"
"	background-color:rgba(148, 105, 141, 255);\n"
"	color:rgba(255, 255, 255, 220);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#btnLogin:pressed{\n"
"\n"
"	background-color:rgba(74, 53, 70, 255);\n"
"\n"
"}\n"
"QPushButton#btnLogin:hover{\n"
"	background-color:rgba(111, 77, 104, 255);\n"
"}\n"
"QPushButton#btnCreate{\n"
"	background-color:rgba(170, 170, 170, 255);\n"
"	color:rgba(255, 255, 255, 200);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#btnCreate:hover{\n"
"	background-color:rgba(140, 140, 140, 255);\n"
"}\n"
"QWidget#leftBox{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, 		stop:0 rgba(0, 0, 0, 255), stop:1 rgba(92, 61, 88, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"QWidget#rightBox{\n"
"	background-color: rgba(255, 255, 255, 255);\n"
"	border-radius: 10px\n"
"}")
        self.leftBox = QWidget(self.widget)
        self.leftBox.setObjectName(u"leftBox")
        self.leftBox.setGeometry(QRect(12, 3, 281, 451))
        self.leftBox.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.leftBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, -1, -1, -1)
        self.verticalSpacer_5 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lblTitle = QLabel(self.leftBox)
        self.lblTitle.setObjectName(u"lblTitle")
        self.lblTitle.setMaximumSize(QSize(16777215, 60))
        font1 = QFont()
        font1.setFamilies([u"Nexa-Trial"])
        font1.setPointSize(50)
        font1.setBold(False)
        font1.setItalic(False)
        self.lblTitle.setFont(font1)
        self.lblTitle.setStyleSheet(u"color:rgba(255, 255, 255, 225);")

        self.verticalLayout_2.addWidget(self.lblTitle)

        self.lblSubTitle = QLabel(self.leftBox)
        self.lblSubTitle.setObjectName(u"lblSubTitle")
        font2 = QFont()
        font2.setFamilies([u"Nexa-Trial"])
        font2.setPointSize(26)
        self.lblSubTitle.setFont(font2)
        self.lblSubTitle.setStyleSheet(u"color:rgba(255, 255, 255, 225)")
        self.lblSubTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lblSubTitle.setIndent(0)

        self.verticalLayout_2.addWidget(self.lblSubTitle)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.rightBox = QWidget(self.widget)
        self.rightBox.setObjectName(u"rightBox")
        self.rightBox.setGeometry(QRect(280, 40, 501, 381))
        self.gridLayout_2 = QGridLayout(self.rightBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(30, 20, -1, -1)
        self.lblMasterPassword = QLabel(self.rightBox)
        self.lblMasterPassword.setObjectName(u"lblMasterPassword")
        self.lblMasterPassword.setFont(font)
        self.lblMasterPassword.setStyleSheet(u"color:rgba(0, 0, 0, 200)")

        self.gridLayout_2.addWidget(self.lblMasterPassword, 9, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 12, 0, 1, 1)

        self.lblEmail = QLabel(self.rightBox)
        self.lblEmail.setObjectName(u"lblEmail")
        self.lblEmail.setFont(font)
        self.lblEmail.setStyleSheet(u"color:rgba(0, 0, 0, 200)")

        self.gridLayout_2.addWidget(self.lblEmail, 5, 0, 1, 1)

        self.lblMassPassHint = QLabel(self.rightBox)
        self.lblMassPassHint.setObjectName(u"lblMassPassHint")
        font3 = QFont()
        font3.setFamilies([u"Nexa-Trial"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        self.lblMassPassHint.setFont(font3)
        self.lblMassPassHint.setStyleSheet(u"color: rgba(0, 0, 0, 200);")

        self.gridLayout_2.addWidget(self.lblMassPassHint, 11, 0, 1, 2)

        self.btnLogin = QPushButton(self.rightBox)
        self.btnLogin.setObjectName(u"btnLogin")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLogin.sizePolicy().hasHeightForWidth())
        self.btnLogin.setSizePolicy(sizePolicy)
        self.btnLogin.setMinimumSize(QSize(350, 30))
        self.btnLogin.setBaseSize(QSize(0, 0))
        font4 = QFont()
        font4.setFamilies([u"Nexa-Trial"])
        font4.setPointSize(16)
        font4.setItalic(False)
        self.btnLogin.setFont(font4)
        self.btnLogin.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.btnLogin, 13, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.lblHelp = QLabel(self.rightBox)
        self.lblHelp.setObjectName(u"lblHelp")
        font5 = QFont()
        font5.setFamilies([u"Nexa-Trial"])
        font5.setPointSize(12)
        font5.setItalic(False)
        self.lblHelp.setFont(font5)
        self.lblHelp.setStyleSheet(u"color: rgba(0, 0, 0, 200);")
        self.lblHelp.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblHelp, 11, 2, 1, 1)

        self.lineEdit_MastPassword = QLineEdit(self.rightBox)
        self.lineEdit_MastPassword.setObjectName(u"lineEdit_MastPassword")
        self.lineEdit_MastPassword.setMinimumSize(QSize(350, 30))
        font6 = QFont()
        font6.setFamilies([u".AppleSystemUIFont"])
        self.lineEdit_MastPassword.setFont(font6)
        self.lineEdit_MastPassword.setStyleSheet(u"background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.lineEdit_MastPassword.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.lineEdit_MastPassword, 10, 0, 1, 3)

        self.btnCreate = QPushButton(self.rightBox)
        self.btnCreate.setObjectName(u"btnCreate")
        self.btnCreate.setMinimumSize(QSize(110, 30))
        font7 = QFont()
        font7.setFamilies([u"Nexa-Trial"])
        font7.setPointSize(13)
        font7.setItalic(False)
        self.btnCreate.setFont(font7)
        self.btnCreate.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.btnCreate, 2, 3, 1, 1)

        self.lblLogin = QLabel(self.rightBox)
        self.lblLogin.setObjectName(u"lblLogin")
        font8 = QFont()
        font8.setFamilies([u"Nexa-Trial"])
        font8.setPointSize(40)
        font8.setBold(True)
        font8.setItalic(False)
        font8.setUnderline(False)
        font8.setStrikeOut(False)
        self.lblLogin.setFont(font8)
        self.lblLogin.setStyleSheet(u"color: rgba(0, 0, 0, 220);")

        self.gridLayout_2.addWidget(self.lblLogin, 3, 0, 1, 4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 14, 0, 1, 1)

        self.lineEdit_Email = QLineEdit(self.rightBox)
        self.lineEdit_Email.setObjectName(u"lineEdit_Email")
        self.lineEdit_Email.setMinimumSize(QSize(350, 30))
        self.lineEdit_Email.setFont(font6)
        self.lineEdit_Email.setStyleSheet(u"background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.lineEdit_Email.setEchoMode(QLineEdit.Normal)

        self.gridLayout_2.addWidget(self.lineEdit_Email, 6, 0, 1, 3)

        self.lblNew = QLabel(self.rightBox)
        self.lblNew.setObjectName(u"lblNew")
        self.lblNew.setMinimumSize(QSize(110, 0))
        self.lblNew.setFont(font)
        self.lblNew.setStyleSheet(u"color: rgba(0, 0, 0, 170);")

        self.gridLayout_2.addWidget(self.lblNew, 2, 2, 1, 1)

        self.rightBox.raise_()
        self.leftBox.raise_()

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi
    
    # @mousePress and @moveWindow used to enable movement of the frameless window
    # When the mouse is clicked on the window, the mouses position is tracked and the window is moved accordingly

        
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblTitle.setText(QCoreApplication.translate("Form", u"pass.me", None))
        self.lblSubTitle.setText(QCoreApplication.translate("Form", u"<html><head/><body>\n"
"<p style=\"line-height:0.4\"><span>\n"
"welcome to the \n"
"</span></p>\n"
"<p style=\"line-height:0.4\"><span>\n"
"pass.me app\n"
"</span></p>\n"
"</body></html>", None))
        self.lblMasterPassword.setText(QCoreApplication.translate("Form", u"master password", None))
        self.lblEmail.setText(QCoreApplication.translate("Form", u"email", None))
        self.lblMassPassHint.setText(QCoreApplication.translate("Form", u"get master password hint", None))
        self.btnLogin.setText(QCoreApplication.translate("Form", u"log in", None))
        self.lblHelp.setText(QCoreApplication.translate("Form", u"help?", None))
        self.lineEdit_MastPassword.setPlaceholderText("")
        self.btnCreate.setText(QCoreApplication.translate("Form", u"create account", None))
        self.lblLogin.setText(QCoreApplication.translate("Form", u"log in to pass.me", None))
        self.lineEdit_Email.setPlaceholderText("")
        self.lblNew.setText(QCoreApplication.translate("Form", u"new to pass.me?", None))
    # retranslateUi        

#if __name__ == "__main__":
 #   app = QtWidgets.QApplication(sys.argv)
#    Form = QtWidgets.QWidget()
#    ui = Ui_Login()
#    ui.setupUi(Form)
#    Form.show()
#    try:
#        sys.exit(app.exec())
#    except SystemExit:
#        print ("Closing window")
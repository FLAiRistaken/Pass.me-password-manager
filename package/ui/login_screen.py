

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)


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
"}\n"
"QPushButton#btnClose{\n"
"	color:rgba(255, 255, 255, 220);\n"
"}\n"
"QPushButton#btnClose:pressed{\n"
"	color: rgba(126, 126, 126, 220);\n"
"\n"
"}\n"
"QPushButton#btnClose:hover{\n"
"	"
                        "color: rgba(190, 190, 190, 220);\n"
"}\n"
"QWidget#rightBox_Hint{\n"
"	background-color: rgba(255, 255, 255, 255);\n"
"	border-radius: 10px\n"
"}\n"
"QPushButton#btnGetHint{\n"
"	background-color:rgba(148, 105, 141, 255);\n"
"	color:rgba(255, 255, 255, 220);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#btnGetHint:pressed{\n"
"\n"
"	background-color:rgba(74, 53, 70, 255);\n"
"\n"
"}\n"
"QPushButton#btnGetHint:hover{\n"
"	background-color:rgba(111, 77, 104, 255);\n"
"}")
        self.leftBox = QWidget(self.widget)
        self.leftBox.setObjectName(u"leftBox")
        self.leftBox.setGeometry(QRect(12, 3, 281, 451))
        self.leftBox.setMinimumSize(QSize(281, 451))
        self.leftBox.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.leftBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, -1, -1)
        self.btnClose = QPushButton(self.leftBox)
        self.btnClose.setObjectName(u"btnClose")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy)
        self.btnClose.setMinimumSize(QSize(5, 0))
        font1 = QFont()
        font1.setFamilies([u"Nexa-Trial"])
        font1.setPointSize(16)
        self.btnClose.setFont(font1)
        self.btnClose.setStyleSheet(u"border: none;")

        self.verticalLayout.addWidget(self.btnClose)

        self.verticalSpacer_5 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lblTitle = QLabel(self.leftBox)
        self.lblTitle.setObjectName(u"lblTitle")
        self.lblTitle.setMaximumSize(QSize(16777215, 60))
        font2 = QFont()
        font2.setFamilies([u"Nexa-Trial"])
        font2.setPointSize(50)
        font2.setBold(False)
        font2.setItalic(False)
        self.lblTitle.setFont(font2)
        self.lblTitle.setStyleSheet(u"color:rgba(255, 255, 255, 225);")

        self.verticalLayout_2.addWidget(self.lblTitle)

        self.lblSubTitle = QLabel(self.leftBox)
        self.lblSubTitle.setObjectName(u"lblSubTitle")
        font3 = QFont()
        font3.setFamilies([u"Nexa-Trial"])
        font3.setPointSize(26)
        self.lblSubTitle.setFont(font3)
        self.lblSubTitle.setStyleSheet(u"color:rgba(255, 255, 255, 225)")
        self.lblSubTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lblSubTitle.setIndent(0)

        self.verticalLayout_2.addWidget(self.lblSubTitle)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.rightBox_Hint = QWidget(self.widget)
        self.rightBox_Hint.setObjectName(u"rightBox_Hint")
        self.rightBox_Hint.setEnabled(False)
        self.rightBox_Hint.setGeometry(QRect(280, 40, 501, 381))
        self.rightBox_Hint.setMinimumSize(QSize(501, 381))
        self.gridLayout_5 = QGridLayout(self.rightBox_Hint)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(30, 20, -1, -1)
        self.verticalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_5.addItem(self.verticalSpacer_12, 8, 0, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_5.addItem(self.verticalSpacer_14, 3, 0, 1, 1)

        self.lineEdit_Email_Hint = QLineEdit(self.rightBox_Hint)
        self.lineEdit_Email_Hint.setObjectName(u"lineEdit_Email_Hint")
        self.lineEdit_Email_Hint.setMinimumSize(QSize(350, 30))
        font4 = QFont()
        font4.setFamilies([u".AppleSystemUIFont"])
        self.lineEdit_Email_Hint.setFont(font4)
        self.lineEdit_Email_Hint.setStyleSheet(u"background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.lineEdit_Email_Hint.setEchoMode(QLineEdit.Normal)

        self.gridLayout_5.addWidget(self.lineEdit_Email_Hint, 5, 0, 1, 1)

        self.lblEmail_Hint = QLabel(self.rightBox_Hint)
        self.lblEmail_Hint.setObjectName(u"lblEmail_Hint")
        self.lblEmail_Hint.setFont(font)
        self.lblEmail_Hint.setStyleSheet(u"color:rgba(0, 0, 0, 200)")

        self.gridLayout_5.addWidget(self.lblEmail_Hint, 4, 0, 1, 1)

        self.lblMassHint = QLabel(self.rightBox_Hint)
        self.lblMassHint.setObjectName(u"lblMassHint")
        font5 = QFont()
        font5.setFamilies([u"Nexa-Trial"])
        font5.setPointSize(40)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setStrikeOut(False)
        self.lblMassHint.setFont(font5)
        self.lblMassHint.setStyleSheet(u"color: rgba(0, 0, 0, 220);")

        self.gridLayout_5.addWidget(self.lblMassHint, 2, 0, 1, 3)

        self.btnBack = QPushButton(self.rightBox_Hint)
        self.btnBack.setObjectName(u"btnBack")
        sizePolicy.setHeightForWidth(self.btnBack.sizePolicy().hasHeightForWidth())
        self.btnBack.setSizePolicy(sizePolicy)
        self.btnBack.setMinimumSize(QSize(5, 0))
        font6 = QFont()
        font6.setFamilies([u"Waseem"])
        font6.setPointSize(25)
        self.btnBack.setFont(font6)
        self.btnBack.setStyleSheet(u"border: none;\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_5.addWidget(self.btnBack, 0, 0, 1, 3)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_13, 11, 0, 1, 1)

        self.lblError = QLabel(self.rightBox_Hint)
        self.lblError.setObjectName(u"lblError")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lblError.sizePolicy().hasHeightForWidth())
        self.lblError.setSizePolicy(sizePolicy1)
        self.lblError.setMinimumSize(QSize(0, 40))
        font7 = QFont()
        font7.setFamilies([u"Nexa-Trial"])
        font7.setPointSize(12)
        self.lblError.setFont(font7)
        self.lblError.setStyleSheet(u"color: rgba(0, 0, 0 ,180); ")

        self.gridLayout_5.addWidget(self.lblError, 6, 0, 1, 1)

        self.btnGetHint = QPushButton(self.rightBox_Hint)
        self.btnGetHint.setObjectName(u"btnGetHint")
        sizePolicy.setHeightForWidth(self.btnGetHint.sizePolicy().hasHeightForWidth())
        self.btnGetHint.setSizePolicy(sizePolicy)
        self.btnGetHint.setMinimumSize(QSize(350, 30))
        self.btnGetHint.setBaseSize(QSize(0, 0))
        font8 = QFont()
        font8.setFamilies([u"Nexa-Trial"])
        font8.setPointSize(16)
        font8.setItalic(False)
        self.btnGetHint.setFont(font8)
        self.btnGetHint.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.btnGetHint, 10, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 5, 2, 1, 1)

        self.rightBox = QWidget(self.widget)
        self.rightBox.setObjectName(u"rightBox")
        self.rightBox.setGeometry(QRect(280, 40, 501, 381))
        self.rightBox.setMinimumSize(QSize(501, 381))
        self.gridLayout_2 = QGridLayout(self.rightBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(30, 20, -1, -1)
        self.lblNew = QLabel(self.rightBox)
        self.lblNew.setObjectName(u"lblNew")
        self.lblNew.setMinimumSize(QSize(110, 0))
        self.lblNew.setFont(font)
        self.lblNew.setStyleSheet(u"color: rgba(0, 0, 0, 170);")

        self.gridLayout_2.addWidget(self.lblNew, 2, 1, 1, 1)

        self.lblHelp = QLabel(self.rightBox)
        self.lblHelp.setObjectName(u"lblHelp")
        font9 = QFont()
        font9.setFamilies([u"Nexa-Trial"])
        font9.setPointSize(12)
        font9.setItalic(False)
        self.lblHelp.setFont(font9)
        self.lblHelp.setStyleSheet(u"color: rgba(0, 0, 0, 200);")
        self.lblHelp.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblHelp, 9, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 12, 0, 1, 1)

        self.btnLogin = QPushButton(self.rightBox)
        self.btnLogin.setObjectName(u"btnLogin")
        sizePolicy.setHeightForWidth(self.btnLogin.sizePolicy().hasHeightForWidth())
        self.btnLogin.setSizePolicy(sizePolicy)
        self.btnLogin.setMinimumSize(QSize(350, 30))
        self.btnLogin.setBaseSize(QSize(0, 0))
        self.btnLogin.setFont(font8)
        self.btnLogin.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.btnLogin, 11, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 10, 0, 1, 1)

        self.lblEmail = QLabel(self.rightBox)
        self.lblEmail.setObjectName(u"lblEmail")
        self.lblEmail.setFont(font)
        self.lblEmail.setStyleSheet(u"color:rgba(0, 0, 0, 200)")

        self.gridLayout_2.addWidget(self.lblEmail, 5, 0, 1, 1)

        self.lineEdit_Email = QLineEdit(self.rightBox)
        self.lineEdit_Email.setObjectName(u"lineEdit_Email")
        self.lineEdit_Email.setMinimumSize(QSize(350, 30))
        self.lineEdit_Email.setFont(font4)
        self.lineEdit_Email.setStyleSheet(u"background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.lineEdit_Email.setEchoMode(QLineEdit.Normal)

        self.gridLayout_2.addWidget(self.lineEdit_Email, 6, 0, 1, 2)

        self.btnCreate = QPushButton(self.rightBox)
        self.btnCreate.setObjectName(u"btnCreate")
        self.btnCreate.setMinimumSize(QSize(110, 30))
        font10 = QFont()
        font10.setFamilies([u"Nexa-Trial"])
        font10.setPointSize(13)
        font10.setItalic(False)
        self.btnCreate.setFont(font10)
        self.btnCreate.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.btnCreate, 2, 2, 1, 1)

        self.lineEdit_MastPassword = QLineEdit(self.rightBox)
        self.lineEdit_MastPassword.setObjectName(u"lineEdit_MastPassword")
        self.lineEdit_MastPassword.setMinimumSize(QSize(350, 30))
        self.lineEdit_MastPassword.setFont(font4)
        self.lineEdit_MastPassword.setStyleSheet(u"background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.lineEdit_MastPassword.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.lineEdit_MastPassword, 8, 0, 1, 2)

        self.lblLogin = QLabel(self.rightBox)
        self.lblLogin.setObjectName(u"lblLogin")
        self.lblLogin.setFont(font5)
        self.lblLogin.setStyleSheet(u"color: rgba(0, 0, 0, 220);")

        self.gridLayout_2.addWidget(self.lblLogin, 3, 0, 1, 3)

        self.btnHint = QPushButton(self.rightBox)
        self.btnHint.setObjectName(u"btnHint")
        self.btnHint.setFont(font)
        self.btnHint.setStyleSheet(u"border: none;\n"
"color: rgba(0, 0, 0, 200);")
        self.btnHint.setFlat(False)

        self.gridLayout_2.addWidget(self.btnHint, 9, 0, 1, 1, Qt.AlignLeft)

        self.lblMasterPassword = QLabel(self.rightBox)
        self.lblMasterPassword.setObjectName(u"lblMasterPassword")
        self.lblMasterPassword.setFont(font)
        self.lblMasterPassword.setStyleSheet(u"color:rgba(0, 0, 0, 200)")

        self.gridLayout_2.addWidget(self.lblMasterPassword, 7, 0, 1, 1)

        self.rightBox_Hint.raise_()
        self.rightBox.raise_()
        self.leftBox.raise_()

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btnClose.setText(QCoreApplication.translate("Form", u"X", None))
        self.lblTitle.setText(QCoreApplication.translate("Form", u"pass.me", None))
        self.lblSubTitle.setText(QCoreApplication.translate("Form", u"<html><head/><body>\n"
"<p style=\"line-height:0.4\"><span>\n"
"welcome to the \n"
"</span></p>\n"
"<p style=\"line-height:0.4\"><span>\n"
"pass.me app\n"
"</span></p>\n"
"</body></html>", None))
        self.lineEdit_Email_Hint.setPlaceholderText("")
        self.lblEmail_Hint.setText(QCoreApplication.translate("Form", u"email", None))
        self.lblMassHint.setText(QCoreApplication.translate("Form", u"master password hint", None))
        self.btnBack.setText(QCoreApplication.translate("Form", u"<", None))
        self.lblError.setText(QCoreApplication.translate("Form", u"\n"
"<html><head/><body>\n"
"<p style=\"line-height:0.4\"><span>\n"
"enter the email for your account. \n"
"</span></p>\n"
"<p style=\"line-height:0.4\"><span>\n"
"if a matching record is found, an email containing your hint will be sent\n"
"</span></p>\n"
"</body></html>", None))
        self.btnGetHint.setText(QCoreApplication.translate("Form", u"get hint", None))
        self.lblNew.setText(QCoreApplication.translate("Form", u"new to pass.me?", None))
        self.lblHelp.setText(QCoreApplication.translate("Form", u"help?", None))
        self.btnLogin.setText(QCoreApplication.translate("Form", u"log in", None))
        self.lblEmail.setText(QCoreApplication.translate("Form", u"email", None))
        self.lineEdit_Email.setPlaceholderText("")
        self.btnCreate.setText(QCoreApplication.translate("Form", u"create account", None))
        self.lineEdit_MastPassword.setPlaceholderText("")
        self.lblLogin.setText(QCoreApplication.translate("Form", u"log in to pass.me", None))
        self.btnHint.setText(QCoreApplication.translate("Form", u"get master password hint", None))
        self.lblMasterPassword.setText(QCoreApplication.translate("Form", u"master password", None))
    # retranslateUi


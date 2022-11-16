

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Create(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(824, 699)
        Form.setMinimumSize(QSize(824, 699))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(800, 675))
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
"}\n"
"QWidget#leftBox{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, 		stop:0 rgba(0, 0, 0, 255), stop:1 rgba(92, 61, 88, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"QWidget#rightBox{\n"
"	background-color: rgba(255, 255, 255, 255);\n"
"	b"
                        "order-radius: 10px\n"
"}")
        self.leftBox = QWidget(self.widget)
        self.leftBox.setObjectName(u"leftBox")
        self.leftBox.setGeometry(QRect(0, 0, 281, 680))
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
        self.rightBox.setGeometry(QRect(270, 40, 501, 610))
        self.gridLayout_2 = QGridLayout(self.rightBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(30, 20, -1, -1)
        self.lblName = QLabel(self.rightBox)
        self.lblName.setObjectName(u"lblName")
        self.lblName.setFont(font)
        self.lblName.setStyleSheet(u"color:rgba(0, 0, 0, 200)")

        self.gridLayout_2.addWidget(self.lblName, 9, 0, 1, 1)

        self.lblCreate = QLabel(self.rightBox)
        self.lblCreate.setObjectName(u"lblCreate")
        font3 = QFont()
        font3.setFamilies([u"Nexa-Trial"])
        font3.setPointSize(40)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        self.lblCreate.setFont(font3)
        self.lblCreate.setStyleSheet(u"color: rgba(0, 0, 0, 220);")

        self.gridLayout_2.addWidget(self.lblCreate, 3, 0, 2, 4)

        self.lineEdit_Name = QLineEdit(self.rightBox)
        self.lineEdit_Name.setObjectName(u"lineEdit_Name")
        self.lineEdit_Name.setMinimumSize(QSize(350, 30))
        font4 = QFont()
        font4.setFamilies([u".AppleSystemUIFont"])
        self.lineEdit_Name.setFont(font4)
        self.lineEdit_Name.setStyleSheet(u"background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.lineEdit_Name.setEchoMode(QLineEdit.Normal)

        self.gridLayout_2.addWidget(self.lineEdit_Name, 10, 0, 1, 1)

        self.lblMasterPassword2 = QLabel(self.rightBox)
        self.lblMasterPassword2.setObjectName(u"lblMasterPassword2")
        self.lblMasterPassword2.setFont(font)
        self.lblMasterPassword2.setStyleSheet(u"color:rgba(0, 0, 0, 200)")

        self.gridLayout_2.addWidget(self.lblMasterPassword2, 18, 0, 1, 2)

        self.passStrengthBar = QProgressBar(self.rightBox)
        self.passStrengthBar.setObjectName(u"passStrengthBar")
        self.passStrengthBar.setStyleSheet(u"background-color: rgb(110, 77, 103);")
        self.passStrengthBar.setValue(24)
        self.passStrengthBar.setTextVisible(True)
        self.passStrengthBar.setInvertedAppearance(False)

        self.gridLayout_2.addWidget(self.passStrengthBar, 17, 0, 1, 1)

        self.lineEdit_Email = QLineEdit(self.rightBox)
        self.lineEdit_Email.setObjectName(u"lineEdit_Email")
        self.lineEdit_Email.setMinimumSize(QSize(350, 30))
        self.lineEdit_Email.setFont(font4)
        self.lineEdit_Email.setStyleSheet(u"background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.lineEdit_Email.setEchoMode(QLineEdit.Normal)

        self.gridLayout_2.addWidget(self.lineEdit_Email, 8, 0, 1, 2)

        self.lblHintDesc = QLabel(self.rightBox)
        self.lblHintDesc.setObjectName(u"lblHintDesc")
        font5 = QFont()
        font5.setFamilies([u"Nexa-Trial"])
        font5.setPointSize(12)
        self.lblHintDesc.setFont(font5)
        self.lblHintDesc.setStyleSheet(u"color: rgba(0, 0, 0, 120);")

        self.gridLayout_2.addWidget(self.lblHintDesc, 22, 0, 1, 3)

        self.lineEdit_PassHint = QLineEdit(self.rightBox)
        self.lineEdit_PassHint.setObjectName(u"lineEdit_PassHint")
        self.lineEdit_PassHint.setMinimumSize(QSize(350, 30))
        self.lineEdit_PassHint.setFont(font4)
        self.lineEdit_PassHint.setStyleSheet(u"background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.lineEdit_PassHint.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.lineEdit_PassHint, 21, 0, 1, 1)

        self.lblMasterPassword = QLabel(self.rightBox)
        self.lblMasterPassword.setObjectName(u"lblMasterPassword")
        self.lblMasterPassword.setFont(font)
        self.lblMasterPassword.setStyleSheet(u"color:rgba(0, 0, 0, 200)")

        self.gridLayout_2.addWidget(self.lblMasterPassword, 13, 0, 1, 2)

        self.lblNew = QLabel(self.rightBox)
        self.lblNew.setObjectName(u"lblNew")
        self.lblNew.setMinimumSize(QSize(95, 32))
        self.lblNew.setFont(font)
        self.lblNew.setStyleSheet(u"color: rgba(0, 0, 0, 170);")

        self.gridLayout_2.addWidget(self.lblNew, 1, 2, 1, 1)

        self.lblEmail = QLabel(self.rightBox)
        self.lblEmail.setObjectName(u"lblEmail")
        self.lblEmail.setFont(font)
        self.lblEmail.setStyleSheet(u"color:rgba(0, 0, 0, 200)")

        self.gridLayout_2.addWidget(self.lblEmail, 6, 0, 1, 1)

        self.lblPassDesc = QLabel(self.rightBox)
        self.lblPassDesc.setObjectName(u"lblPassDesc")
        self.lblPassDesc.setFont(font5)
        self.lblPassDesc.setStyleSheet(u"color: rgba(0, 0, 0, 120);")

        self.gridLayout_2.addWidget(self.lblPassDesc, 15, 0, 1, 3)

        self.btnLogin = QPushButton(self.rightBox)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setMinimumSize(QSize(110, 30))
        font6 = QFont()
        font6.setFamilies([u"Nexa-Trial"])
        font6.setPointSize(13)
        font6.setItalic(False)
        self.btnLogin.setFont(font6)
        self.btnLogin.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.btnLogin, 1, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 31, 0, 1, 1)

        self.lineEdit_MastPassword2 = QLineEdit(self.rightBox)
        self.lineEdit_MastPassword2.setObjectName(u"lineEdit_MastPassword2")
        self.lineEdit_MastPassword2.setMinimumSize(QSize(350, 30))
        self.lineEdit_MastPassword2.setFont(font4)
        self.lineEdit_MastPassword2.setStyleSheet(u"background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.lineEdit_MastPassword2.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.lineEdit_MastPassword2, 19, 0, 1, 1)

        self.btnCreate = QPushButton(self.rightBox)
        self.btnCreate.setObjectName(u"btnCreate")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCreate.sizePolicy().hasHeightForWidth())
        self.btnCreate.setSizePolicy(sizePolicy)
        self.btnCreate.setMinimumSize(QSize(350, 30))
        self.btnCreate.setBaseSize(QSize(0, 0))
        font7 = QFont()
        font7.setFamilies([u"Nexa-Trial"])
        font7.setPointSize(16)
        font7.setItalic(False)
        self.btnCreate.setFont(font7)
        self.btnCreate.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.btnCreate, 30, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 5, 0, 1, 1)

        self.lineEdit_MastPassword = QLineEdit(self.rightBox)
        self.lineEdit_MastPassword.setObjectName(u"lineEdit_MastPassword")
        self.lineEdit_MastPassword.setMinimumSize(QSize(350, 30))
        self.lineEdit_MastPassword.setFont(font4)
        self.lineEdit_MastPassword.setStyleSheet(u"background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.lineEdit_MastPassword.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.lineEdit_MastPassword, 14, 0, 1, 2)

        self.lblPasswordHint = QLabel(self.rightBox)
        self.lblPasswordHint.setObjectName(u"lblPasswordHint")
        self.lblPasswordHint.setFont(font)
        self.lblPasswordHint.setStyleSheet(u"color:rgba(0, 0, 0, 200)")

        self.gridLayout_2.addWidget(self.lblPasswordHint, 20, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 28, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 32, 0, 1, 1)

        self.rightBox.raise_()
        self.leftBox.raise_()

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

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
        self.lblName.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>name <span style=\" font-family:'Arial'; font-size:9pt; color:#a3a3a3;\">(optional)</span></p></body></html>", None))
        self.lblCreate.setText(QCoreApplication.translate("Form", u"create your pass.me", None))
        self.lineEdit_Name.setPlaceholderText("")
        self.lblMasterPassword2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>re-type master password <span style=\" font-family:'Arial'; font-size:9pt; color:#a3a3a3;\">(required)</span></p></body></html>", None))
        self.lineEdit_Email.setPlaceholderText("")
        self.lblHintDesc.setText(QCoreApplication.translate("Form", u"can help you remeber your master password if forgotten", None))
        self.lineEdit_PassHint.setPlaceholderText("")
        self.lblMasterPassword.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>master password <span style=\" font-family:'Arial'; font-size:9pt; color:#a3a3a3;\">(required)</span></p></body></html>", None))
        self.lblNew.setText(QCoreApplication.translate("Form", u"exisiting user?", None))
        self.lblEmail.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>email <span style=\" font-family:'Arial'; font-size:9pt; color:#a3a3a3;\">(required)</span></p></body></html>", None))
        self.lblPassDesc.setText(QCoreApplication.translate("Form", u"used to access your pass.me. \n"
"NOTE: if forgotten, cannot be recovered", None))
        self.btnLogin.setText(QCoreApplication.translate("Form", u"log in", None))
        self.lineEdit_MastPassword2.setPlaceholderText("")
        self.btnCreate.setText(QCoreApplication.translate("Form", u"create account", None))
        self.lineEdit_MastPassword.setPlaceholderText("")
        self.lblPasswordHint.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>master password hint <span style=\" font-family:'Arial'; font-size:9pt; color:#a3a3a3;\">(optional)</span></p></body></html>", None))
    # retranslateUi

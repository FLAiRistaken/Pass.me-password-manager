# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_identity_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QToolButton, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(518, 793)
        self.gridLayout_4 = QGridLayout(Form)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(500, 775))
        self.widget.setMaximumSize(QSize(500, 800))
        self.widget.setStyleSheet(u"QToolButton{\n"
"	border-radius:6px;\n"
"	color: rgba(255, 255, 255, 220);\n"
"	padding: 10px;\n"
"}\n"
"QToolButton:hover{\n"
"	background-color: rgba(152, 108, 144, 115);\n"
"}\n"
"QPushButton#btnClose{\n"
"	color:rgba(255, 255, 255, 220);\n"
"}\n"
"QPushButton#btnClose:pressed{\n"
"	color: rgba(126, 126, 126, 220);\n"
"\n"
"}\n"
"QPushButton#btnClose:hover{\n"
"	color: rgba(190, 190, 190, 220);\n"
"}\n"
"\n"
"QWidget {\n"
"	background-color: rgba(32, 32, 32, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#text_fields_group {\n"
"	padding: 5px;\n"
"}\n"
"QFrame#main_data_entry_group{\n"
"	background-color: rgba(70, 70, 70, 255);\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"QLabel#lblNewItemTitle {\n"
"	background-color: rgba(255, 255, 255, 25);\n"
"	padding: 5px;\n"
"}\n"
"\n"
"")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout_2.setContentsMargins(20, 12, 20, 12)
        self.btn_back = QPushButton(self.widget)
        self.btn_back.setObjectName(u"btn_back")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy1)
        self.btn_back.setMinimumSize(QSize(0, 0))
        self.btn_back.setMaximumSize(QSize(18, 21))
        font = QFont()
        font.setFamilies([u"Waseem"])
        font.setPointSize(25)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet(u"border: none;\n"
"")

        self.gridLayout_2.addWidget(self.btn_back, 1, 0, 1, 2)

        self.lbl_identity = QLabel(self.widget)
        self.lbl_identity.setObjectName(u"lbl_identity")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbl_identity.sizePolicy().hasHeightForWidth())
        self.lbl_identity.setSizePolicy(sizePolicy2)
        self.lbl_identity.setMaximumSize(QSize(364, 40))
        font1 = QFont()
        font1.setFamilies([u"Nexa-Trial"])
        font1.setPointSize(31)
        self.lbl_identity.setFont(font1)
        self.lbl_identity.setStyleSheet(u"color: rgba(255,255,255, 220);")
        self.lbl_identity.setTextFormat(Qt.RichText)

        self.gridLayout_2.addWidget(self.lbl_identity, 2, 0, 1, 2, Qt.AlignLeft)

        self.divider = QFrame(self.widget)
        self.divider.setObjectName(u"divider")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.divider.sizePolicy().hasHeightForWidth())
        self.divider.setSizePolicy(sizePolicy3)
        self.divider.setMaximumSize(QSize(16777215, 1))
        self.divider.setStyleSheet(u"background-color: rgba(255, 255, 255, 80);\n"
"border: none;")
        self.divider.setFrameShape(QFrame.HLine)
        self.divider.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.divider, 4, 0, 1, 2)

        self.text_fields_group = QFrame(self.widget)
        self.text_fields_group.setObjectName(u"text_fields_group")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.text_fields_group.sizePolicy().hasHeightForWidth())
        self.text_fields_group.setSizePolicy(sizePolicy4)
        self.text_fields_group.setMinimumSize(QSize(430, 351))
        self.text_fields_group.setMaximumSize(QSize(460, 700))
        self.text_fields_group.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.text_fields_group)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 6, -1, 6)
        self.lbl_notes = QLabel(self.text_fields_group)
        self.lbl_notes.setObjectName(u"lbl_notes")
        self.lbl_notes.setMinimumSize(QSize(0, 10))
        self.lbl_notes.setMaximumSize(QSize(16777215, 10))
        font2 = QFont()
        font2.setFamilies([u"Nexa-Trial"])
        self.lbl_notes.setFont(font2)
        self.lbl_notes.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout.addWidget(self.lbl_notes, 3, 0, 1, 1)

        self.btn_save = QToolButton(self.text_fields_group)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy5)
        self.btn_save.setMaximumSize(QSize(16777215, 75))
        font3 = QFont()
        font3.setFamilies([u"Nexa-Trial"])
        font3.setPointSize(16)
        self.btn_save.setFont(font3)
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-color:rgba(148, 105, 141, 220);")
        self.btn_save.setPopupMode(QToolButton.InstantPopup)
        self.btn_save.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.btn_save.setAutoRaise(False)
        self.btn_save.setArrowType(Qt.NoArrow)

        self.gridLayout.addWidget(self.btn_save, 5, 0, 1, 1)

        self.main_data_entry_group = QFrame(self.text_fields_group)
        self.main_data_entry_group.setObjectName(u"main_data_entry_group")
        sizePolicy4.setHeightForWidth(self.main_data_entry_group.sizePolicy().hasHeightForWidth())
        self.main_data_entry_group.setSizePolicy(sizePolicy4)
        self.main_data_entry_group.setMinimumSize(QSize(200, 200))
        self.main_data_entry_group.setStyleSheet(u"")
        self.main_data_entry_group.setFrameShape(QFrame.StyledPanel)
        self.main_data_entry_group.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.main_data_entry_group)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.le_surname = QLineEdit(self.main_data_entry_group)
        self.le_surname.setObjectName(u"le_surname")
        self.le_surname.setMinimumSize(QSize(0, 30))
        font4 = QFont()
        font4.setFamilies([u".AppleSystemUIFont"])
        self.le_surname.setFont(font4)
        self.le_surname.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_surname.setEchoMode(QLineEdit.Normal)

        self.gridLayout_3.addWidget(self.le_surname, 3, 1, 1, 1)

        self.lbl_license_num = QLabel(self.main_data_entry_group)
        self.lbl_license_num.setObjectName(u"lbl_license_num")
        self.lbl_license_num.setMinimumSize(QSize(0, 10))
        self.lbl_license_num.setMaximumSize(QSize(16777215, 10))
        self.lbl_license_num.setFont(font2)
        self.lbl_license_num.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_license_num, 13, 0, 1, 1)

        self.lbl_title = QLabel(self.main_data_entry_group)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setMinimumSize(QSize(0, 10))
        self.lbl_title.setMaximumSize(QSize(16777215, 10))
        self.lbl_title.setFont(font2)
        self.lbl_title.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_title, 0, 0, 1, 1)

        self.le_pass_num = QLineEdit(self.main_data_entry_group)
        self.le_pass_num.setObjectName(u"le_pass_num")
        self.le_pass_num.setMinimumSize(QSize(0, 30))
        self.le_pass_num.setFont(font4)
        self.le_pass_num.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_pass_num.setEchoMode(QLineEdit.Normal)

        self.gridLayout_3.addWidget(self.le_pass_num, 11, 0, 1, 2)

        self.le_nat_insur = QLineEdit(self.main_data_entry_group)
        self.le_nat_insur.setObjectName(u"le_nat_insur")
        self.le_nat_insur.setMinimumSize(QSize(0, 30))
        self.le_nat_insur.setFont(font4)
        self.le_nat_insur.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_nat_insur.setEchoMode(QLineEdit.Normal)

        self.gridLayout_3.addWidget(self.le_nat_insur, 9, 0, 1, 2)

        self.lbl_surname = QLabel(self.main_data_entry_group)
        self.lbl_surname.setObjectName(u"lbl_surname")
        self.lbl_surname.setMinimumSize(QSize(0, 10))
        self.lbl_surname.setMaximumSize(QSize(16777215, 10))
        self.lbl_surname.setFont(font2)
        self.lbl_surname.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_surname, 2, 1, 1, 1)

        self.lbl_first_name = QLabel(self.main_data_entry_group)
        self.lbl_first_name.setObjectName(u"lbl_first_name")
        self.lbl_first_name.setMinimumSize(QSize(0, 10))
        self.lbl_first_name.setMaximumSize(QSize(16777215, 10))
        self.lbl_first_name.setFont(font2)
        self.lbl_first_name.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_first_name, 2, 0, 1, 1)

        self.combo_title = QComboBox(self.main_data_entry_group)
        self.combo_title.setObjectName(u"combo_title")
        self.combo_title.setMinimumSize(QSize(0, 25))
        self.combo_title.setStyleSheet(u"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:6px;\n"
"color: rgba(255, 255, 255, 200);\n"
"background-color: rgba(43, 43, 43, 200);")

        self.gridLayout_3.addWidget(self.combo_title, 1, 0, 1, 2)

        self.le_email = QLineEdit(self.main_data_entry_group)
        self.le_email.setObjectName(u"le_email")
        self.le_email.setMinimumSize(QSize(0, 30))
        self.le_email.setFont(font4)
        self.le_email.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_email.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.gridLayout_3.addWidget(self.le_email, 5, 0, 1, 2)

        self.lbl_passport_num = QLabel(self.main_data_entry_group)
        self.lbl_passport_num.setObjectName(u"lbl_passport_num")
        self.lbl_passport_num.setMinimumSize(QSize(0, 13))
        self.lbl_passport_num.setMaximumSize(QSize(16777215, 13))
        self.lbl_passport_num.setFont(font2)
        self.lbl_passport_num.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_passport_num, 10, 0, 1, 1)

        self.lbl_nat_insurance = QLabel(self.main_data_entry_group)
        self.lbl_nat_insurance.setObjectName(u"lbl_nat_insurance")
        self.lbl_nat_insurance.setMinimumSize(QSize(0, 10))
        self.lbl_nat_insurance.setMaximumSize(QSize(16777215, 10))
        self.lbl_nat_insurance.setFont(font2)
        self.lbl_nat_insurance.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_nat_insurance, 8, 0, 1, 1)

        self.lbl_phone = QLabel(self.main_data_entry_group)
        self.lbl_phone.setObjectName(u"lbl_phone")
        self.lbl_phone.setMinimumSize(QSize(0, 13))
        self.lbl_phone.setMaximumSize(QSize(16777215, 13))
        self.lbl_phone.setFont(font2)
        self.lbl_phone.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_phone, 6, 0, 1, 1)

        self.le_phone = QLineEdit(self.main_data_entry_group)
        self.le_phone.setObjectName(u"le_phone")
        self.le_phone.setMinimumSize(QSize(0, 30))
        self.le_phone.setFont(font4)
        self.le_phone.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_phone.setEchoMode(QLineEdit.Normal)

        self.gridLayout_3.addWidget(self.le_phone, 7, 0, 1, 2)

        self.lbl_email = QLabel(self.main_data_entry_group)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setMinimumSize(QSize(0, 10))
        self.lbl_email.setMaximumSize(QSize(16777215, 12))
        self.lbl_email.setFont(font2)
        self.lbl_email.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_email, 4, 0, 1, 1)

        self.le_first_name = QLineEdit(self.main_data_entry_group)
        self.le_first_name.setObjectName(u"le_first_name")
        self.le_first_name.setMinimumSize(QSize(0, 30))
        self.le_first_name.setFont(font4)
        self.le_first_name.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_first_name.setEchoMode(QLineEdit.Normal)

        self.gridLayout_3.addWidget(self.le_first_name, 3, 0, 1, 1)

        self.le_license_num = QLineEdit(self.main_data_entry_group)
        self.le_license_num.setObjectName(u"le_license_num")
        self.le_license_num.setMinimumSize(QSize(0, 30))
        self.le_license_num.setFont(font4)
        self.le_license_num.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_license_num.setEchoMode(QLineEdit.Normal)

        self.gridLayout_3.addWidget(self.le_license_num, 14, 0, 1, 2)


        self.gridLayout.addWidget(self.main_data_entry_group, 2, 0, 1, 1)

        self.le_name = QLineEdit(self.text_fields_group)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setMinimumSize(QSize(0, 40))
        self.le_name.setFont(font4)
        self.le_name.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_name.setEchoMode(QLineEdit.Normal)

        self.gridLayout.addWidget(self.le_name, 1, 0, 1, 1)

        self.lbl_name = QLabel(self.text_fields_group)
        self.lbl_name.setObjectName(u"lbl_name")
        self.lbl_name.setMinimumSize(QSize(0, 10))
        self.lbl_name.setMaximumSize(QSize(16777215, 10))
        self.lbl_name.setFont(font2)
        self.lbl_name.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout.addWidget(self.lbl_name, 0, 0, 1, 1)

        self.te_notes = QTextEdit(self.text_fields_group)
        self.te_notes.setObjectName(u"te_notes")
        self.te_notes.setMaximumSize(QSize(16777215, 70))
        self.te_notes.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px;")

        self.gridLayout.addWidget(self.te_notes, 4, 0, 1, 1)


        self.gridLayout_2.addWidget(self.text_fields_group, 5, 0, 1, 2)


        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_back.setText(QCoreApplication.translate("Form", u"<", None))
        self.lbl_identity.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:700;\">New Identity</span></p></body></html>", None))
        self.lbl_notes.setText(QCoreApplication.translate("Form", u"notes", None))
        self.btn_save.setText(QCoreApplication.translate("Form", u"save", None))
        self.le_surname.setPlaceholderText("")
        self.lbl_license_num.setText(QCoreApplication.translate("Form", u"license number", None))
        self.lbl_title.setText(QCoreApplication.translate("Form", u"title", None))
        self.le_pass_num.setPlaceholderText("")
        self.le_nat_insur.setPlaceholderText("")
        self.lbl_surname.setText(QCoreApplication.translate("Form", u"surname", None))
        self.lbl_first_name.setText(QCoreApplication.translate("Form", u"first name", None))
        self.le_email.setPlaceholderText("")
        self.lbl_passport_num.setText(QCoreApplication.translate("Form", u"passport number", None))
        self.lbl_nat_insurance.setText(QCoreApplication.translate("Form", u"national insurance number", None))
        self.lbl_phone.setText(QCoreApplication.translate("Form", u"phone number", None))
        self.le_phone.setPlaceholderText("")
        self.lbl_email.setText(QCoreApplication.translate("Form", u"email", None))
        self.le_first_name.setPlaceholderText("")
        self.le_license_num.setPlaceholderText("")
        self.le_name.setPlaceholderText("")
        self.lbl_name.setText(QCoreApplication.translate("Form", u"name", None))
    # retranslateUi


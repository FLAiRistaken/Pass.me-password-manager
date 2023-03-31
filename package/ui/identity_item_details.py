# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'identity_item_details.ui'
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
    QLabel, QLayout, QLineEdit, QSizePolicy,
    QTextEdit, QToolButton, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(376, 506)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 375, 505))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(365, 505))
        self.widget.setStyleSheet(u"QToolButton{\n"
"	border-radius:6px;\n"
"	color: rgba(255, 255, 255, 220);\n"
"	padding: 5px;\n"
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
"QFrame#main_data_entry_group{\n"
"	background-color: rgba(70, 70, 70, 255);\n"
"	padding: 2px;\n"
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
        self.gridLayout_2.setContentsMargins(20, 20, 20, 8)
        self.btn_edit = QToolButton(self.widget)
        self.btn_edit.setObjectName(u"btn_edit")
        font = QFont()
        font.setFamilies([u"Nexa-Trial"])
        font.setPointSize(12)
        self.btn_edit.setFont(font)
        self.btn_edit.setStyleSheet(u"border-radius: 5px;")

        self.gridLayout_2.addWidget(self.btn_edit, 0, 3, 1, 1)

        self.lbl_item_name = QLabel(self.widget)
        self.lbl_item_name.setObjectName(u"lbl_item_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_item_name.sizePolicy().hasHeightForWidth())
        self.lbl_item_name.setSizePolicy(sizePolicy1)
        self.lbl_item_name.setMaximumSize(QSize(364, 40))
        font1 = QFont()
        font1.setFamilies([u"Nexa-Trial"])
        font1.setPointSize(31)
        font1.setBold(True)
        self.lbl_item_name.setFont(font1)
        self.lbl_item_name.setStyleSheet(u"color: rgba(255,255,255, 220);")
        self.lbl_item_name.setTextFormat(Qt.RichText)

        self.gridLayout_2.addWidget(self.lbl_item_name, 0, 0, 1, 3)

        self.text_fields_group = QFrame(self.widget)
        self.text_fields_group.setObjectName(u"text_fields_group")
        sizePolicy.setHeightForWidth(self.text_fields_group.sizePolicy().hasHeightForWidth())
        self.text_fields_group.setSizePolicy(sizePolicy)
        self.text_fields_group.setMaximumSize(QSize(460, 551))
        self.text_fields_group.setStyleSheet(u"")
        self.text_fields_group.setLineWidth(1)
        self.gridLayout = QGridLayout(self.text_fields_group)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 5, 3, 5)
        self.lbl_notes = QLabel(self.text_fields_group)
        self.lbl_notes.setObjectName(u"lbl_notes")
        self.lbl_notes.setMinimumSize(QSize(0, 10))
        self.lbl_notes.setMaximumSize(QSize(16777215, 10))
        font2 = QFont()
        font2.setFamilies([u"Nexa-Trial"])
        self.lbl_notes.setFont(font2)
        self.lbl_notes.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout.addWidget(self.lbl_notes, 1, 0, 1, 1)

        self.main_data_entry_group = QFrame(self.text_fields_group)
        self.main_data_entry_group.setObjectName(u"main_data_entry_group")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.main_data_entry_group.sizePolicy().hasHeightForWidth())
        self.main_data_entry_group.setSizePolicy(sizePolicy2)
        self.main_data_entry_group.setMinimumSize(QSize(200, 200))
        self.main_data_entry_group.setStyleSheet(u"")
        self.main_data_entry_group.setFrameShape(QFrame.StyledPanel)
        self.main_data_entry_group.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.main_data_entry_group)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(7)
        self.gridLayout_3.setContentsMargins(-1, 12, -1, 12)
        self.le_license_no = QLineEdit(self.main_data_entry_group)
        self.le_license_no.setObjectName(u"le_license_no")
        self.le_license_no.setMinimumSize(QSize(0, 25))
        self.le_license_no.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")

        self.gridLayout_3.addWidget(self.le_license_no, 19, 0, 1, 2)

        self.combo_title = QComboBox(self.main_data_entry_group)
        self.combo_title.addItem("")
        self.combo_title.addItem("")
        self.combo_title.addItem("")
        self.combo_title.addItem("")
        self.combo_title.addItem("")
        self.combo_title.addItem("")
        self.combo_title.addItem("")
        self.combo_title.setObjectName(u"combo_title")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.combo_title.sizePolicy().hasHeightForWidth())
        self.combo_title.setSizePolicy(sizePolicy3)
        self.combo_title.setMinimumSize(QSize(0, 25))
        self.combo_title.setMaximumSize(QSize(16777215, 25))
        self.combo_title.setFont(font2)
        self.combo_title.setStyleSheet(u"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:6px;\n"
"color: rgba(255, 255, 255, 200);\n"
"background-color: rgba(43, 43, 43, 200);")

        self.gridLayout_3.addWidget(self.combo_title, 1, 0, 1, 2)

        self.lbl_passport_num = QLabel(self.main_data_entry_group)
        self.lbl_passport_num.setObjectName(u"lbl_passport_num")
        self.lbl_passport_num.setMaximumSize(QSize(16777215, 10))
        self.lbl_passport_num.setFont(font2)
        self.lbl_passport_num.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_passport_num, 15, 0, 1, 1)

        self.le_email = QLineEdit(self.main_data_entry_group)
        self.le_email.setObjectName(u"le_email")
        self.le_email.setMinimumSize(QSize(0, 25))
        font3 = QFont()
        font3.setFamilies([u".AppleSystemUIFont"])
        self.le_email.setFont(font3)
        self.le_email.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_email.setEchoMode(QLineEdit.Normal)
        self.le_email.setReadOnly(True)

        self.gridLayout_3.addWidget(self.le_email, 6, 0, 1, 2)

        self.lbl_first_name = QLabel(self.main_data_entry_group)
        self.lbl_first_name.setObjectName(u"lbl_first_name")
        self.lbl_first_name.setMinimumSize(QSize(0, 10))
        self.lbl_first_name.setMaximumSize(QSize(16777215, 12))
        self.lbl_first_name.setFont(font2)
        self.lbl_first_name.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_first_name, 3, 0, 1, 1)

        self.lbl_phone_number = QLabel(self.main_data_entry_group)
        self.lbl_phone_number.setObjectName(u"lbl_phone_number")
        self.lbl_phone_number.setMaximumSize(QSize(16777215, 13))
        self.lbl_phone_number.setFont(font2)
        self.lbl_phone_number.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_phone_number, 7, 0, 1, 1)

        self.le_nat_insur_no = QLineEdit(self.main_data_entry_group)
        self.le_nat_insur_no.setObjectName(u"le_nat_insur_no")
        self.le_nat_insur_no.setMinimumSize(QSize(0, 25))
        self.le_nat_insur_no.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")

        self.gridLayout_3.addWidget(self.le_nat_insur_no, 14, 0, 1, 2)

        self.lbl_title = QLabel(self.main_data_entry_group)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setMinimumSize(QSize(0, 10))
        self.lbl_title.setMaximumSize(QSize(16777215, 10))
        self.lbl_title.setFont(font2)
        self.lbl_title.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_title, 0, 0, 1, 1)

        self.le_phone_no = QLineEdit(self.main_data_entry_group)
        self.le_phone_no.setObjectName(u"le_phone_no")
        self.le_phone_no.setMinimumSize(QSize(0, 25))
        self.le_phone_no.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")

        self.gridLayout_3.addWidget(self.le_phone_no, 8, 0, 1, 2)

        self.lbl_nat_insur_num = QLabel(self.main_data_entry_group)
        self.lbl_nat_insur_num.setObjectName(u"lbl_nat_insur_num")
        self.lbl_nat_insur_num.setMinimumSize(QSize(0, 10))
        self.lbl_nat_insur_num.setMaximumSize(QSize(16777215, 10))
        self.lbl_nat_insur_num.setFont(font2)
        self.lbl_nat_insur_num.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_nat_insur_num, 13, 0, 1, 1)

        self.lbl_email = QLabel(self.main_data_entry_group)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setMinimumSize(QSize(0, 10))
        self.lbl_email.setMaximumSize(QSize(16777215, 10))
        self.lbl_email.setFont(font2)
        self.lbl_email.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_email, 5, 0, 1, 1)

        self.lbl_license_num = QLabel(self.main_data_entry_group)
        self.lbl_license_num.setObjectName(u"lbl_license_num")
        self.lbl_license_num.setMaximumSize(QSize(16777215, 10))
        self.lbl_license_num.setFont(font2)
        self.lbl_license_num.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_license_num, 17, 0, 1, 1)

        self.lbl_surname = QLabel(self.main_data_entry_group)
        self.lbl_surname.setObjectName(u"lbl_surname")
        self.lbl_surname.setMaximumSize(QSize(16777215, 13))
        self.lbl_surname.setFont(font2)
        self.lbl_surname.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_surname, 3, 1, 1, 1)

        self.le_surname = QLineEdit(self.main_data_entry_group)
        self.le_surname.setObjectName(u"le_surname")
        self.le_surname.setMinimumSize(QSize(0, 25))
        self.le_surname.setFont(font3)
        self.le_surname.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_surname.setEchoMode(QLineEdit.Normal)
        self.le_surname.setReadOnly(True)

        self.gridLayout_3.addWidget(self.le_surname, 4, 1, 1, 1)

        self.le_first_name = QLineEdit(self.main_data_entry_group)
        self.le_first_name.setObjectName(u"le_first_name")
        self.le_first_name.setMinimumSize(QSize(0, 25))
        self.le_first_name.setFont(font3)
        self.le_first_name.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_first_name.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.le_first_name.setReadOnly(True)

        self.gridLayout_3.addWidget(self.le_first_name, 4, 0, 1, 1)

        self.le_pass_no = QLineEdit(self.main_data_entry_group)
        self.le_pass_no.setObjectName(u"le_pass_no")
        self.le_pass_no.setMinimumSize(QSize(0, 25))
        self.le_pass_no.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")

        self.gridLayout_3.addWidget(self.le_pass_no, 16, 0, 1, 2)


        self.gridLayout.addWidget(self.main_data_entry_group, 0, 0, 1, 1)

        self.te_notes = QTextEdit(self.text_fields_group)
        self.te_notes.setObjectName(u"te_notes")
        sizePolicy.setHeightForWidth(self.te_notes.sizePolicy().hasHeightForWidth())
        self.te_notes.setSizePolicy(sizePolicy)
        self.te_notes.setMaximumSize(QSize(16777215, 40))
        self.te_notes.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px;")
        self.te_notes.setReadOnly(True)

        self.gridLayout.addWidget(self.te_notes, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.text_fields_group, 1, 0, 3, 4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_edit.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.lbl_item_name.setText(QCoreApplication.translate("Form", u"ItemName", None))
        self.lbl_notes.setText(QCoreApplication.translate("Form", u"notes", None))
        self.combo_title.setItemText(0, QCoreApplication.translate("Form", u"- Select -", None))
        self.combo_title.setItemText(1, QCoreApplication.translate("Form", u"Mr", None))
        self.combo_title.setItemText(2, QCoreApplication.translate("Form", u"Mrs", None))
        self.combo_title.setItemText(3, QCoreApplication.translate("Form", u"Miss", None))
        self.combo_title.setItemText(4, QCoreApplication.translate("Form", u"Ms", None))
        self.combo_title.setItemText(5, QCoreApplication.translate("Form", u"Master", None))
        self.combo_title.setItemText(6, QCoreApplication.translate("Form", u"Dr", None))

        self.lbl_passport_num.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.le_email.setPlaceholderText("")
        self.lbl_first_name.setText(QCoreApplication.translate("Form", u"account number", None))
        self.lbl_phone_number.setText(QCoreApplication.translate("Form", u"expiration year", None))
        self.lbl_title.setText(QCoreApplication.translate("Form", u"title", None))
        self.lbl_nat_insur_num.setText(QCoreApplication.translate("Form", u"sort code", None))
        self.lbl_email.setText(QCoreApplication.translate("Form", u"brand", None))
        self.lbl_license_num.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_surname.setText(QCoreApplication.translate("Form", u"expiration month", None))
        self.le_surname.setPlaceholderText("")
        self.le_first_name.setPlaceholderText("")
    # retranslateUi


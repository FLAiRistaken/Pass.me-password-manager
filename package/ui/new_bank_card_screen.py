# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_bank_card_screen.ui'
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
        Form.resize(524, 777)
        self.gridLayout_4 = QGridLayout(Form)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(500, 700))
        self.widget.setMaximumSize(QSize(500, 750))
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
"")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout_2.setContentsMargins(20, 20, 20, 20)
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

        self.lbl_new_card = QLabel(self.widget)
        self.lbl_new_card.setObjectName(u"lbl_new_card")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbl_new_card.sizePolicy().hasHeightForWidth())
        self.lbl_new_card.setSizePolicy(sizePolicy2)
        self.lbl_new_card.setMaximumSize(QSize(364, 40))
        font1 = QFont()
        font1.setFamilies([u"Nexa-Trial"])
        font1.setPointSize(31)
        self.lbl_new_card.setFont(font1)
        self.lbl_new_card.setStyleSheet(u"color: rgba(255,255,255, 220);")
        self.lbl_new_card.setTextFormat(Qt.RichText)

        self.gridLayout_2.addWidget(self.lbl_new_card, 2, 0, 1, 2, Qt.AlignLeft)

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
        self.text_fields_group.setMinimumSize(QSize(430, 351))
        self.text_fields_group.setMaximumSize(QSize(460, 600))
        self.text_fields_group.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.text_fields_group)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 12, -1, 6)
        self.te_notes = QTextEdit(self.text_fields_group)
        self.te_notes.setObjectName(u"te_notes")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.te_notes.sizePolicy().hasHeightForWidth())
        self.te_notes.setSizePolicy(sizePolicy4)
        self.te_notes.setMaximumSize(QSize(16777215, 50))
        self.te_notes.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px;")

        self.gridLayout.addWidget(self.te_notes, 4, 0, 1, 1)

        self.btn_save = QToolButton(self.text_fields_group)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy5)
        self.btn_save.setMaximumSize(QSize(16777215, 75))
        font2 = QFont()
        font2.setFamilies([u"Nexa-Trial"])
        font2.setPointSize(16)
        self.btn_save.setFont(font2)
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-color:rgba(148, 105, 141, 220);")
        self.btn_save.setPopupMode(QToolButton.InstantPopup)
        self.btn_save.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.btn_save.setAutoRaise(False)
        self.btn_save.setArrowType(Qt.NoArrow)

        self.gridLayout.addWidget(self.btn_save, 6, 0, 1, 1)

        self.lbl_notes = QLabel(self.text_fields_group)
        self.lbl_notes.setObjectName(u"lbl_notes")
        self.lbl_notes.setMinimumSize(QSize(0, 10))
        self.lbl_notes.setMaximumSize(QSize(16777215, 10))
        font3 = QFont()
        font3.setFamilies([u"Nexa-Trial"])
        self.lbl_notes.setFont(font3)
        self.lbl_notes.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout.addWidget(self.lbl_notes, 3, 0, 1, 1)

        self.main_data_entry_group = QFrame(self.text_fields_group)
        self.main_data_entry_group.setObjectName(u"main_data_entry_group")
        sizePolicy.setHeightForWidth(self.main_data_entry_group.sizePolicy().hasHeightForWidth())
        self.main_data_entry_group.setSizePolicy(sizePolicy)
        self.main_data_entry_group.setMinimumSize(QSize(200, 200))
        self.main_data_entry_group.setStyleSheet(u"")
        self.main_data_entry_group.setFrameShape(QFrame.StyledPanel)
        self.main_data_entry_group.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.main_data_entry_group)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lbl_exp_month = QLabel(self.main_data_entry_group)
        self.lbl_exp_month.setObjectName(u"lbl_exp_month")
        self.lbl_exp_month.setFont(font3)
        self.lbl_exp_month.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_exp_month, 6, 0, 1, 1)

        self.le_name_on_card = QLineEdit(self.main_data_entry_group)
        self.le_name_on_card.setObjectName(u"le_name_on_card")
        self.le_name_on_card.setMinimumSize(QSize(0, 30))
        font4 = QFont()
        font4.setFamilies([u".AppleSystemUIFont"])
        self.le_name_on_card.setFont(font4)
        self.le_name_on_card.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_name_on_card.setEchoMode(QLineEdit.Normal)

        self.gridLayout_3.addWidget(self.le_name_on_card, 1, 0, 1, 2)

        self.le_card_number = QLineEdit(self.main_data_entry_group)
        self.le_card_number.setObjectName(u"le_card_number")
        self.le_card_number.setMinimumSize(QSize(0, 30))
        self.le_card_number.setFont(font4)
        self.le_card_number.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_card_number.setMaxLength(16)
        self.le_card_number.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.gridLayout_3.addWidget(self.le_card_number, 3, 0, 1, 2)

        self.combo_exp_year = QComboBox(self.main_data_entry_group)
        self.combo_exp_year.addItem("")
        self.combo_exp_year.addItem("")
        self.combo_exp_year.addItem("")
        self.combo_exp_year.addItem("")
        self.combo_exp_year.addItem("")
        self.combo_exp_year.addItem("")
        self.combo_exp_year.addItem("")
        self.combo_exp_year.addItem("")
        self.combo_exp_year.setObjectName(u"combo_exp_year")
        self.combo_exp_year.setMinimumSize(QSize(0, 25))
        self.combo_exp_year.setFont(font3)
        self.combo_exp_year.setStyleSheet(u"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:6px;\n"
"color: rgba(255, 255, 255, 200);\n"
"background-color: rgba(43, 43, 43, 200);")

        self.gridLayout_3.addWidget(self.combo_exp_year, 7, 1, 1, 1)

        self.lbl_exp_year = QLabel(self.main_data_entry_group)
        self.lbl_exp_year.setObjectName(u"lbl_exp_year")
        self.lbl_exp_year.setFont(font3)
        self.lbl_exp_year.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_exp_year, 6, 1, 1, 1)

        self.lbl_cvv = QLabel(self.main_data_entry_group)
        self.lbl_cvv.setObjectName(u"lbl_cvv")
        self.lbl_cvv.setFont(font3)
        self.lbl_cvv.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_cvv, 8, 0, 1, 1)

        self.lbl_name_on_card = QLabel(self.main_data_entry_group)
        self.lbl_name_on_card.setObjectName(u"lbl_name_on_card")
        self.lbl_name_on_card.setMinimumSize(QSize(0, 10))
        self.lbl_name_on_card.setMaximumSize(QSize(16777215, 10))
        self.lbl_name_on_card.setFont(font3)
        self.lbl_name_on_card.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_name_on_card, 0, 0, 1, 1)

        self.combo_brand = QComboBox(self.main_data_entry_group)
        self.combo_brand.addItem("")
        self.combo_brand.addItem("")
        self.combo_brand.addItem("")
        self.combo_brand.addItem("")
        self.combo_brand.addItem("")
        self.combo_brand.setObjectName(u"combo_brand")
        sizePolicy.setHeightForWidth(self.combo_brand.sizePolicy().hasHeightForWidth())
        self.combo_brand.setSizePolicy(sizePolicy)
        self.combo_brand.setMinimumSize(QSize(0, 25))
        self.combo_brand.setMaximumSize(QSize(16777215, 30))
        self.combo_brand.setFont(font3)
        self.combo_brand.setStyleSheet(u"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:6px;\n"
"color: rgba(255, 255, 255, 200);\n"
"background-color: rgba(43, 43, 43, 200);")

        self.gridLayout_3.addWidget(self.combo_brand, 5, 0, 1, 2)

        self.lbl_card_number = QLabel(self.main_data_entry_group)
        self.lbl_card_number.setObjectName(u"lbl_card_number")
        self.lbl_card_number.setMinimumSize(QSize(0, 10))
        self.lbl_card_number.setMaximumSize(QSize(16777215, 12))
        self.lbl_card_number.setFont(font3)
        self.lbl_card_number.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_card_number, 2, 0, 1, 1)

        self.combo_exp_month = QComboBox(self.main_data_entry_group)
        self.combo_exp_month.addItem("")
        self.combo_exp_month.addItem("")
        self.combo_exp_month.addItem("")
        self.combo_exp_month.addItem("")
        self.combo_exp_month.addItem("")
        self.combo_exp_month.addItem("")
        self.combo_exp_month.addItem("")
        self.combo_exp_month.addItem("")
        self.combo_exp_month.addItem("")
        self.combo_exp_month.addItem("")
        self.combo_exp_month.addItem("")
        self.combo_exp_month.addItem("")
        self.combo_exp_month.addItem("")
        self.combo_exp_month.setObjectName(u"combo_exp_month")
        self.combo_exp_month.setMinimumSize(QSize(0, 25))
        self.combo_exp_month.setFont(font3)
        self.combo_exp_month.setStyleSheet(u"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:6px;\n"
"color: rgba(255, 255, 255, 200);\n"
"background-color: rgba(43, 43, 43, 200);")

        self.gridLayout_3.addWidget(self.combo_exp_month, 7, 0, 1, 1)

        self.lbl_brand = QLabel(self.main_data_entry_group)
        self.lbl_brand.setObjectName(u"lbl_brand")
        self.lbl_brand.setMinimumSize(QSize(0, 10))
        self.lbl_brand.setMaximumSize(QSize(16777215, 10))
        self.lbl_brand.setFont(font3)
        self.lbl_brand.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_brand, 4, 0, 1, 1)

        self.le_cvv = QLineEdit(self.main_data_entry_group)
        self.le_cvv.setObjectName(u"le_cvv")
        self.le_cvv.setMinimumSize(QSize(0, 30))
        self.le_cvv.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_cvv.setMaxLength(3)
        self.le_cvv.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.gridLayout_3.addWidget(self.le_cvv, 9, 0, 1, 2)


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
        self.lbl_name.setFont(font3)
        self.lbl_name.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout.addWidget(self.lbl_name, 0, 0, 1, 1)

        self.combo_folders = QComboBox(self.text_fields_group)
        self.combo_folders.addItem("")
        self.combo_folders.addItem("")
        self.combo_folders.addItem("")
        self.combo_folders.addItem("")
        self.combo_folders.addItem("")
        self.combo_folders.addItem("")
        self.combo_folders.addItem("")
        self.combo_folders.addItem("")
        self.combo_folders.setObjectName(u"combo_folders")
        sizePolicy.setHeightForWidth(self.combo_folders.sizePolicy().hasHeightForWidth())
        self.combo_folders.setSizePolicy(sizePolicy)
        self.combo_folders.setMaximumSize(QSize(16777215, 30))
        self.combo_folders.setFont(font3)
        self.combo_folders.setStyleSheet(u"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:6px;\n"
"color: rgba(255, 255, 255, 200);")

        self.gridLayout.addWidget(self.combo_folders, 5, 0, 1, 1)


        self.gridLayout_2.addWidget(self.text_fields_group, 5, 0, 1, 2)


        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)

        QWidget.setTabOrder(self.le_name, self.le_name_on_card)
        QWidget.setTabOrder(self.le_name_on_card, self.le_card_number)
        QWidget.setTabOrder(self.le_card_number, self.combo_brand)
        QWidget.setTabOrder(self.combo_brand, self.combo_exp_month)
        QWidget.setTabOrder(self.combo_exp_month, self.combo_exp_year)
        QWidget.setTabOrder(self.combo_exp_year, self.le_cvv)
        QWidget.setTabOrder(self.le_cvv, self.te_notes)
        QWidget.setTabOrder(self.te_notes, self.combo_folders)
        QWidget.setTabOrder(self.combo_folders, self.btn_save)
        QWidget.setTabOrder(self.btn_save, self.btn_back)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_back.setText(QCoreApplication.translate("Form", u"<", None))
        self.lbl_new_card.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:700;\">New Bank Card</span></p></body></html>", None))
        self.btn_save.setText(QCoreApplication.translate("Form", u"save", None))
        self.lbl_notes.setText(QCoreApplication.translate("Form", u"notes", None))
        self.lbl_exp_month.setText(QCoreApplication.translate("Form", u"expiration month", None))
        self.le_name_on_card.setPlaceholderText("")
        self.le_card_number.setPlaceholderText("")
        self.combo_exp_year.setItemText(0, QCoreApplication.translate("Form", u"- Select - ", None))
        self.combo_exp_year.setItemText(1, QCoreApplication.translate("Form", u"2023", None))
        self.combo_exp_year.setItemText(2, QCoreApplication.translate("Form", u"2024", None))
        self.combo_exp_year.setItemText(3, QCoreApplication.translate("Form", u"2025", None))
        self.combo_exp_year.setItemText(4, QCoreApplication.translate("Form", u"2026", None))
        self.combo_exp_year.setItemText(5, QCoreApplication.translate("Form", u"2027", None))
        self.combo_exp_year.setItemText(6, QCoreApplication.translate("Form", u"2028", None))
        self.combo_exp_year.setItemText(7, QCoreApplication.translate("Form", u"2029", None))

        self.lbl_exp_year.setText(QCoreApplication.translate("Form", u"expiration year", None))
        self.lbl_cvv.setText(QCoreApplication.translate("Form", u"security code (CVV)", None))
        self.lbl_name_on_card.setText(QCoreApplication.translate("Form", u"name on card", None))
        self.combo_brand.setItemText(0, QCoreApplication.translate("Form", u"- Select -", None))
        self.combo_brand.setItemText(1, QCoreApplication.translate("Form", u"Visa", None))
        self.combo_brand.setItemText(2, QCoreApplication.translate("Form", u"Mastercard", None))
        self.combo_brand.setItemText(3, QCoreApplication.translate("Form", u"American Express", None))
        self.combo_brand.setItemText(4, QCoreApplication.translate("Form", u"Other", None))

        self.lbl_card_number.setText(QCoreApplication.translate("Form", u"card number", None))
        self.combo_exp_month.setItemText(0, QCoreApplication.translate("Form", u"- Select - ", None))
        self.combo_exp_month.setItemText(1, QCoreApplication.translate("Form", u"01 - January", None))
        self.combo_exp_month.setItemText(2, QCoreApplication.translate("Form", u"02 - February", None))
        self.combo_exp_month.setItemText(3, QCoreApplication.translate("Form", u"03 - March", None))
        self.combo_exp_month.setItemText(4, QCoreApplication.translate("Form", u"04 - April", None))
        self.combo_exp_month.setItemText(5, QCoreApplication.translate("Form", u"05 - May", None))
        self.combo_exp_month.setItemText(6, QCoreApplication.translate("Form", u"06 - June", None))
        self.combo_exp_month.setItemText(7, QCoreApplication.translate("Form", u"07 - July", None))
        self.combo_exp_month.setItemText(8, QCoreApplication.translate("Form", u"08 - August", None))
        self.combo_exp_month.setItemText(9, QCoreApplication.translate("Form", u"09 - September", None))
        self.combo_exp_month.setItemText(10, QCoreApplication.translate("Form", u"10 - October", None))
        self.combo_exp_month.setItemText(11, QCoreApplication.translate("Form", u"11 - November", None))
        self.combo_exp_month.setItemText(12, QCoreApplication.translate("Form", u"12 - December", None))

        self.lbl_brand.setText(QCoreApplication.translate("Form", u"brand", None))
        self.le_name.setPlaceholderText("")
        self.lbl_name.setText(QCoreApplication.translate("Form", u"name", None))
        self.combo_folders.setItemText(0, QCoreApplication.translate("Form", u"No folder", None))
        self.combo_folders.setItemText(1, QCoreApplication.translate("Form", u"Business", None))
        self.combo_folders.setItemText(2, QCoreApplication.translate("Form", u"Email", None))
        self.combo_folders.setItemText(3, QCoreApplication.translate("Form", u"Entertainment", None))
        self.combo_folders.setItemText(4, QCoreApplication.translate("Form", u"Education", None))
        self.combo_folders.setItemText(5, QCoreApplication.translate("Form", u"Finance", None))
        self.combo_folders.setItemText(6, QCoreApplication.translate("Form", u"Games", None))
        self.combo_folders.setItemText(7, QCoreApplication.translate("Form", u"Social", None))

    # retranslateUi


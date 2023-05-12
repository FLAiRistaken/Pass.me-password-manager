# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bank_card_item_details.ui'
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
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QSizePolicy, QTextEdit, QToolButton, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(365, 521)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 365, 521))
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
        self.gridLayout_2.setContentsMargins(7, 7, 7, 7)
        self.lbl_item_name = QLabel(self.widget)
        self.lbl_item_name.setObjectName(u"lbl_item_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_item_name.sizePolicy().hasHeightForWidth())
        self.lbl_item_name.setSizePolicy(sizePolicy1)
        self.lbl_item_name.setMaximumSize(QSize(364, 35))
        font = QFont()
        font.setFamilies([u"Nexa-Trial"])
        font.setPointSize(31)
        font.setBold(True)
        self.lbl_item_name.setFont(font)
        self.lbl_item_name.setStyleSheet(u"color: rgba(255,255,255, 220);")
        self.lbl_item_name.setTextFormat(Qt.RichText)

        self.gridLayout_2.addWidget(self.lbl_item_name, 0, 0, 1, 1)

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
        font1 = QFont()
        font1.setFamilies([u"Nexa-Trial"])
        self.lbl_notes.setFont(font1)
        self.lbl_notes.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout.addWidget(self.lbl_notes, 1, 0, 1, 1)

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

        self.combo_folders = QComboBox(self.text_fields_group)
        self.combo_folders.addItem("")
        self.combo_folders.addItem("")
        self.combo_folders.addItem("")
        self.combo_folders.addItem("")
        self.combo_folders.addItem("")
        self.combo_folders.addItem("")
        self.combo_folders.addItem("")
        self.combo_folders.addItem("")
        self.combo_folders.addItem("")
        self.combo_folders.addItem("")
        self.combo_folders.setObjectName(u"combo_folders")
        self.combo_folders.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.combo_folders.sizePolicy().hasHeightForWidth())
        self.combo_folders.setSizePolicy(sizePolicy2)
        self.combo_folders.setMaximumSize(QSize(16777215, 30))
        self.combo_folders.setFont(font1)
        self.combo_folders.setStyleSheet(u"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:6px;\n"
"color: rgba(255, 255, 255, 200);")
        self.combo_folders.setEditable(False)

        self.gridLayout.addWidget(self.combo_folders, 3, 0, 1, 1)

        self.main_data_entry_group = QFrame(self.text_fields_group)
        self.main_data_entry_group.setObjectName(u"main_data_entry_group")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.main_data_entry_group.sizePolicy().hasHeightForWidth())
        self.main_data_entry_group.setSizePolicy(sizePolicy3)
        self.main_data_entry_group.setMinimumSize(QSize(200, 200))
        self.main_data_entry_group.setStyleSheet(u"")
        self.main_data_entry_group.setFrameShape(QFrame.StyledPanel)
        self.main_data_entry_group.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.main_data_entry_group)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 12, -1, 12)
        self.lbl_name_on_card = QLabel(self.main_data_entry_group)
        self.lbl_name_on_card.setObjectName(u"lbl_name_on_card")
        self.lbl_name_on_card.setMinimumSize(QSize(0, 10))
        self.lbl_name_on_card.setMaximumSize(QSize(16777215, 10))
        self.lbl_name_on_card.setFont(font1)
        self.lbl_name_on_card.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_name_on_card, 0, 0, 1, 1)

        self.lbl_exp_month = QLabel(self.main_data_entry_group)
        self.lbl_exp_month.setObjectName(u"lbl_exp_month")
        self.lbl_exp_month.setFont(font1)
        self.lbl_exp_month.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_exp_month, 6, 0, 1, 1)

        self.lbl_cvv = QLabel(self.main_data_entry_group)
        self.lbl_cvv.setObjectName(u"lbl_cvv")
        self.lbl_cvv.setMinimumSize(QSize(0, 10))
        self.lbl_cvv.setMaximumSize(QSize(16777215, 10))
        self.lbl_cvv.setFont(font1)
        self.lbl_cvv.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_cvv, 10, 0, 1, 1)

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
        self.combo_exp_month.setEnabled(False)
        self.combo_exp_month.setMinimumSize(QSize(0, 25))
        self.combo_exp_month.setFont(font1)
        self.combo_exp_month.setStyleSheet(u"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:6px;\n"
"color: rgba(255, 255, 255, 200);\n"
"background-color: rgba(43, 43, 43, 200);")

        self.gridLayout_3.addWidget(self.combo_exp_month, 8, 0, 1, 1)

        self.lbl_card_number = QLabel(self.main_data_entry_group)
        self.lbl_card_number.setObjectName(u"lbl_card_number")
        self.lbl_card_number.setMinimumSize(QSize(0, 10))
        self.lbl_card_number.setMaximumSize(QSize(16777215, 12))
        self.lbl_card_number.setFont(font1)
        self.lbl_card_number.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_card_number, 2, 0, 1, 1)

        self.lbl_brand = QLabel(self.main_data_entry_group)
        self.lbl_brand.setObjectName(u"lbl_brand")
        self.lbl_brand.setMinimumSize(QSize(0, 10))
        self.lbl_brand.setMaximumSize(QSize(16777215, 10))
        self.lbl_brand.setFont(font1)
        self.lbl_brand.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_brand, 4, 0, 1, 1)

        self.lbl_exp_year = QLabel(self.main_data_entry_group)
        self.lbl_exp_year.setObjectName(u"lbl_exp_year")
        self.lbl_exp_year.setFont(font1)
        self.lbl_exp_year.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_exp_year, 6, 1, 1, 1)

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
        self.combo_exp_year.setEnabled(False)
        self.combo_exp_year.setMinimumSize(QSize(0, 25))
        self.combo_exp_year.setFont(font1)
        self.combo_exp_year.setStyleSheet(u"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:6px;\n"
"color: rgba(255, 255, 255, 200);\n"
"background-color: rgba(43, 43, 43, 200);")

        self.gridLayout_3.addWidget(self.combo_exp_year, 8, 1, 1, 1)

        self.combo_brand = QComboBox(self.main_data_entry_group)
        self.combo_brand.addItem("")
        self.combo_brand.addItem("")
        self.combo_brand.addItem("")
        self.combo_brand.addItem("")
        self.combo_brand.addItem("")
        self.combo_brand.setObjectName(u"combo_brand")
        self.combo_brand.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.combo_brand.sizePolicy().hasHeightForWidth())
        self.combo_brand.setSizePolicy(sizePolicy2)
        self.combo_brand.setMinimumSize(QSize(0, 25))
        self.combo_brand.setMaximumSize(QSize(16777215, 30))
        self.combo_brand.setFont(font1)
        self.combo_brand.setStyleSheet(u"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:6px;\n"
"color: rgba(255, 255, 255, 200);\n"
"background-color: rgba(43, 43, 43, 200);")

        self.gridLayout_3.addWidget(self.combo_brand, 5, 0, 1, 2)

        self.le_card_number = QLineEdit(self.main_data_entry_group)
        self.le_card_number.setObjectName(u"le_card_number")
        self.le_card_number.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setFamilies([u".AppleSystemUIFont"])
        self.le_card_number.setFont(font2)
        self.le_card_number.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_card_number.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.le_card_number.setReadOnly(True)

        self.gridLayout_3.addWidget(self.le_card_number, 3, 0, 1, 2)

        self.le_name_on_card = QLineEdit(self.main_data_entry_group)
        self.le_name_on_card.setObjectName(u"le_name_on_card")
        self.le_name_on_card.setMinimumSize(QSize(0, 30))
        self.le_name_on_card.setFont(font2)
        self.le_name_on_card.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_name_on_card.setEchoMode(QLineEdit.Normal)
        self.le_name_on_card.setReadOnly(True)

        self.gridLayout_3.addWidget(self.le_name_on_card, 1, 0, 1, 2)

        self.le_cvv = QLineEdit(self.main_data_entry_group)
        self.le_cvv.setObjectName(u"le_cvv")
        self.le_cvv.setMinimumSize(QSize(0, 30))
        self.le_cvv.setFont(font2)
        self.le_cvv.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_cvv.setEchoMode(QLineEdit.Normal)
        self.le_cvv.setReadOnly(True)

        self.gridLayout_3.addWidget(self.le_cvv, 11, 0, 1, 2)


        self.gridLayout.addWidget(self.main_data_entry_group, 0, 0, 1, 1)

        self.dates_grid = QGridLayout()
        self.dates_grid.setObjectName(u"dates_grid")
        self.mod_date_layout = QHBoxLayout()
        self.mod_date_layout.setObjectName(u"mod_date_layout")
        self.lbl_date_modified = QLabel(self.text_fields_group)
        self.lbl_date_modified.setObjectName(u"lbl_date_modified")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(9)
        self.lbl_date_modified.setFont(font3)
        self.lbl_date_modified.setStyleSheet(u"color: rgba(255, 255, 255, 100);")

        self.mod_date_layout.addWidget(self.lbl_date_modified, 0, Qt.AlignRight)

        self.lbl_modified_value = QLabel(self.text_fields_group)
        self.lbl_modified_value.setObjectName(u"lbl_modified_value")
        self.lbl_modified_value.setFont(font3)
        self.lbl_modified_value.setStyleSheet(u"color: rgba(255, 255, 255, 100);")

        self.mod_date_layout.addWidget(self.lbl_modified_value)


        self.dates_grid.addLayout(self.mod_date_layout, 2, 0, 1, 1)

        self.create_date_layout = QHBoxLayout()
        self.create_date_layout.setObjectName(u"create_date_layout")
        self.lbl_date_created = QLabel(self.text_fields_group)
        self.lbl_date_created.setObjectName(u"lbl_date_created")
        self.lbl_date_created.setFont(font3)
        self.lbl_date_created.setStyleSheet(u"color: rgba(255, 255, 255, 100);")

        self.create_date_layout.addWidget(self.lbl_date_created, 0, Qt.AlignRight)

        self.lbl_create_value = QLabel(self.text_fields_group)
        self.lbl_create_value.setObjectName(u"lbl_create_value")
        self.lbl_create_value.setFont(font3)
        self.lbl_create_value.setStyleSheet(u"color: rgba(255, 255, 255, 100);")

        self.create_date_layout.addWidget(self.lbl_create_value)


        self.dates_grid.addLayout(self.create_date_layout, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.dates_grid, 4, 0, 1, 1)


        self.gridLayout_2.addWidget(self.text_fields_group, 1, 0, 3, 5)

        self.btn_edit = QToolButton(self.widget)
        self.btn_edit.setObjectName(u"btn_edit")
        font4 = QFont()
        font4.setFamilies([u"Nexa-Trial"])
        font4.setPointSize(12)
        self.btn_edit.setFont(font4)
        self.btn_edit.setStyleSheet(u"border-radius: 5px;")

        self.gridLayout_2.addWidget(self.btn_edit, 0, 4, 1, 1)

        self.btn_fav = QToolButton(self.widget)
        self.btn_fav.setObjectName(u"btn_fav")
        font5 = QFont()
        font5.setFamilies([u"Nexa-Trial"])
        font5.setPointSize(18)
        self.btn_fav.setFont(font5)
        self.btn_fav.setStyleSheet(u"border-radius: 5px;")

        self.gridLayout_2.addWidget(self.btn_fav, 0, 3, 1, 1)

        QWidget.setTabOrder(self.le_name_on_card, self.le_card_number)
        QWidget.setTabOrder(self.le_card_number, self.combo_brand)
        QWidget.setTabOrder(self.combo_brand, self.combo_exp_month)
        QWidget.setTabOrder(self.combo_exp_month, self.combo_exp_year)
        QWidget.setTabOrder(self.combo_exp_year, self.le_cvv)
        QWidget.setTabOrder(self.le_cvv, self.te_notes)
        QWidget.setTabOrder(self.te_notes, self.combo_folders)
        QWidget.setTabOrder(self.combo_folders, self.btn_fav)
        QWidget.setTabOrder(self.btn_fav, self.btn_edit)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_item_name.setText(QCoreApplication.translate("Form", u"ItemName", None))
        self.lbl_notes.setText(QCoreApplication.translate("Form", u"notes", None))
        self.combo_folders.setItemText(0, QCoreApplication.translate("Form", u"No folder", None))
        self.combo_folders.setItemText(1, QCoreApplication.translate("Form", u"Business", None))
        self.combo_folders.setItemText(2, QCoreApplication.translate("Form", u"Email", None))
        self.combo_folders.setItemText(3, QCoreApplication.translate("Form", u"Entertainment", None))
        self.combo_folders.setItemText(4, QCoreApplication.translate("Form", u"Education", None))
        self.combo_folders.setItemText(5, QCoreApplication.translate("Form", u"Encrypted notes", None))
        self.combo_folders.setItemText(6, QCoreApplication.translate("Form", u"Finance", None))
        self.combo_folders.setItemText(7, QCoreApplication.translate("Form", u"Games", None))
        self.combo_folders.setItemText(8, QCoreApplication.translate("Form", u"Shopping", None))
        self.combo_folders.setItemText(9, QCoreApplication.translate("Form", u"Social", None))

        self.lbl_name_on_card.setText(QCoreApplication.translate("Form", u"name on account", None))
        self.lbl_exp_month.setText(QCoreApplication.translate("Form", u"expiration month", None))
        self.lbl_cvv.setText(QCoreApplication.translate("Form", u"sort code", None))
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

        self.lbl_card_number.setText(QCoreApplication.translate("Form", u"account number", None))
        self.lbl_brand.setText(QCoreApplication.translate("Form", u"brand", None))
        self.lbl_exp_year.setText(QCoreApplication.translate("Form", u"expiration year", None))
        self.combo_exp_year.setItemText(0, QCoreApplication.translate("Form", u"- Select - ", None))
        self.combo_exp_year.setItemText(1, QCoreApplication.translate("Form", u"2023", None))
        self.combo_exp_year.setItemText(2, QCoreApplication.translate("Form", u"2024", None))
        self.combo_exp_year.setItemText(3, QCoreApplication.translate("Form", u"2025", None))
        self.combo_exp_year.setItemText(4, QCoreApplication.translate("Form", u"2026", None))
        self.combo_exp_year.setItemText(5, QCoreApplication.translate("Form", u"2027", None))
        self.combo_exp_year.setItemText(6, QCoreApplication.translate("Form", u"2028", None))
        self.combo_exp_year.setItemText(7, QCoreApplication.translate("Form", u"2029", None))

        self.combo_brand.setItemText(0, QCoreApplication.translate("Form", u"- Select -", None))
        self.combo_brand.setItemText(1, QCoreApplication.translate("Form", u"Visa", None))
        self.combo_brand.setItemText(2, QCoreApplication.translate("Form", u"Mastercard", None))
        self.combo_brand.setItemText(3, QCoreApplication.translate("Form", u"American Express", None))
        self.combo_brand.setItemText(4, QCoreApplication.translate("Form", u"Other", None))

        self.le_card_number.setPlaceholderText("")
        self.le_name_on_card.setPlaceholderText("")
        self.le_cvv.setPlaceholderText("")
        self.lbl_date_modified.setText(QCoreApplication.translate("Form", u"Date modified:", None))
        self.lbl_modified_value.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_date_created.setText(QCoreApplication.translate("Form", u"Date created:", None))
        self.lbl_create_value.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.btn_edit.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.btn_fav.setText(QCoreApplication.translate("Form", u"\u2606", None))
    # retranslateUi


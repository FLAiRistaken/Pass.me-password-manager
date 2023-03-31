# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_item_details_main.ui'
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
        Form.resize(368, 508)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 367, 507))
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
        self.gridLayout_2.setContentsMargins(20, 20, 20, 20)
        self.lbl_date_modified = QLabel(self.widget)
        self.lbl_date_modified.setObjectName(u"lbl_date_modified")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(9)
        self.lbl_date_modified.setFont(font)
        self.lbl_date_modified.setStyleSheet(u"color: rgba(255, 255, 255, 100);")

        self.gridLayout_2.addWidget(self.lbl_date_modified, 6, 0, 1, 1, Qt.AlignRight)

        self.lbl_modified_value = QLabel(self.widget)
        self.lbl_modified_value.setObjectName(u"lbl_modified_value")
        self.lbl_modified_value.setFont(font)
        self.lbl_modified_value.setStyleSheet(u"color: rgba(255, 255, 255, 100);")

        self.gridLayout_2.addWidget(self.lbl_modified_value, 6, 1, 1, 1, Qt.AlignLeft)

        self.lbl_item_name = QLabel(self.widget)
        self.lbl_item_name.setObjectName(u"lbl_item_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_item_name.sizePolicy().hasHeightForWidth())
        self.lbl_item_name.setSizePolicy(sizePolicy1)
        self.lbl_item_name.setMaximumSize(QSize(364, 112))
        font1 = QFont()
        font1.setFamilies([u"Nexa-Trial"])
        font1.setPointSize(31)
        font1.setBold(True)
        self.lbl_item_name.setFont(font1)
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
        self.le_password = QLineEdit(self.main_data_entry_group)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setFamilies([u".AppleSystemUIFont"])
        self.le_password.setFont(font2)
        self.le_password.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_password.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.le_password.setReadOnly(True)

        self.gridLayout_3.addWidget(self.le_password, 3, 0, 1, 1)

        self.lbl_password = QLabel(self.main_data_entry_group)
        self.lbl_password.setObjectName(u"lbl_password")
        self.lbl_password.setMinimumSize(QSize(0, 10))
        self.lbl_password.setMaximumSize(QSize(16777215, 12))
        font3 = QFont()
        font3.setFamilies([u"Nexa-Trial"])
        self.lbl_password.setFont(font3)
        self.lbl_password.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_password, 2, 0, 1, 1)

        self.le_website = QLineEdit(self.main_data_entry_group)
        self.le_website.setObjectName(u"le_website")
        self.le_website.setMinimumSize(QSize(0, 30))
        self.le_website.setFont(font2)
        self.le_website.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_website.setEchoMode(QLineEdit.Normal)
        self.le_website.setReadOnly(True)

        self.gridLayout_3.addWidget(self.le_website, 5, 0, 1, 1)

        self.le_email = QLineEdit(self.main_data_entry_group)
        self.le_email.setObjectName(u"le_email")
        self.le_email.setMinimumSize(QSize(0, 30))
        self.le_email.setFont(font2)
        self.le_email.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_email.setEchoMode(QLineEdit.Normal)
        self.le_email.setReadOnly(True)

        self.gridLayout_3.addWidget(self.le_email, 1, 0, 1, 1)

        self.lbl_email = QLabel(self.main_data_entry_group)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setMinimumSize(QSize(0, 10))
        self.lbl_email.setMaximumSize(QSize(16777215, 10))
        self.lbl_email.setFont(font3)
        self.lbl_email.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_email, 0, 0, 1, 1)

        self.lbl_website = QLabel(self.main_data_entry_group)
        self.lbl_website.setObjectName(u"lbl_website")
        self.lbl_website.setMinimumSize(QSize(0, 10))
        self.lbl_website.setMaximumSize(QSize(16777215, 10))
        self.lbl_website.setFont(font3)
        self.lbl_website.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_website, 4, 0, 1, 1)


        self.gridLayout.addWidget(self.main_data_entry_group, 0, 0, 1, 1)

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
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.combo_folders.sizePolicy().hasHeightForWidth())
        self.combo_folders.setSizePolicy(sizePolicy3)
        self.combo_folders.setMaximumSize(QSize(16777215, 30))
        self.combo_folders.setFont(font3)
        self.combo_folders.setStyleSheet(u"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:6px;\n"
"color: rgba(255, 255, 255, 200);")
        self.combo_folders.setEditable(False)

        self.gridLayout.addWidget(self.combo_folders, 3, 0, 1, 1)

        self.te_notes = QTextEdit(self.text_fields_group)
        self.te_notes.setObjectName(u"te_notes")
        sizePolicy.setHeightForWidth(self.te_notes.sizePolicy().hasHeightForWidth())
        self.te_notes.setSizePolicy(sizePolicy)
        self.te_notes.setMaximumSize(QSize(16777215, 110))
        self.te_notes.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px;")
        self.te_notes.setReadOnly(True)

        self.gridLayout.addWidget(self.te_notes, 2, 0, 1, 1)

        self.lbl_notes = QLabel(self.text_fields_group)
        self.lbl_notes.setObjectName(u"lbl_notes")
        self.lbl_notes.setMinimumSize(QSize(0, 10))
        self.lbl_notes.setMaximumSize(QSize(16777215, 10))
        self.lbl_notes.setFont(font3)
        self.lbl_notes.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout.addWidget(self.lbl_notes, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.text_fields_group, 2, 0, 2, 4)

        self.btn_edit = QToolButton(self.widget)
        self.btn_edit.setObjectName(u"btn_edit")
        font4 = QFont()
        font4.setFamilies([u"Nexa-Trial"])
        font4.setPointSize(12)
        self.btn_edit.setFont(font4)
        self.btn_edit.setStyleSheet(u"border-radius: 5px;")

        self.gridLayout_2.addWidget(self.btn_edit, 0, 3, 1, 1)

        self.lbl_date_created = QLabel(self.widget)
        self.lbl_date_created.setObjectName(u"lbl_date_created")
        self.lbl_date_created.setFont(font)
        self.lbl_date_created.setStyleSheet(u"color: rgba(255, 255, 255, 100);")

        self.gridLayout_2.addWidget(self.lbl_date_created, 4, 0, 1, 1, Qt.AlignRight)

        self.lbl_create_value = QLabel(self.widget)
        self.lbl_create_value.setObjectName(u"lbl_create_value")
        self.lbl_create_value.setFont(font)
        self.lbl_create_value.setStyleSheet(u"color: rgba(255, 255, 255, 100);")

        self.gridLayout_2.addWidget(self.lbl_create_value, 4, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_date_modified.setText(QCoreApplication.translate("Form", u"Date modified:", None))
        self.lbl_modified_value.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_item_name.setText(QCoreApplication.translate("Form", u"ItemName", None))
        self.le_password.setPlaceholderText("")
        self.lbl_password.setText(QCoreApplication.translate("Form", u"password", None))
        self.le_website.setPlaceholderText("")
        self.le_email.setPlaceholderText("")
        self.lbl_email.setText(QCoreApplication.translate("Form", u"email / username", None))
        self.lbl_website.setText(QCoreApplication.translate("Form", u"website", None))
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

        self.lbl_notes.setText(QCoreApplication.translate("Form", u"notes", None))
        self.btn_edit.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.lbl_date_created.setText(QCoreApplication.translate("Form", u"Date created:", None))
        self.lbl_create_value.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi


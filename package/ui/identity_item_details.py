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
        self.lbl_item_name.setMaximumSize(QSize(364, 40))
        font = QFont()
        font.setFamilies([u"Nexa-Trial"])
        font.setPointSize(31)
        font.setBold(True)
        self.lbl_item_name.setFont(font)
        self.lbl_item_name.setStyleSheet(u"color: rgba(255,255,255, 220);")
        self.lbl_item_name.setTextFormat(Qt.RichText)

        self.gridLayout_2.addWidget(self.lbl_item_name, 0, 0, 1, 3)

        self.btn_edit = QToolButton(self.widget)
        self.btn_edit.setObjectName(u"btn_edit")
        font1 = QFont()
        font1.setFamilies([u"Nexa-Trial"])
        font1.setPointSize(12)
        self.btn_edit.setFont(font1)
        self.btn_edit.setStyleSheet(u"border-radius: 5px;")

        self.gridLayout_2.addWidget(self.btn_edit, 0, 4, 1, 1)

        self.text_fields_group = QFrame(self.widget)
        self.text_fields_group.setObjectName(u"text_fields_group")
        sizePolicy.setHeightForWidth(self.text_fields_group.sizePolicy().hasHeightForWidth())
        self.text_fields_group.setSizePolicy(sizePolicy)
        self.text_fields_group.setMaximumSize(QSize(460, 560))
        self.text_fields_group.setStyleSheet(u"")
        self.text_fields_group.setLineWidth(1)
        self.gridLayout = QGridLayout(self.text_fields_group)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 0, 3, 4)
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
        self.gridLayout_3.setVerticalSpacing(6)
        self.gridLayout_3.setContentsMargins(-1, 8, -1, 12)
        self.le_license_no = QLineEdit(self.main_data_entry_group)
        self.le_license_no.setObjectName(u"le_license_no")
        self.le_license_no.setMinimumSize(QSize(0, 25))
        self.le_license_no.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_license_no.setReadOnly(True)

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
        self.combo_title.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.combo_title.sizePolicy().hasHeightForWidth())
        self.combo_title.setSizePolicy(sizePolicy3)
        self.combo_title.setMinimumSize(QSize(0, 25))
        self.combo_title.setMaximumSize(QSize(16777215, 25))
        font2 = QFont()
        font2.setFamilies([u"Nexa-Trial"])
        self.combo_title.setFont(font2)
        self.combo_title.setStyleSheet(u"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:6px;\n"
"color: rgba(255, 255, 255, 200);\n"
"background-color: rgba(43, 43, 43, 200);")
        self.combo_title.setEditable(False)

        self.gridLayout_3.addWidget(self.combo_title, 1, 0, 1, 2)

        self.lbl_passport_num = QLabel(self.main_data_entry_group)
        self.lbl_passport_num.setObjectName(u"lbl_passport_num")
        self.lbl_passport_num.setMaximumSize(QSize(16777215, 10))
        self.lbl_passport_num.setFont(font1)
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
        self.lbl_first_name.setFont(font1)
        self.lbl_first_name.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_first_name, 3, 0, 1, 1)

        self.lbl_phone_number = QLabel(self.main_data_entry_group)
        self.lbl_phone_number.setObjectName(u"lbl_phone_number")
        self.lbl_phone_number.setMaximumSize(QSize(16777215, 13))
        self.lbl_phone_number.setFont(font1)
        self.lbl_phone_number.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_phone_number, 7, 0, 1, 1)

        self.le_nat_insur_no = QLineEdit(self.main_data_entry_group)
        self.le_nat_insur_no.setObjectName(u"le_nat_insur_no")
        self.le_nat_insur_no.setMinimumSize(QSize(0, 25))
        self.le_nat_insur_no.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_nat_insur_no.setReadOnly(True)

        self.gridLayout_3.addWidget(self.le_nat_insur_no, 14, 0, 1, 2)

        self.lbl_title = QLabel(self.main_data_entry_group)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setMinimumSize(QSize(0, 10))
        self.lbl_title.setMaximumSize(QSize(16777215, 10))
        self.lbl_title.setFont(font1)
        self.lbl_title.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_title, 0, 0, 1, 1)

        self.le_phone_no = QLineEdit(self.main_data_entry_group)
        self.le_phone_no.setObjectName(u"le_phone_no")
        self.le_phone_no.setMinimumSize(QSize(0, 25))
        self.le_phone_no.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_phone_no.setReadOnly(True)

        self.gridLayout_3.addWidget(self.le_phone_no, 8, 0, 1, 2)

        self.lbl_license_num = QLabel(self.main_data_entry_group)
        self.lbl_license_num.setObjectName(u"lbl_license_num")
        self.lbl_license_num.setMaximumSize(QSize(16777215, 10))
        self.lbl_license_num.setFont(font1)
        self.lbl_license_num.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_license_num, 17, 0, 1, 1)

        self.lbl_surname = QLabel(self.main_data_entry_group)
        self.lbl_surname.setObjectName(u"lbl_surname")
        self.lbl_surname.setMaximumSize(QSize(16777215, 13))
        self.lbl_surname.setFont(font1)
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
        self.le_first_name.setEchoMode(QLineEdit.Normal)
        self.le_first_name.setReadOnly(True)

        self.gridLayout_3.addWidget(self.le_first_name, 4, 0, 1, 1)

        self.le_pass_no = QLineEdit(self.main_data_entry_group)
        self.le_pass_no.setObjectName(u"le_pass_no")
        self.le_pass_no.setMinimumSize(QSize(0, 25))
        self.le_pass_no.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_pass_no.setReadOnly(True)

        self.gridLayout_3.addWidget(self.le_pass_no, 16, 0, 1, 2)

        self.lbl_email = QLabel(self.main_data_entry_group)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setMinimumSize(QSize(0, 10))
        self.lbl_email.setMaximumSize(QSize(16777215, 10))
        self.lbl_email.setFont(font1)
        self.lbl_email.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_email, 5, 0, 1, 2)

        self.lbl_nat_insur_num = QLabel(self.main_data_entry_group)
        self.lbl_nat_insur_num.setObjectName(u"lbl_nat_insur_num")
        self.lbl_nat_insur_num.setMinimumSize(QSize(0, 10))
        self.lbl_nat_insur_num.setMaximumSize(QSize(16777215, 10))
        self.lbl_nat_insur_num.setFont(font1)
        self.lbl_nat_insur_num.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_3.addWidget(self.lbl_nat_insur_num, 13, 0, 1, 2)


        self.gridLayout.addWidget(self.main_data_entry_group, 0, 0, 1, 1)

        self.te_notes = QTextEdit(self.text_fields_group)
        self.te_notes.setObjectName(u"te_notes")
        sizePolicy.setHeightForWidth(self.te_notes.sizePolicy().hasHeightForWidth())
        self.te_notes.setSizePolicy(sizePolicy)
        self.te_notes.setMaximumSize(QSize(16777215, 35))
        font4 = QFont()
        font4.setPointSize(12)
        self.te_notes.setFont(font4)
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
        self.lbl_notes.setFont(font2)
        self.lbl_notes.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout.addWidget(self.lbl_notes, 1, 0, 1, 1)

        self.dates_grid_2 = QGridLayout()
        self.dates_grid_2.setObjectName(u"dates_grid_2")
        self.mod_date_layout_2 = QHBoxLayout()
        self.mod_date_layout_2.setObjectName(u"mod_date_layout_2")
        self.lbl_date_modified_2 = QLabel(self.text_fields_group)
        self.lbl_date_modified_2.setObjectName(u"lbl_date_modified_2")
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(9)
        self.lbl_date_modified_2.setFont(font5)
        self.lbl_date_modified_2.setStyleSheet(u"color: rgba(255, 255, 255, 100);")

        self.mod_date_layout_2.addWidget(self.lbl_date_modified_2, 0, Qt.AlignRight)

        self.lbl_modified_value_2 = QLabel(self.text_fields_group)
        self.lbl_modified_value_2.setObjectName(u"lbl_modified_value_2")
        self.lbl_modified_value_2.setFont(font5)
        self.lbl_modified_value_2.setStyleSheet(u"color: rgba(255, 255, 255, 100);")

        self.mod_date_layout_2.addWidget(self.lbl_modified_value_2)


        self.dates_grid_2.addLayout(self.mod_date_layout_2, 2, 0, 1, 1)

        self.create_date_layout_2 = QHBoxLayout()
        self.create_date_layout_2.setObjectName(u"create_date_layout_2")
        self.lbl_date_created_2 = QLabel(self.text_fields_group)
        self.lbl_date_created_2.setObjectName(u"lbl_date_created_2")
        self.lbl_date_created_2.setFont(font5)
        self.lbl_date_created_2.setStyleSheet(u"color: rgba(255, 255, 255, 100);")

        self.create_date_layout_2.addWidget(self.lbl_date_created_2, 0, Qt.AlignRight)

        self.lbl_create_value_2 = QLabel(self.text_fields_group)
        self.lbl_create_value_2.setObjectName(u"lbl_create_value_2")
        self.lbl_create_value_2.setFont(font5)
        self.lbl_create_value_2.setStyleSheet(u"color: rgba(255, 255, 255, 100);")

        self.create_date_layout_2.addWidget(self.lbl_create_value_2)


        self.dates_grid_2.addLayout(self.create_date_layout_2, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.dates_grid_2, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.text_fields_group, 1, 0, 3, 5)

        self.btn_fav = QToolButton(self.widget)
        self.btn_fav.setObjectName(u"btn_fav")
        font6 = QFont()
        font6.setFamilies([u"Nexa-Trial"])
        font6.setPointSize(18)
        self.btn_fav.setFont(font6)
        self.btn_fav.setStyleSheet(u"border-radius: 5px;")

        self.gridLayout_2.addWidget(self.btn_fav, 0, 3, 1, 1)

        QWidget.setTabOrder(self.combo_title, self.le_first_name)
        QWidget.setTabOrder(self.le_first_name, self.le_surname)
        QWidget.setTabOrder(self.le_surname, self.le_email)
        QWidget.setTabOrder(self.le_email, self.le_phone_no)
        QWidget.setTabOrder(self.le_phone_no, self.le_nat_insur_no)
        QWidget.setTabOrder(self.le_nat_insur_no, self.le_pass_no)
        QWidget.setTabOrder(self.le_pass_no, self.le_license_no)
        QWidget.setTabOrder(self.le_license_no, self.te_notes)
        QWidget.setTabOrder(self.te_notes, self.btn_fav)
        QWidget.setTabOrder(self.btn_fav, self.btn_edit)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_item_name.setText(QCoreApplication.translate("Form", u"ItemName", None))
        self.btn_edit.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.combo_title.setItemText(0, QCoreApplication.translate("Form", u"- Select -", None))
        self.combo_title.setItemText(1, QCoreApplication.translate("Form", u"Mr", None))
        self.combo_title.setItemText(2, QCoreApplication.translate("Form", u"Mrs", None))
        self.combo_title.setItemText(3, QCoreApplication.translate("Form", u"Miss", None))
        self.combo_title.setItemText(4, QCoreApplication.translate("Form", u"Ms", None))
        self.combo_title.setItemText(5, QCoreApplication.translate("Form", u"Master", None))
        self.combo_title.setItemText(6, QCoreApplication.translate("Form", u"Dr", None))

        self.lbl_passport_num.setText(QCoreApplication.translate("Form", u"passport number", None))
        self.le_email.setPlaceholderText("")
        self.lbl_first_name.setText(QCoreApplication.translate("Form", u"<span style=\" font-family:'Arial'; font-size:11.5pt;\">f</span>irst name", None))
        self.lbl_phone_number.setText(QCoreApplication.translate("Form", u"phone number", None))
        self.lbl_title.setText(QCoreApplication.translate("Form", u"title", None))
        self.lbl_license_num.setText(QCoreApplication.translate("Form", u"license number", None))
        self.lbl_surname.setText(QCoreApplication.translate("Form", u"last name", None))
        self.le_surname.setPlaceholderText("")
        self.le_first_name.setPlaceholderText("")
        self.lbl_email.setText(QCoreApplication.translate("Form", u"email", None))
        self.lbl_nat_insur_num.setText(QCoreApplication.translate("Form", u"national insurance number", None))
        self.lbl_notes.setText(QCoreApplication.translate("Form", u"notes", None))
        self.lbl_date_modified_2.setText(QCoreApplication.translate("Form", u"Date modified:", None))
        self.lbl_modified_value_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_date_created_2.setText(QCoreApplication.translate("Form", u"Date created:", None))
        self.lbl_create_value_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.btn_fav.setText(QCoreApplication.translate("Form", u"\u2606", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'secure_note_details.ui'
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
    QHBoxLayout, QLabel, QLayout, QSizePolicy,
    QTextEdit, QToolButton, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(364, 521)
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
"\n"
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
        self.btn_edit = QToolButton(self.widget)
        self.btn_edit.setObjectName(u"btn_edit")
        font = QFont()
        font.setFamilies([u"Nexa-Trial"])
        font.setPointSize(12)
        self.btn_edit.setFont(font)
        self.btn_edit.setStyleSheet(u"border-radius: 5px;")

        self.gridLayout_2.addWidget(self.btn_edit, 0, 3, 1, 1)

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

        self.gridLayout.addWidget(self.lbl_notes, 0, 0, 1, 1)

        self.te_notes = QTextEdit(self.text_fields_group)
        self.te_notes.setObjectName(u"te_notes")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.te_notes.sizePolicy().hasHeightForWidth())
        self.te_notes.setSizePolicy(sizePolicy1)
        self.te_notes.setMaximumSize(QSize(16777215, 999999))
        self.te_notes.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px;")
        self.te_notes.setReadOnly(True)

        self.gridLayout.addWidget(self.te_notes, 1, 0, 1, 1)

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
        sizePolicy1.setHeightForWidth(self.combo_folders.sizePolicy().hasHeightForWidth())
        self.combo_folders.setSizePolicy(sizePolicy1)
        self.combo_folders.setMaximumSize(QSize(16777215, 30))
        self.combo_folders.setFont(font1)
        self.combo_folders.setStyleSheet(u"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:6px;\n"
"color: rgba(255, 255, 255, 200);")
        self.combo_folders.setEditable(False)

        self.gridLayout.addWidget(self.combo_folders, 2, 0, 1, 1)

        self.dates_grid = QGridLayout()
        self.dates_grid.setObjectName(u"dates_grid")
        self.mod_date_layout = QHBoxLayout()
        self.mod_date_layout.setObjectName(u"mod_date_layout")
        self.lbl_date_modified = QLabel(self.text_fields_group)
        self.lbl_date_modified.setObjectName(u"lbl_date_modified")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(9)
        self.lbl_date_modified.setFont(font2)
        self.lbl_date_modified.setStyleSheet(u"color: rgba(255, 255, 255, 100);")

        self.mod_date_layout.addWidget(self.lbl_date_modified, 0, Qt.AlignRight)

        self.lbl_modified_value = QLabel(self.text_fields_group)
        self.lbl_modified_value.setObjectName(u"lbl_modified_value")
        self.lbl_modified_value.setFont(font2)
        self.lbl_modified_value.setStyleSheet(u"color: rgba(255, 255, 255, 100);")

        self.mod_date_layout.addWidget(self.lbl_modified_value)


        self.dates_grid.addLayout(self.mod_date_layout, 2, 0, 1, 1)

        self.create_date_layout = QHBoxLayout()
        self.create_date_layout.setObjectName(u"create_date_layout")
        self.lbl_date_created = QLabel(self.text_fields_group)
        self.lbl_date_created.setObjectName(u"lbl_date_created")
        self.lbl_date_created.setFont(font2)
        self.lbl_date_created.setStyleSheet(u"color: rgba(255, 255, 255, 100);")

        self.create_date_layout.addWidget(self.lbl_date_created, 0, Qt.AlignRight)

        self.lbl_create_value = QLabel(self.text_fields_group)
        self.lbl_create_value.setObjectName(u"lbl_create_value")
        self.lbl_create_value.setFont(font2)
        self.lbl_create_value.setStyleSheet(u"color: rgba(255, 255, 255, 100);")

        self.create_date_layout.addWidget(self.lbl_create_value)


        self.dates_grid.addLayout(self.create_date_layout, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.dates_grid, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.text_fields_group, 2, 0, 2, 4)

        self.lbl_item_name = QLabel(self.widget)
        self.lbl_item_name.setObjectName(u"lbl_item_name")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbl_item_name.sizePolicy().hasHeightForWidth())
        self.lbl_item_name.setSizePolicy(sizePolicy2)
        self.lbl_item_name.setMaximumSize(QSize(364, 112))
        font3 = QFont()
        font3.setFamilies([u"Nexa-Trial"])
        font3.setPointSize(31)
        font3.setBold(True)
        self.lbl_item_name.setFont(font3)
        self.lbl_item_name.setStyleSheet(u"color: rgba(255,255,255, 220);")
        self.lbl_item_name.setTextFormat(Qt.RichText)

        self.gridLayout_2.addWidget(self.lbl_item_name, 0, 0, 1, 1)

        self.btn_fav = QToolButton(self.widget)
        self.btn_fav.setObjectName(u"btn_fav")
        font4 = QFont()
        font4.setFamilies([u"Nexa-Trial"])
        font4.setPointSize(18)
        self.btn_fav.setFont(font4)
        self.btn_fav.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.btn_fav, 0, 2, 1, 1)

        QWidget.setTabOrder(self.te_notes, self.combo_folders)
        QWidget.setTabOrder(self.combo_folders, self.btn_fav)
        QWidget.setTabOrder(self.btn_fav, self.btn_edit)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_edit.setText(QCoreApplication.translate("Form", u"Edit", None))
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

        self.lbl_date_modified.setText(QCoreApplication.translate("Form", u"Date modified:", None))
        self.lbl_modified_value.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_date_created.setText(QCoreApplication.translate("Form", u"Date created:", None))
        self.lbl_create_value.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_item_name.setText(QCoreApplication.translate("Form", u"ItemName", None))
        self.btn_fav.setText(QCoreApplication.translate("Form", u"\u2606", None))
    # retranslateUi


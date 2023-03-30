# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_secure_note_screen.ui'
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
        Form.resize(524, 624)
        self.gridLayout_4 = QGridLayout(Form)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(500, 600))
        self.widget.setMaximumSize(QSize(500, 600))
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

        self.lbl_secure_note = QLabel(self.widget)
        self.lbl_secure_note.setObjectName(u"lbl_secure_note")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbl_secure_note.sizePolicy().hasHeightForWidth())
        self.lbl_secure_note.setSizePolicy(sizePolicy2)
        self.lbl_secure_note.setMaximumSize(QSize(364, 112))
        font1 = QFont()
        font1.setFamilies([u"Nexa-Trial"])
        font1.setPointSize(31)
        self.lbl_secure_note.setFont(font1)
        self.lbl_secure_note.setStyleSheet(u"color: rgba(255,255,255, 220);")
        self.lbl_secure_note.setTextFormat(Qt.RichText)

        self.gridLayout_2.addWidget(self.lbl_secure_note, 2, 0, 1, 2, Qt.AlignLeft)

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
        self.btn_save = QToolButton(self.text_fields_group)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy4)
        self.btn_save.setMaximumSize(QSize(16777215, 44))
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

        self.gridLayout.addWidget(self.btn_save, 5, 0, 1, 1)

        self.te_notes = QTextEdit(self.text_fields_group)
        self.te_notes.setObjectName(u"te_notes")
        self.te_notes.setMaximumSize(QSize(16777215, 300))
        self.te_notes.setStyleSheet(u"background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px;")

        self.gridLayout.addWidget(self.te_notes, 3, 0, 1, 1)

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
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.combo_folders.sizePolicy().hasHeightForWidth())
        self.combo_folders.setSizePolicy(sizePolicy5)
        self.combo_folders.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setFamilies([u"Nexa-Trial"])
        self.combo_folders.setFont(font3)
        self.combo_folders.setStyleSheet(u"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:6px;\n"
"color: rgba(255, 255, 255, 200);")

        self.gridLayout.addWidget(self.combo_folders, 4, 0, 1, 1)

        self.le_name = QLineEdit(self.text_fields_group)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setMinimumSize(QSize(0, 40))
        font4 = QFont()
        font4.setFamilies([u".AppleSystemUIFont"])
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

        self.lbl_notes = QLabel(self.text_fields_group)
        self.lbl_notes.setObjectName(u"lbl_notes")
        self.lbl_notes.setMinimumSize(QSize(0, 10))
        self.lbl_notes.setMaximumSize(QSize(16777215, 10))
        self.lbl_notes.setFont(font3)
        self.lbl_notes.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout.addWidget(self.lbl_notes, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.text_fields_group, 5, 0, 1, 2)


        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_back.setText(QCoreApplication.translate("Form", u"<", None))
        self.lbl_secure_note.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:700;\">New Secure Note</span></p></body></html>", None))
        self.btn_save.setText(QCoreApplication.translate("Form", u"save", None))
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

        self.le_name.setPlaceholderText("")
        self.lbl_name.setText(QCoreApplication.translate("Form", u"name", None))
        self.lbl_notes.setText(QCoreApplication.translate("Form", u"notes", None))
    # retranslateUi


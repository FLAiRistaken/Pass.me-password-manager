# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_item_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(524, 561)
        Form.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(500, 537))
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
"QFrame#button_group {\n"
"	background-color: rgba(255, 255, 255, 25);\n"
"	padding: 10px;\n"
"}\n"
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
        self.divider = QFrame(self.widget)
        self.divider.setObjectName(u"divider")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.divider.sizePolicy().hasHeightForWidth())
        self.divider.setSizePolicy(sizePolicy1)
        self.divider.setMaximumSize(QSize(16777215, 1))
        self.divider.setStyleSheet(u"background-color: rgba(255, 255, 255, 80);\n"
"border: none;")
        self.divider.setFrameShape(QFrame.HLine)
        self.divider.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.divider, 3, 0, 1, 2)

        self.lblNewItemTitle = QLabel(self.widget)
        self.lblNewItemTitle.setObjectName(u"lblNewItemTitle")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lblNewItemTitle.sizePolicy().hasHeightForWidth())
        self.lblNewItemTitle.setSizePolicy(sizePolicy2)
        self.lblNewItemTitle.setMaximumSize(QSize(364, 112))
        font = QFont()
        font.setFamilies([u"Nexa-Trial"])
        font.setPointSize(31)
        self.lblNewItemTitle.setFont(font)
        self.lblNewItemTitle.setStyleSheet(u"color: rgba(255,255,255, 220);")
        self.lblNewItemTitle.setTextFormat(Qt.RichText)

        self.gridLayout_2.addWidget(self.lblNewItemTitle, 1, 0, 1, 2, Qt.AlignLeft)

        self.btnClose = QPushButton(self.widget)
        self.btnClose.setObjectName(u"btnClose")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy3)
        self.btnClose.setMinimumSize(QSize(5, 0))
        self.btnClose.setMaximumSize(QSize(11, 21))
        font1 = QFont()
        font1.setFamilies([u"Nexa-Trial"])
        font1.setPointSize(16)
        self.btnClose.setFont(font1)
        self.btnClose.setStyleSheet(u"border: none;")

        self.gridLayout_2.addWidget(self.btnClose, 0, 0, 1, 1)

        self.button_group = QFrame(self.widget)
        self.button_group.setObjectName(u"button_group")
        self.button_group.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.button_group)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_item_identity = QToolButton(self.button_group)
        self.btn_item_identity.setObjectName(u"btn_item_identity")
        self.btn_item_identity.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_item_identity.sizePolicy().hasHeightForWidth())
        self.btn_item_identity.setSizePolicy(sizePolicy4)
        self.btn_item_identity.setMaximumSize(QSize(16777215, 75))
        self.btn_item_identity.setFont(font1)
        self.btn_item_identity.setLayoutDirection(Qt.LeftToRight)
        self.btn_item_identity.setStyleSheet(u"")
        self.btn_item_identity.setPopupMode(QToolButton.InstantPopup)
        self.btn_item_identity.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.btn_item_identity.setAutoRaise(False)
        self.btn_item_identity.setArrowType(Qt.NoArrow)

        self.gridLayout.addWidget(self.btn_item_identity, 1, 1, 1, 1)

        self.btn_item_bank_card = QToolButton(self.button_group)
        self.btn_item_bank_card.setObjectName(u"btn_item_bank_card")
        self.btn_item_bank_card.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.btn_item_bank_card.sizePolicy().hasHeightForWidth())
        self.btn_item_bank_card.setSizePolicy(sizePolicy4)
        self.btn_item_bank_card.setMaximumSize(QSize(16777215, 75))
        self.btn_item_bank_card.setFont(font1)
        self.btn_item_bank_card.setLayoutDirection(Qt.LeftToRight)
        self.btn_item_bank_card.setStyleSheet(u"")
        self.btn_item_bank_card.setPopupMode(QToolButton.InstantPopup)
        self.btn_item_bank_card.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.btn_item_bank_card.setAutoRaise(False)
        self.btn_item_bank_card.setArrowType(Qt.NoArrow)

        self.gridLayout.addWidget(self.btn_item_bank_card, 0, 1, 1, 1)

        self.btn_item_bank_acc = QToolButton(self.button_group)
        self.btn_item_bank_acc.setObjectName(u"btn_item_bank_acc")
        self.btn_item_bank_acc.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.btn_item_bank_acc.sizePolicy().hasHeightForWidth())
        self.btn_item_bank_acc.setSizePolicy(sizePolicy4)
        self.btn_item_bank_acc.setMaximumSize(QSize(16777215, 75))
        self.btn_item_bank_acc.setFont(font1)
        self.btn_item_bank_acc.setLayoutDirection(Qt.LeftToRight)
        self.btn_item_bank_acc.setStyleSheet(u"")
        self.btn_item_bank_acc.setPopupMode(QToolButton.InstantPopup)
        self.btn_item_bank_acc.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.btn_item_bank_acc.setAutoRaise(False)
        self.btn_item_bank_acc.setArrowType(Qt.NoArrow)

        self.gridLayout.addWidget(self.btn_item_bank_acc, 1, 0, 1, 1)

        self.btn_item_login = QToolButton(self.button_group)
        self.btn_item_login.setObjectName(u"btn_item_login")
        self.btn_item_login.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.btn_item_login.sizePolicy().hasHeightForWidth())
        self.btn_item_login.setSizePolicy(sizePolicy4)
        self.btn_item_login.setMaximumSize(QSize(16777215, 75))
        self.btn_item_login.setFont(font1)
        self.btn_item_login.setLayoutDirection(Qt.LeftToRight)
        self.btn_item_login.setStyleSheet(u"")
        self.btn_item_login.setPopupMode(QToolButton.InstantPopup)
        self.btn_item_login.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.btn_item_login.setAutoRaise(False)
        self.btn_item_login.setArrowType(Qt.NoArrow)

        self.gridLayout.addWidget(self.btn_item_login, 0, 0, 1, 1)

        self.btn_item_note = QToolButton(self.button_group)
        self.btn_item_note.setObjectName(u"btn_item_note")
        self.btn_item_note.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.btn_item_note.sizePolicy().hasHeightForWidth())
        self.btn_item_note.setSizePolicy(sizePolicy4)
        self.btn_item_note.setMaximumSize(QSize(16777215, 75))
        self.btn_item_note.setFont(font1)
        self.btn_item_note.setLayoutDirection(Qt.LeftToRight)
        self.btn_item_note.setStyleSheet(u"")
        self.btn_item_note.setPopupMode(QToolButton.InstantPopup)
        self.btn_item_note.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.btn_item_note.setAutoRaise(False)
        self.btn_item_note.setArrowType(Qt.NoArrow)

        self.gridLayout.addWidget(self.btn_item_note, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.button_group, 4, 0, 1, 2)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblNewItemTitle.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Select desired item </p><p>to add to your <span style=\" font-weight:700;\">pass.me</span></p></body></html>", None))
        self.btnClose.setText(QCoreApplication.translate("Form", u"X", None))
        self.btn_item_identity.setText(QCoreApplication.translate("Form", u"identity", None))
        self.btn_item_bank_card.setText(QCoreApplication.translate("Form", u"bank card", None))
        self.btn_item_bank_acc.setText(QCoreApplication.translate("Form", u"bank account", None))
        self.btn_item_login.setText(QCoreApplication.translate("Form", u"login", None))
        self.btn_item_note.setText(QCoreApplication.translate("Form", u"secure note", None))
    # retranslateUi


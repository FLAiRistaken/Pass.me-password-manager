# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'password_generator.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QRadioButton, QSizePolicy,
    QToolButton, QVBoxLayout, QWidget)
import icons_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(873, 668)
        Form.setStyleSheet(u"QWidget#widget{\n"
"	background-color: rgba(32, 32, 32, 255);\n"
"	border-radius: 8px;\n"
"}")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(800, 492))
        self.widget.setStyleSheet(u"QPushButton#btnClose{\n"
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
"QFrame#frame_pass_history {\n"
"	background-color: rgb(23, 23, 23);\n"
"	border-radius: 8px;\n"
"}\n"
"QFrame#frame_pass_type {\n"
"	background-color: rgb(23, 23, 23);\n"
"	border-radius: 5px;\n"
"}\n"
"QFrame#frame_options{\n"
"	background-color: rgb(23, 23, 23);\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QToolButton#btn_gen_pass {\n"
"	background-color: rgb(23, 23, 23);\n"
"	border: none;\n"
"}\n"
"\n"
"QToolButton#btn_copy {\n"
"	background-color: rgb(23, 23, 23);\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QToolButton#btn_copy:hover{\n"
"	background-color: rgb(35, 35, 35);\n"
"}\n"
"\n"
"QToolButton#btn_gen_pass:hover{\n"
"	background-color: rgb(35, 35, 35);\n"
"}\n"
"\n"
"QToolButton#btn_copy:pressed{\n"
"	background-color: rgb(40, 40, "
                        "40);\n"
"}\n"
"\n"
"QToolButton#btn_gen_pass:pressed{\n"
"	background-color: rgb(40, 40, 40);\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btnClose = QPushButton(self.widget)
        self.btnClose.setObjectName(u"btnClose")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy)
        self.btnClose.setMinimumSize(QSize(5, 0))
        self.btnClose.setMaximumSize(QSize(11, 21))
        font = QFont()
        font.setFamilies([u"Nexa-Trial"])
        font.setPointSize(16)
        self.btnClose.setFont(font)
        self.btnClose.setStyleSheet(u"border: none;")

        self.gridLayout_2.addWidget(self.btnClose, 0, 0, 1, 1)

        self.frame_pass_history = QFrame(self.widget)
        self.frame_pass_history.setObjectName(u"frame_pass_history")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_pass_history.sizePolicy().hasHeightForWidth())
        self.frame_pass_history.setSizePolicy(sizePolicy1)
        self.frame_pass_history.setMinimumSize(QSize(200, 0))
        self.frame_pass_history.setMaximumSize(QSize(250, 468))
        self.frame_pass_history.setStyleSheet(u"")
        self.frame_pass_history.setFrameShape(QFrame.StyledPanel)
        self.frame_pass_history.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_pass_history)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_history = QLabel(self.frame_pass_history)
        self.lbl_history.setObjectName(u"lbl_history")
        font1 = QFont()
        font1.setFamilies([u"Nexa-Trial"])
        self.lbl_history.setFont(font1)

        self.verticalLayout.addWidget(self.lbl_history)

        self.listWidget = QListWidget(self.frame_pass_history)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.listWidget)


        self.gridLayout_2.addWidget(self.frame_pass_history, 0, 2, 3, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lbl_options = QLabel(self.widget)
        self.lbl_options.setObjectName(u"lbl_options")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbl_options.sizePolicy().hasHeightForWidth())
        self.lbl_options.setSizePolicy(sizePolicy3)
        self.lbl_options.setMaximumSize(QSize(508, 17))
        self.lbl_options.setFont(font1)

        self.gridLayout_3.addWidget(self.lbl_options, 4, 0, 1, 1)

        self.frame_pass_type = QFrame(self.widget)
        self.frame_pass_type.setObjectName(u"frame_pass_type")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_pass_type.sizePolicy().hasHeightForWidth())
        self.frame_pass_type.setSizePolicy(sizePolicy4)
        self.frame_pass_type.setMinimumSize(QSize(0, 75))
        self.frame_pass_type.setMaximumSize(QSize(508, 75))
        self.frame_pass_type.setFrameShape(QFrame.StyledPanel)
        self.frame_pass_type.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_pass_type)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.rad_password = QRadioButton(self.frame_pass_type)
        self.rad_password.setObjectName(u"rad_password")
        self.rad_password.setChecked(True)

        self.gridLayout_4.addWidget(self.rad_password, 1, 0, 1, 1)

        self.lbl_pass_type = QLabel(self.frame_pass_type)
        self.lbl_pass_type.setObjectName(u"lbl_pass_type")
        self.lbl_pass_type.setFont(font1)

        self.gridLayout_4.addWidget(self.lbl_pass_type, 0, 0, 1, 1)

        self.rad_passphrase = QRadioButton(self.frame_pass_type)
        self.rad_passphrase.setObjectName(u"rad_passphrase")

        self.gridLayout_4.addWidget(self.rad_passphrase, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame_pass_type, 5, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.le_password = QLineEdit(self.widget)
        self.le_password.setObjectName(u"le_password")
        sizePolicy4.setHeightForWidth(self.le_password.sizePolicy().hasHeightForWidth())
        self.le_password.setSizePolicy(sizePolicy4)
        self.le_password.setMinimumSize(QSize(0, 45))
        self.le_password.setMaximumSize(QSize(448, 45))
        font2 = QFont()
        font2.setPointSize(16)
        self.le_password.setFont(font2)
        self.le_password.setStyleSheet(u"background-color: rgb(23, 23, 23);\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_password.setReadOnly(True)
        self.le_password.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.le_password)

        self.btn_gen_pass = QToolButton(self.widget)
        self.btn_gen_pass.setObjectName(u"btn_gen_pass")
        self.btn_gen_pass.setMaximumSize(QSize(30, 45))
        self.btn_gen_pass.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/pass_gen/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_gen_pass.setIcon(icon)
        self.btn_gen_pass.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_gen_pass)

        self.btn_copy = QToolButton(self.widget)
        self.btn_copy.setObjectName(u"btn_copy")
        self.btn_copy.setMaximumSize(QSize(30, 45))
        self.btn_copy.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/pass_gen/copypaste_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_copy.setIcon(icon1)
        self.btn_copy.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_copy)


        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 0, 2, 1)


        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)


        self.retranslateUi(Form)
        self.btn_copy.clicked.connect(self.le_password.copy)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btnClose.setText(QCoreApplication.translate("Form", u"X", None))
        self.lbl_history.setText(QCoreApplication.translate("Form", u"Password History", None))
        self.lbl_options.setText(QCoreApplication.translate("Form", u"Options", None))
        self.rad_password.setText(QCoreApplication.translate("Form", u"Password", None))
        self.lbl_pass_type.setText(QCoreApplication.translate("Form", u"Password Type", None))
        self.rad_passphrase.setText(QCoreApplication.translate("Form", u"Passphrase", None))
        self.btn_gen_pass.setText("")
        self.btn_copy.setText("")
    # retranslateUi


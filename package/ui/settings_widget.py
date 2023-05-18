# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget)
from icons import rc_icons

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(724, 409)
        font = QFont()
        font.setBold(True)
        Form.setFont(font)
        Form.setStyleSheet(u"QWidget#widget{\n"
"	background-color: rgba(32, 32, 32, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QWidget#acc_sett_box{\n"
"	background-color: rgba(32, 32, 32, 100);\n"
"	border-radius: 8px;\n"
"}")
        self.gridLayout_6 = QGridLayout(Form)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(700, 400))
        self.widget.setStyleSheet(u"QWidget#menu_widget{\n"
"	background-color: rgba(52, 52, 52, 255);\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QWidget#acc_sett_box{\n"
"	background-color: rgba(32, 32, 32, 100);\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QWidget#pass_reset_box{\n"
"	background-color: rgba(32, 32, 32, 100);\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QWidget#email_reset_box{\n"
"	background-color: rgba(32, 32, 32, 100);\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QStackedWidget{\n"
"	background-color: rgba(52, 52, 52, 255);\n"
"	border-radius: 8px;\n"
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
"QFrame#frame_pass_history {\n"
"	background-color: rgb(23, 23, 23);\n"
"	border-radius: 8px;\n"
"}\n"
"QFrame#frame_pass_type {\n"
"	background-color: rgb(23, 23, 23);\n"
"	border-radius: 5px;\n"
"}\n"
"QFrame#frame_options{\n"
"	background-color: rgb(23"
                        ", 23, 23);\n"
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
"	background-color: rgb(40, 40, 40);\n"
"}\n"
"\n"
"QToolButton#btn_gen_pass:pressed{\n"
"	background-color: rgb(40, 40, 40);\n"
"}\n"
"")
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.btn_close = QPushButton(self.widget)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMinimumSize(QSize(5, 0))
        self.btn_close.setMaximumSize(QSize(11, 21))
        font1 = QFont()
        font1.setFamilies([u"Nexa-Trial"])
        font1.setPointSize(16)
        self.btn_close.setFont(font1)
        self.btn_close.setStyleSheet(u"border: none;")

        self.gridLayout_5.addWidget(self.btn_close, 0, 0, 1, 1)

        self.lbl_curr_page = QLabel(self.widget)
        self.lbl_curr_page.setObjectName(u"lbl_curr_page")
        font2 = QFont()
        font2.setFamilies([u"Nexa-Trial"])
        font2.setPointSize(18)
        self.lbl_curr_page.setFont(font2)

        self.gridLayout_5.addWidget(self.lbl_curr_page, 0, 2, 1, 1)

        self.stacked_widget = QStackedWidget(self.widget)
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.stacked_widget.setStyleSheet(u"QPushButton#btn_back{\n"
"	color:rgba(255, 255, 255, 220);\n"
"}\n"
"QPushButton#btn_back:pressed{\n"
"	color: rgba(126, 126, 126, 220);\n"
"\n"
"}\n"
"QPushButton#btn_back:hover{\n"
"	color: rgba(190, 190, 190, 220);\n"
"}")
        self.page_acc_sett = QWidget()
        self.page_acc_sett.setObjectName(u"page_acc_sett")
        self.page_acc_sett.setStyleSheet(u"QWidget#acc_sett_box{\n"
"	background-color: rgba(32, 32, 32, 100);\n"
"	border-radius: 8px;\n"
"}")
        self.gridLayout = QGridLayout(self.page_acc_sett)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(12, 12, 12, 12)
        self.acc_sett_box = QWidget(self.page_acc_sett)
        self.acc_sett_box.setObjectName(u"acc_sett_box")
        self.acc_sett_box.setMinimumSize(QSize(0, 230))
        self.acc_sett_box.setStyleSheet(u"QPushButton {\n"
"	border-radius: 5px;\n"
"	background-color: rgba(255, 255, 255, 20);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton#btn_logout{\n"
"	background-color: rgba(148, 105, 141, 200);\n"
"}\n"
"\n"
"QPushButton::hover#btn_logout{\n"
"	background-color: rgba(148, 105, 141, 230);\n"
"}")
        self.gridLayout_2 = QGridLayout(self.acc_sett_box)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbl_chg_email = QLabel(self.acc_sett_box)
        self.lbl_chg_email.setObjectName(u"lbl_chg_email")
        font3 = QFont()
        font3.setFamilies([u"Nexa-Trial"])
        font3.setPointSize(14)
        self.lbl_chg_email.setFont(font3)

        self.gridLayout_2.addWidget(self.lbl_chg_email, 1, 0, 1, 1)

        self.btn_logout = QPushButton(self.acc_sett_box)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy1)
        self.btn_logout.setMinimumSize(QSize(445, 40))
        self.btn_logout.setMaximumSize(QSize(16777215, 40))
        font4 = QFont()
        font4.setFamilies([u"Nexa-Trial"])
        font4.setPointSize(15)
        self.btn_logout.setFont(font4)
        self.btn_logout.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.btn_logout, 2, 0, 1, 2)

        self.btn_chg_pass = QPushButton(self.acc_sett_box)
        self.btn_chg_pass.setObjectName(u"btn_chg_pass")
        sizePolicy1.setHeightForWidth(self.btn_chg_pass.sizePolicy().hasHeightForWidth())
        self.btn_chg_pass.setSizePolicy(sizePolicy1)
        self.btn_chg_pass.setMinimumSize(QSize(215, 40))
        self.btn_chg_pass.setMaximumSize(QSize(16777215, 40))
        font5 = QFont()
        font5.setFamilies([u"Nexa-Trial"])
        self.btn_chg_pass.setFont(font5)

        self.gridLayout_2.addWidget(self.btn_chg_pass, 0, 1, 1, 1)

        self.lbl_chg_pass = QLabel(self.acc_sett_box)
        self.lbl_chg_pass.setObjectName(u"lbl_chg_pass")
        self.lbl_chg_pass.setFont(font3)

        self.gridLayout_2.addWidget(self.lbl_chg_pass, 0, 0, 1, 1)

        self.btn_chg_email = QPushButton(self.acc_sett_box)
        self.btn_chg_email.setObjectName(u"btn_chg_email")
        sizePolicy1.setHeightForWidth(self.btn_chg_email.sizePolicy().hasHeightForWidth())
        self.btn_chg_email.setSizePolicy(sizePolicy1)
        self.btn_chg_email.setMinimumSize(QSize(215, 40))
        self.btn_chg_email.setMaximumSize(QSize(16777215, 40))
        self.btn_chg_email.setFont(font5)

        self.gridLayout_2.addWidget(self.btn_chg_email, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.acc_sett_box, 3, 0, 1, 1)

        self.lbl_user_email = QLabel(self.page_acc_sett)
        self.lbl_user_email.setObjectName(u"lbl_user_email")
        font6 = QFont()
        font6.setFamilies([u"Tahoma"])
        font6.setPointSize(16)
        self.lbl_user_email.setFont(font6)
        self.lbl_user_email.setStyleSheet(u"color: rgba(255, 255, 255, 160);")

        self.gridLayout.addWidget(self.lbl_user_email, 1, 0, 1, 1)

        self.lbl_user_name = QLabel(self.page_acc_sett)
        self.lbl_user_name.setObjectName(u"lbl_user_name")
        font7 = QFont()
        font7.setFamilies([u"Nexa-Trial"])
        font7.setPointSize(20)
        self.lbl_user_name.setFont(font7)

        self.gridLayout.addWidget(self.lbl_user_name, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.stacked_widget.addWidget(self.page_acc_sett)
        self.page_pass_reset = QWidget()
        self.page_pass_reset.setObjectName(u"page_pass_reset")
        self.gridLayout_4 = QGridLayout(self.page_pass_reset)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lbl_user_name_pass_reset = QLabel(self.page_pass_reset)
        self.lbl_user_name_pass_reset.setObjectName(u"lbl_user_name_pass_reset")
        self.lbl_user_name_pass_reset.setFont(font7)

        self.gridLayout_4.addWidget(self.lbl_user_name_pass_reset, 0, 0, 1, 1)

        self.lbl_user_email_pass_reset = QLabel(self.page_pass_reset)
        self.lbl_user_email_pass_reset.setObjectName(u"lbl_user_email_pass_reset")
        self.lbl_user_email_pass_reset.setFont(font6)
        self.lbl_user_email_pass_reset.setStyleSheet(u"color: rgba(255, 255, 255, 160);")

        self.gridLayout_4.addWidget(self.lbl_user_email_pass_reset, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 3, 0, 1, 2)

        self.pass_reset_box = QWidget(self.page_pass_reset)
        self.pass_reset_box.setObjectName(u"pass_reset_box")
        self.pass_reset_box.setMinimumSize(QSize(0, 230))
        self.pass_reset_box.setStyleSheet(u"QPushButton#btn_change_pass{\n"
"	border-radius: 5px;\n"
"	background-color: rgba(148, 105, 141, 200);\n"
"}\n"
"\n"
"QPushButton#btn_change_pass::hover{\n"
"	background-color: rgba(148, 105, 141, 230);\n"
"}")
        self.gridLayout_3 = QGridLayout(self.pass_reset_box)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lbl_old_pass = QLabel(self.pass_reset_box)
        self.lbl_old_pass.setObjectName(u"lbl_old_pass")
        self.lbl_old_pass.setFont(font3)

        self.gridLayout_3.addWidget(self.lbl_old_pass, 0, 0, 1, 1)

        self.lbl_new_pass = QLabel(self.pass_reset_box)
        self.lbl_new_pass.setObjectName(u"lbl_new_pass")
        self.lbl_new_pass.setFont(font3)

        self.gridLayout_3.addWidget(self.lbl_new_pass, 1, 0, 1, 1)

        self.le_new_pass_ver = QLineEdit(self.pass_reset_box)
        self.le_new_pass_ver.setObjectName(u"le_new_pass_ver")
        self.le_new_pass_ver.setMinimumSize(QSize(0, 30))
        font8 = QFont()
        font8.setFamilies([u".AppleSystemUIFont"])
        self.le_new_pass_ver.setFont(font8)
        self.le_new_pass_ver.setStyleSheet(u"background-color: rgba(33, 33, 33, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_new_pass_ver.setMaxLength(64)
        self.le_new_pass_ver.setEchoMode(QLineEdit.Normal)
        self.le_new_pass_ver.setReadOnly(False)

        self.gridLayout_3.addWidget(self.le_new_pass_ver, 3, 2, 1, 1)

        self.le_old_pass = QLineEdit(self.pass_reset_box)
        self.le_old_pass.setObjectName(u"le_old_pass")
        self.le_old_pass.setMinimumSize(QSize(0, 30))
        self.le_old_pass.setFont(font8)
        self.le_old_pass.setStyleSheet(u"background-color: rgba(33, 33, 33, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_old_pass.setMaxLength(64)
        self.le_old_pass.setEchoMode(QLineEdit.Normal)
        self.le_old_pass.setReadOnly(False)

        self.gridLayout_3.addWidget(self.le_old_pass, 0, 2, 1, 1)

        self.le_new_pass = QLineEdit(self.pass_reset_box)
        self.le_new_pass.setObjectName(u"le_new_pass")
        self.le_new_pass.setMinimumSize(QSize(0, 30))
        self.le_new_pass.setFont(font8)
        self.le_new_pass.setStyleSheet(u"background-color: rgba(33, 33, 33, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_new_pass.setMaxLength(64)
        self.le_new_pass.setEchoMode(QLineEdit.Normal)
        self.le_new_pass.setReadOnly(False)

        self.gridLayout_3.addWidget(self.le_new_pass, 1, 2, 1, 1)

        self.btn_change_pass = QPushButton(self.pass_reset_box)
        self.btn_change_pass.setObjectName(u"btn_change_pass")
        sizePolicy1.setHeightForWidth(self.btn_change_pass.sizePolicy().hasHeightForWidth())
        self.btn_change_pass.setSizePolicy(sizePolicy1)
        self.btn_change_pass.setMaximumSize(QSize(16777215, 40))
        self.btn_change_pass.setFont(font4)
        self.btn_change_pass.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.btn_change_pass, 4, 0, 1, 3)

        self.lbl_new_pass_ver = QLabel(self.pass_reset_box)
        self.lbl_new_pass_ver.setObjectName(u"lbl_new_pass_ver")
        self.lbl_new_pass_ver.setFont(font3)

        self.gridLayout_3.addWidget(self.lbl_new_pass_ver, 3, 0, 1, 1)


        self.gridLayout_4.addWidget(self.pass_reset_box, 4, 0, 1, 2)

        self.btn_back_pass = QPushButton(self.page_pass_reset)
        self.btn_back_pass.setObjectName(u"btn_back_pass")
        sizePolicy.setHeightForWidth(self.btn_back_pass.sizePolicy().hasHeightForWidth())
        self.btn_back_pass.setSizePolicy(sizePolicy)
        self.btn_back_pass.setMinimumSize(QSize(5, 0))
        self.btn_back_pass.setMaximumSize(QSize(11, 21))
        font9 = QFont()
        font9.setFamilies([u"Tahoma"])
        font9.setPointSize(16)
        font9.setBold(True)
        self.btn_back_pass.setFont(font9)
        self.btn_back_pass.setStyleSheet(u"border: none;")

        self.gridLayout_4.addWidget(self.btn_back_pass, 0, 1, 1, 1)

        self.stacked_widget.addWidget(self.page_pass_reset)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_8 = QGridLayout(self.page)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.lbl_user_name_email_reset = QLabel(self.page)
        self.lbl_user_name_email_reset.setObjectName(u"lbl_user_name_email_reset")
        self.lbl_user_name_email_reset.setFont(font7)

        self.gridLayout_8.addWidget(self.lbl_user_name_email_reset, 0, 0, 1, 1)

        self.lbl_user_email_email_reset = QLabel(self.page)
        self.lbl_user_email_email_reset.setObjectName(u"lbl_user_email_email_reset")
        self.lbl_user_email_email_reset.setFont(font6)
        self.lbl_user_email_email_reset.setStyleSheet(u"color: rgba(255, 255, 255, 160);")

        self.gridLayout_8.addWidget(self.lbl_user_email_email_reset, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_4, 2, 0, 1, 2)

        self.btn_back_email = QPushButton(self.page)
        self.btn_back_email.setObjectName(u"btn_back_email")
        sizePolicy.setHeightForWidth(self.btn_back_email.sizePolicy().hasHeightForWidth())
        self.btn_back_email.setSizePolicy(sizePolicy)
        self.btn_back_email.setMinimumSize(QSize(5, 0))
        self.btn_back_email.setMaximumSize(QSize(11, 21))
        self.btn_back_email.setFont(font9)
        self.btn_back_email.setStyleSheet(u"border: none;")

        self.gridLayout_8.addWidget(self.btn_back_email, 0, 1, 1, 1)

        self.email_reset_box = QWidget(self.page)
        self.email_reset_box.setObjectName(u"email_reset_box")
        self.email_reset_box.setMinimumSize(QSize(0, 230))
        self.email_reset_box.setStyleSheet(u"QPushButton#btn_change_email{\n"
"	border-radius: 5px;\n"
"	background-color: rgba(148, 105, 141, 200);\n"
"}\n"
"\n"
"QPushButton#btn_change_email::hover{\n"
"	background-color: rgba(148, 105, 141, 230);\n"
"}")
        self.gridLayout_7 = QGridLayout(self.email_reset_box)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.lbl_old_email = QLabel(self.email_reset_box)
        self.lbl_old_email.setObjectName(u"lbl_old_email")
        self.lbl_old_email.setFont(font3)

        self.gridLayout_7.addWidget(self.lbl_old_email, 0, 0, 1, 1)

        self.lbl_new_email = QLabel(self.email_reset_box)
        self.lbl_new_email.setObjectName(u"lbl_new_email")
        self.lbl_new_email.setFont(font3)

        self.gridLayout_7.addWidget(self.lbl_new_email, 1, 0, 1, 1)

        self.le_new_email_ver = QLineEdit(self.email_reset_box)
        self.le_new_email_ver.setObjectName(u"le_new_email_ver")
        self.le_new_email_ver.setMinimumSize(QSize(0, 30))
        self.le_new_email_ver.setFont(font8)
        self.le_new_email_ver.setStyleSheet(u"background-color: rgba(33, 33, 33, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_new_email_ver.setMaxLength(64)
        self.le_new_email_ver.setEchoMode(QLineEdit.Normal)
        self.le_new_email_ver.setReadOnly(False)

        self.gridLayout_7.addWidget(self.le_new_email_ver, 3, 2, 1, 1)

        self.le_old_email = QLineEdit(self.email_reset_box)
        self.le_old_email.setObjectName(u"le_old_email")
        self.le_old_email.setMinimumSize(QSize(0, 30))
        self.le_old_email.setFont(font8)
        self.le_old_email.setStyleSheet(u"background-color: rgba(33, 33, 33, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_old_email.setMaxLength(64)
        self.le_old_email.setEchoMode(QLineEdit.Normal)
        self.le_old_email.setReadOnly(False)

        self.gridLayout_7.addWidget(self.le_old_email, 0, 2, 1, 1)

        self.le_new_email = QLineEdit(self.email_reset_box)
        self.le_new_email.setObjectName(u"le_new_email")
        self.le_new_email.setMinimumSize(QSize(0, 30))
        self.le_new_email.setFont(font8)
        self.le_new_email.setStyleSheet(u"background-color: rgba(33, 33, 33, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.le_new_email.setMaxLength(64)
        self.le_new_email.setEchoMode(QLineEdit.Normal)
        self.le_new_email.setReadOnly(False)

        self.gridLayout_7.addWidget(self.le_new_email, 1, 2, 1, 1)

        self.btn_change_email = QPushButton(self.email_reset_box)
        self.btn_change_email.setObjectName(u"btn_change_email")
        sizePolicy1.setHeightForWidth(self.btn_change_email.sizePolicy().hasHeightForWidth())
        self.btn_change_email.setSizePolicy(sizePolicy1)
        self.btn_change_email.setMaximumSize(QSize(16777215, 40))
        self.btn_change_email.setFont(font4)
        self.btn_change_email.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.btn_change_email, 4, 0, 1, 3)

        self.lbl_new_email_ver = QLabel(self.email_reset_box)
        self.lbl_new_email_ver.setObjectName(u"lbl_new_email_ver")
        self.lbl_new_email_ver.setFont(font3)

        self.gridLayout_7.addWidget(self.lbl_new_email_ver, 3, 0, 1, 1)


        self.gridLayout_8.addWidget(self.email_reset_box, 3, 0, 1, 2)

        self.stacked_widget.addWidget(self.page)

        self.gridLayout_5.addWidget(self.stacked_widget, 1, 2, 1, 2)

        self.menu_widget = QWidget(self.widget)
        self.menu_widget.setObjectName(u"menu_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.menu_widget.sizePolicy().hasHeightForWidth())
        self.menu_widget.setSizePolicy(sizePolicy2)
        self.menu_widget.setMinimumSize(QSize(175, 0))
        self.menu_widget.setMaximumSize(QSize(175, 16777215))
        self.menu_widget.setStyleSheet(u"QToolButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgba(255, 255, 255, 20);\n"
"}\n"
"\n"
"QToolButton::hover{\n"
"	background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.menu_widget)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.lbl_settings_title = QLabel(self.menu_widget)
        self.lbl_settings_title.setObjectName(u"lbl_settings_title")
        font10 = QFont()
        font10.setFamilies([u"Nexa-Trial"])
        font10.setPointSize(21)
        font10.setBold(False)
        self.lbl_settings_title.setFont(font10)

        self.verticalLayout.addWidget(self.lbl_settings_title)

        self.btn_account = QToolButton(self.menu_widget)
        self.btn_account.setObjectName(u"btn_account")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_account.sizePolicy().hasHeightForWidth())
        self.btn_account.setSizePolicy(sizePolicy3)
        self.btn_account.setMinimumSize(QSize(155, 50))
        self.btn_account.setMaximumSize(QSize(206, 50))
        self.btn_account.setFont(font4)
        self.btn_account.setLayoutDirection(Qt.LeftToRight)
        self.btn_account.setStyleSheet(u"")
        self.btn_account.setCheckable(False)
        self.btn_account.setChecked(False)

        self.verticalLayout.addWidget(self.btn_account)

        self.btn_general = QToolButton(self.menu_widget)
        self.btn_general.setObjectName(u"btn_general")
        sizePolicy3.setHeightForWidth(self.btn_general.sizePolicy().hasHeightForWidth())
        self.btn_general.setSizePolicy(sizePolicy3)
        self.btn_general.setMinimumSize(QSize(155, 50))
        self.btn_general.setMaximumSize(QSize(206, 50))
        self.btn_general.setFont(font4)
        self.btn_general.setLayoutDirection(Qt.LeftToRight)
        self.btn_general.setStyleSheet(u"")
        self.btn_general.setCheckable(False)
        self.btn_general.setChecked(False)

        self.verticalLayout.addWidget(self.btn_general)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_5.addWidget(self.menu_widget, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.stacked_widget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_close.setText(QCoreApplication.translate("Form", u"X", None))
        self.lbl_curr_page.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_chg_email.setText(QCoreApplication.translate("Form", u"Change email address", None))
        self.btn_logout.setText(QCoreApplication.translate("Form", u"Logout...", None))
        self.btn_chg_pass.setText(QCoreApplication.translate("Form", u"Change Password...", None))
        self.lbl_chg_pass.setText(QCoreApplication.translate("Form", u"Change Master password", None))
        self.btn_chg_email.setText(QCoreApplication.translate("Form", u"Change Email...", None))
        self.lbl_user_email.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_user_name.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_user_name_pass_reset.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_user_email_pass_reset.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_old_pass.setText(QCoreApplication.translate("Form", u"Old Master password:", None))
        self.lbl_new_pass.setText(QCoreApplication.translate("Form", u"New Master password:", None))
        self.le_new_pass_ver.setPlaceholderText("")
        self.le_old_pass.setPlaceholderText("")
        self.le_new_pass.setPlaceholderText("")
        self.btn_change_pass.setText(QCoreApplication.translate("Form", u"Change Password...", None))
        self.lbl_new_pass_ver.setText(QCoreApplication.translate("Form", u"Verify new Master password:", None))
        self.btn_back_pass.setText(QCoreApplication.translate("Form", u"<", None))
        self.lbl_user_name_email_reset.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_user_email_email_reset.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.btn_back_email.setText(QCoreApplication.translate("Form", u"<", None))
        self.lbl_old_email.setText(QCoreApplication.translate("Form", u"Old Email address:", None))
        self.lbl_new_email.setText(QCoreApplication.translate("Form", u"New Email address:", None))
        self.le_new_email_ver.setPlaceholderText("")
        self.le_old_email.setPlaceholderText("")
        self.le_new_email.setPlaceholderText("")
        self.btn_change_email.setText(QCoreApplication.translate("Form", u"Change Email...", None))
        self.lbl_new_email_ver.setText(QCoreApplication.translate("Form", u"Verify new Email address:", None))
        self.lbl_settings_title.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.btn_account.setText(QCoreApplication.translate("Form", u"Account", None))
        self.btn_general.setText(QCoreApplication.translate("Form", u"General", None))
    # retranslateUi


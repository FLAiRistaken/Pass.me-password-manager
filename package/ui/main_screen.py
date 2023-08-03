# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_screen.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)
from icons import rc_icons

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(942, 622)
        Form.setStyleSheet(u"")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget#left_box{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, 		stop:0 rgba(0, 0, 0, 255), stop:1 rgba(92, 61, 88, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"QWidget#top_box{\n"
"	background-color: rgba(32, 32, 32, 255);\n"
"	border-top-right-radius: 10px\n"
"}\n"
"QWidget#middle_box{\n"
"	background-color: rgba(32, 32, 32, 255);\n"
"	border-color: rgb(0, 0, 0);\n"
"}\n"
"QWidget#right_box{\n"
"	background-color: rgba(32, 32, 32, 255);\n"
"	border-bottom-right-radius: 10px\n"
"}\n"
"QPushButton#btnNew{\n"
"	background-color:rgba(148, 105, 141, 255);\n"
"	color:rgba(255, 255, 255, 220);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#btnNew::hover{\n"
"	background-color:rgba(148, 105, 141, 200);\n"
"}\n"
"QListWidget{\n"
"	background-color: rgba(35, 35, 35, 220);\n"
"	border-radius:10px;\n"
"}\n"
"QToolButton#btnProfile{\n"
"	border:none;\n"
"	color:rgba(255, 255, 255, 220);\n"
"	border-radius:5px;\n"
"}\n"
"QToolButton#btnProfile:hover{\n"
"	background-color: rgba(152, 108, 144, 80"
                        ")\n"
"}")
        self.left_box = QWidget(self.widget)
        self.left_box.setObjectName(u"left_box")
        self.left_box.setGeometry(QRect(10, 0, 261, 621))
        self.left_box.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	color: rgba(255, 255, 255, 200);\n"
"	padding: 10px;\n"
"	text-align: left;\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(152, 108, 144, 115)\n"
"}\n"
"QToolButton{\n"
"	text-align:left;\n"
"	border-radius:6px;\n"
"	color: rgba(255, 255, 255, 220);\n"
"	padding: 10px;\n"
"}\n"
"QToolButton:hover{\n"
"	background-color: rgba(152, 108, 144, 115)\n"
"}\n"
"QToolButton#btnTags{\n"
"	border:none;\n"
"	color:rgba(255, 255, 255, 220);\n"
"	border-radius:5px;\n"
"}\n"
"QToolButton#btnTags:hover{\n"
"	background-color: rgba(152, 108, 144, 80);\n"
"}\n"
"QMenu{\n"
"	opacity: 50%;\n"
"}\n"
"QMenu::item{\n"
"	background-color: rgba(32, 32, 32, 100);\n"
"	border-radius: 4px;\n"
"	padding:6px;\n"
"	margin-top: 3px;\n"
"	margin-bottom: 2px;\n"
"	font-size: 16px;\n"
"	width: 200%\n"
"}\n"
"QMenu::item::selected{\n"
"	background-color: rgba(40, 40, 40, 100);\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.left_box)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnProfile = QToolButton(self.left_box)
        self.btnProfile.setObjectName(u"btnProfile")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnProfile.sizePolicy().hasHeightForWidth())
        self.btnProfile.setSizePolicy(sizePolicy)
        self.btnProfile.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"Nexa-Trial"])
        font.setPointSize(16)
        self.btnProfile.setFont(font)
        self.btnProfile.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnProfile.setLayoutDirection(Qt.LeftToRight)
        self.btnProfile.setStyleSheet(u"border-radius:6px;\n"
"color: rgba(255, 255, 255, 200);\n"
"padding: 10px;")
        self.btnProfile.setIconSize(QSize(9, 9))
        self.btnProfile.setPopupMode(QToolButton.InstantPopup)
        self.btnProfile.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.btnProfile.setAutoRaise(False)
        self.btnProfile.setArrowType(Qt.DownArrow)

        self.verticalLayout_2.addWidget(self.btnProfile)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.btnAll_Items = QPushButton(self.left_box)
        self.btnAll_Items.setObjectName(u"btnAll_Items")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnAll_Items.sizePolicy().hasHeightForWidth())
        self.btnAll_Items.setSizePolicy(sizePolicy1)
        self.btnAll_Items.setMinimumSize(QSize(0, 0))
        self.btnAll_Items.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamilies([u"Nexa-Trial"])
        font1.setPointSize(15)
        self.btnAll_Items.setFont(font1)
        self.btnAll_Items.setLayoutDirection(Qt.LeftToRight)
        self.btnAll_Items.setStyleSheet(u"")
        self.btnAll_Items.setCheckable(False)
        self.btnAll_Items.setChecked(False)

        self.verticalLayout_2.addWidget(self.btnAll_Items)

        self.btnFavorites = QPushButton(self.left_box)
        self.btnFavorites.setObjectName(u"btnFavorites")
        sizePolicy1.setHeightForWidth(self.btnFavorites.sizePolicy().hasHeightForWidth())
        self.btnFavorites.setSizePolicy(sizePolicy1)
        self.btnFavorites.setMinimumSize(QSize(0, 0))
        self.btnFavorites.setMaximumSize(QSize(16777215, 40))
        self.btnFavorites.setFont(font1)
        self.btnFavorites.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.btnFavorites)

        self.btnGenerator = QPushButton(self.left_box)
        self.btnGenerator.setObjectName(u"btnGenerator")
        sizePolicy1.setHeightForWidth(self.btnGenerator.sizePolicy().hasHeightForWidth())
        self.btnGenerator.setSizePolicy(sizePolicy1)
        self.btnGenerator.setMaximumSize(QSize(16777215, 40))
        self.btnGenerator.setFont(font1)
        self.btnGenerator.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.btnGenerator)

        self.line = QFrame(self.left_box)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setStyleSheet(u"background-color: rgba(255, 255, 255, 20);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.lbl_folders = QLabel(self.left_box)
        self.lbl_folders.setObjectName(u"lbl_folders")
        self.lbl_folders.setFont(font)
        self.lbl_folders.setStyleSheet(u"color: rgba(255, 255, 255, 200);")

        self.verticalLayout_2.addWidget(self.lbl_folders)

        self.btn_business = QPushButton(self.left_box)
        self.btn_business.setObjectName(u"btn_business")
        sizePolicy1.setHeightForWidth(self.btn_business.sizePolicy().hasHeightForWidth())
        self.btn_business.setSizePolicy(sizePolicy1)
        self.btn_business.setMaximumSize(QSize(16777215, 32))
        font2 = QFont()
        font2.setFamilies([u"Nexa-Trial"])
        font2.setPointSize(14)
        self.btn_business.setFont(font2)
        self.btn_business.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.btn_business)

        self.btn_email = QPushButton(self.left_box)
        self.btn_email.setObjectName(u"btn_email")
        sizePolicy1.setHeightForWidth(self.btn_email.sizePolicy().hasHeightForWidth())
        self.btn_email.setSizePolicy(sizePolicy1)
        self.btn_email.setMaximumSize(QSize(16777215, 32))
        self.btn_email.setFont(font2)
        self.btn_email.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.btn_email)

        self.btn_entertainment = QPushButton(self.left_box)
        self.btn_entertainment.setObjectName(u"btn_entertainment")
        sizePolicy1.setHeightForWidth(self.btn_entertainment.sizePolicy().hasHeightForWidth())
        self.btn_entertainment.setSizePolicy(sizePolicy1)
        self.btn_entertainment.setMaximumSize(QSize(16777215, 32))
        self.btn_entertainment.setFont(font2)
        self.btn_entertainment.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.btn_entertainment)

        self.btn_education = QPushButton(self.left_box)
        self.btn_education.setObjectName(u"btn_education")
        sizePolicy1.setHeightForWidth(self.btn_education.sizePolicy().hasHeightForWidth())
        self.btn_education.setSizePolicy(sizePolicy1)
        self.btn_education.setMaximumSize(QSize(16777215, 32))
        self.btn_education.setFont(font2)
        self.btn_education.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.btn_education)

        self.btn_finance = QPushButton(self.left_box)
        self.btn_finance.setObjectName(u"btn_finance")
        sizePolicy1.setHeightForWidth(self.btn_finance.sizePolicy().hasHeightForWidth())
        self.btn_finance.setSizePolicy(sizePolicy1)
        self.btn_finance.setMaximumSize(QSize(16777215, 32))
        self.btn_finance.setFont(font2)
        self.btn_finance.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.btn_finance)

        self.btn_games = QPushButton(self.left_box)
        self.btn_games.setObjectName(u"btn_games")
        sizePolicy1.setHeightForWidth(self.btn_games.sizePolicy().hasHeightForWidth())
        self.btn_games.setSizePolicy(sizePolicy1)
        self.btn_games.setMaximumSize(QSize(16777215, 32))
        self.btn_games.setFont(font2)
        self.btn_games.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.btn_games)

        self.btn_social = QPushButton(self.left_box)
        self.btn_social.setObjectName(u"btn_social")
        sizePolicy1.setHeightForWidth(self.btn_social.sizePolicy().hasHeightForWidth())
        self.btn_social.setSizePolicy(sizePolicy1)
        self.btn_social.setMaximumSize(QSize(16777215, 32))
        self.btn_social.setFont(font2)
        self.btn_social.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.btn_social)

        self.line_3 = QFrame(self.left_box)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMaximumSize(QSize(16777215, 1))
        self.line_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 20);")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.btnRecently_Deleted = QPushButton(self.left_box)
        self.btnRecently_Deleted.setObjectName(u"btnRecently_Deleted")
        sizePolicy1.setHeightForWidth(self.btnRecently_Deleted.sizePolicy().hasHeightForWidth())
        self.btnRecently_Deleted.setSizePolicy(sizePolicy1)
        self.btnRecently_Deleted.setMinimumSize(QSize(0, 0))
        self.btnRecently_Deleted.setMaximumSize(QSize(16777215, 40))
        self.btnRecently_Deleted.setFont(font1)
        self.btnRecently_Deleted.setLayoutDirection(Qt.LeftToRight)
        self.btnRecently_Deleted.setStyleSheet(u"")
        self.btnRecently_Deleted.setCheckable(False)
        self.btnRecently_Deleted.setChecked(False)

        self.verticalLayout_2.addWidget(self.btnRecently_Deleted)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.gridLayoutWidget = QWidget(self.widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(270, 20, 671, 581))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.right_box = QWidget(self.gridLayoutWidget)
        self.right_box.setObjectName(u"right_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.right_box.sizePolicy().hasHeightForWidth())
        self.right_box.setSizePolicy(sizePolicy2)
        self.right_box.setMinimumSize(QSize(300, 0))
        self.right_box.setSizeIncrement(QSize(0, 0))
        self.right_box.setBaseSize(QSize(400, 0))
        self.right_box.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.right_box)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.wItemBox = QWidget(self.right_box)
        self.wItemBox.setObjectName(u"wItemBox")
        self.wItemBox.setMinimumSize(QSize(0, 0))
        self.wItemBox.setBaseSize(QSize(0, 0))
        self.wItemBox.setStyleSheet(u"background-color: rgba(35, 35, 35, 220);")

        self.gridLayout_2.addWidget(self.wItemBox, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.right_box, 1, 1, 1, 1)

        self.middle_box = QWidget(self.gridLayoutWidget)
        self.middle_box.setObjectName(u"middle_box")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.middle_box.sizePolicy().hasHeightForWidth())
        self.middle_box.setSizePolicy(sizePolicy3)
        self.middle_box.setMinimumSize(QSize(150, 0))
        self.middle_box.setMaximumSize(QSize(400, 16777215))
        self.middle_box.setBaseSize(QSize(150, 0))
        self.middle_box.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.middle_box)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.comboCategories = QComboBox(self.middle_box)
        self.comboCategories.addItem("")
        self.comboCategories.addItem("")
        self.comboCategories.addItem("")
        self.comboCategories.addItem("")
        self.comboCategories.addItem("")
        self.comboCategories.addItem("")
        self.comboCategories.setObjectName(u"comboCategories")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.comboCategories.sizePolicy().hasHeightForWidth())
        self.comboCategories.setSizePolicy(sizePolicy4)
        self.comboCategories.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setFamilies([u"Nexa-Trial"])
        self.comboCategories.setFont(font3)
        self.comboCategories.setStyleSheet(u"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:6px;\n"
"color: rgba(255, 255, 255, 200);")

        self.verticalLayout_3.addWidget(self.comboCategories)

        self.lvItems = QListWidget(self.middle_box)
        self.lvItems.setObjectName(u"lvItems")
        self.lvItems.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.lvItems)


        self.gridLayout_4.addWidget(self.middle_box, 1, 0, 1, 1)

        self.top_box = QWidget(self.gridLayoutWidget)
        self.top_box.setObjectName(u"top_box")
        self.top_box.setMaximumSize(QSize(16777215, 50))
        self.top_box.setStyleSheet(u"\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.horizontalLayout = QHBoxLayout(self.top_box)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnNew = QPushButton(self.top_box)
        self.btnNew.setObjectName(u"btnNew")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btnNew.sizePolicy().hasHeightForWidth())
        self.btnNew.setSizePolicy(sizePolicy5)
        self.btnNew.setMaximumSize(QSize(65, 25))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(15)
        self.btnNew.setFont(font4)
        self.btnNew.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btnNew)

        self.line_2 = QFrame(self.top_box)
        self.line_2.setObjectName(u"line_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy6)
        self.line_2.setMaximumSize(QSize(16777215, 25))
        self.line_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.hSearch = QHBoxLayout()
        self.hSearch.setSpacing(0)
        self.hSearch.setObjectName(u"hSearch")
        self.widget_2 = QWidget(self.top_box)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMaximumSize(QSize(26, 27))
        self.widget_2.setStyleSheet(u"\n"
"background-color: rgb(23, 23, 23);\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"")
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(10, 10))
        self.label.setMaximumSize(QSize(15, 15))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label.setPixmap(QPixmap(u":/search_icon/search_icon.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label.setMargin(0)
        self.label.setIndent(-1)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)


        self.hSearch.addWidget(self.widget_2)

        self.lineEdit_Search = QLineEdit(self.top_box)
        self.lineEdit_Search.setObjectName(u"lineEdit_Search")
        self.lineEdit_Search.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_Search.sizePolicy().hasHeightForWidth())
        self.lineEdit_Search.setSizePolicy(sizePolicy)
        self.lineEdit_Search.setMaximumSize(QSize(100000, 27))
        self.lineEdit_Search.setStyleSheet(u"border-bottom-right-radius: 6px;\n"
"border-top-right-radius: 6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px")
        self.lineEdit_Search.setFrame(False)
        self.lineEdit_Search.setClearButtonEnabled(True)

        self.hSearch.addWidget(self.lineEdit_Search)


        self.horizontalLayout.addLayout(self.hSearch)


        self.gridLayout_4.addWidget(self.top_box, 0, 0, 1, 2)

        self.gridLayoutWidget.raise_()
        self.left_box.raise_()

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Form)
        self.btnProfile.clicked.connect(self.btnProfile.showMenu)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btnProfile.setText(QCoreApplication.translate("Form", u"    account", None))
        self.btnAll_Items.setText(QCoreApplication.translate("Form", u"all items", None))
        self.btnFavorites.setText(QCoreApplication.translate("Form", u"favorites", None))
        self.btnGenerator.setText(QCoreApplication.translate("Form", u"generator", None))
        self.lbl_folders.setText(QCoreApplication.translate("Form", u"folders", None))
        self.btn_business.setText(QCoreApplication.translate("Form", u"Business", None))
        self.btn_email.setText(QCoreApplication.translate("Form", u"Email", None))
        self.btn_entertainment.setText(QCoreApplication.translate("Form", u"Entertainment", None))
        self.btn_education.setText(QCoreApplication.translate("Form", u"Education", None))
        self.btn_finance.setText(QCoreApplication.translate("Form", u"Finance", None))
        self.btn_games.setText(QCoreApplication.translate("Form", u"Games", None))
        self.btn_social.setText(QCoreApplication.translate("Form", u"Social", None))
        self.btnRecently_Deleted.setText(QCoreApplication.translate("Form", u"recently deleted", None))
        self.comboCategories.setItemText(0, QCoreApplication.translate("Form", u"All Categories", None))
        self.comboCategories.setItemText(1, QCoreApplication.translate("Form", u"Logins", None))
        self.comboCategories.setItemText(2, QCoreApplication.translate("Form", u"Identities", None))
        self.comboCategories.setItemText(3, QCoreApplication.translate("Form", u"Bank cards", None))
        self.comboCategories.setItemText(4, QCoreApplication.translate("Form", u"Bank accounts", None))
        self.comboCategories.setItemText(5, QCoreApplication.translate("Form", u"Secure notes", None))

        self.btnNew.setText(QCoreApplication.translate("Form", u"+  New", None))
        self.label.setText("")
        self.lineEdit_Search.setInputMask("")
        self.lineEdit_Search.setText("")
        self.lineEdit_Search.setPlaceholderText(QCoreApplication.translate("Form", u"search", None))
    # retranslateUi


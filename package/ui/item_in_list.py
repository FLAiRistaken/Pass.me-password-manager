# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_in_list.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(240, 82)
        Form.setMaximumSize(QSize(250, 82))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 4, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(8, 12, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.lbl_Item_Name = QLabel(self.widget)
        self.lbl_Item_Name.setObjectName(u"lbl_Item_Name")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.lbl_Item_Name.setFont(font)
        self.lbl_Item_Name.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")

        self.gridLayout_2.addWidget(self.lbl_Item_Name, 1, 2, 1, 1)

        self.lbl_Item_Icon = QLabel(self.widget)
        self.lbl_Item_Icon.setObjectName(u"lbl_Item_Icon")
        self.lbl_Item_Icon.setMaximumSize(QSize(50, 50))
        self.lbl_Item_Icon.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(30, 30, 30);")

        self.gridLayout_2.addWidget(self.lbl_Item_Icon, 0, 1, 4, 1)

        self.lbl_Item_Details = QLabel(self.widget)
        self.lbl_Item_Details.setObjectName(u"lbl_Item_Details")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.lbl_Item_Details.setFont(font1)
        self.lbl_Item_Details.setStyleSheet(u"color: rgba(255, 255, 255, 200);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.gridLayout_2.addWidget(self.lbl_Item_Details, 2, 2, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_Item_Name.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_Item_Icon.setText("")
        self.lbl_Item_Details.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi


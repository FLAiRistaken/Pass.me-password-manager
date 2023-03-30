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

class Ui_Item_In_List(object):
    def setupUi(self, Item_In_List):
        if not Item_In_List.objectName():
            Item_In_List.setObjectName(u"Item_In_List")
        Item_In_List.resize(200, 75)
        Item_In_List.setMaximumSize(QSize(200, 75))
        Item_In_List.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(30, 30, 30);")
        self.gridLayout = QGridLayout(Item_In_List)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_Item_Icon = QLabel(Item_In_List)
        self.lbl_Item_Icon.setObjectName(u"lbl_Item_Icon")
        self.lbl_Item_Icon.setMaximumSize(QSize(50, 50))

        self.gridLayout.addWidget(self.lbl_Item_Icon, 0, 1, 4, 1)

        self.lbl_Item_Name = QLabel(Item_In_List)
        self.lbl_Item_Name.setObjectName(u"lbl_Item_Name")
        font = QFont()
        font.setBold(True)
        self.lbl_Item_Name.setFont(font)

        self.gridLayout.addWidget(self.lbl_Item_Name, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.lbl_Item_Details = QLabel(Item_In_List)
        self.lbl_Item_Details.setObjectName(u"lbl_Item_Details")
        font1 = QFont()
        font1.setPointSize(11)
        self.lbl_Item_Details.setFont(font1)
        self.lbl_Item_Details.setStyleSheet(u"color: rgba(255, 255, 255, 200);")

        self.gridLayout.addWidget(self.lbl_Item_Details, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(8, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.retranslateUi(Item_In_List)

        QMetaObject.connectSlotsByName(Item_In_List)
    # setupUi

    def retranslateUi(self, Item_In_List):
        Item_In_List.setWindowTitle(QCoreApplication.translate("Item_In_List", u"Form", None))
        self.lbl_Item_Icon.setText("")
        self.lbl_Item_Name.setText(QCoreApplication.translate("Item_In_List", u"TextLabel", None))
        self.lbl_Item_Details.setText(QCoreApplication.translate("Item_In_List", u"TextLabel", None))
    # retranslateUi


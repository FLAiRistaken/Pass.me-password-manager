# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pass_hist_list_item.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(218, 70)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QSize(218, 70))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_gen_date = QLabel(Form)
        self.lbl_gen_date.setObjectName(u"lbl_gen_date")
        font = QFont()
        font.setPointSize(11)
        self.lbl_gen_date.setFont(font)
        self.lbl_gen_date.setStyleSheet(u"color: rgba(255, 255, 255, 200);")

        self.gridLayout.addWidget(self.lbl_gen_date, 1, 0, 1, 1)

        self.lbl_password = QLabel(Form)
        self.lbl_password.setObjectName(u"lbl_password")
        font1 = QFont()
        font1.setBold(True)
        self.lbl_password.setFont(font1)

        self.gridLayout.addWidget(self.lbl_password, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_gen_date.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_password.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi


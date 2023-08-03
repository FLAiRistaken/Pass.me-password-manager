# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_msg_box.ui'
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
        Form.resize(223, 83)
        Form.setStyleSheet(u"QWidget#wid_msg_box {\n"
"	background-color: rgba(23, 23, 23, 225);\n"
"	border-radius: 5px;\n"
"}")
        self.wid_msg_box = QWidget(Form)
        self.wid_msg_box.setObjectName(u"wid_msg_box")
        self.wid_msg_box.setGeometry(QRect(0, 0, 221, 81))
        self.gridLayout = QGridLayout(self.wid_msg_box)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_msg = QLabel(self.wid_msg_box)
        self.lbl_msg.setObjectName(u"lbl_msg")
        self.lbl_msg.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_msg, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_msg.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi


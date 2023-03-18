# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_password_options.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QSizePolicy, QSlider, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(509, 280)
        Form.setStyleSheet(u"QWidget#widget_password {\n"
"	background-color: rgb(23, 23, 23);\n"
"	border-radius: 5px;\n"
"}")
        self.widget_password = QWidget(Form)
        self.widget_password.setObjectName(u"widget_password")
        self.widget_password.setGeometry(QRect(0, 0, 499, 270))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_password.sizePolicy().hasHeightForWidth())
        self.widget_password.setSizePolicy(sizePolicy)
        self.widget_password.setStyleSheet(u"padding: 10px;")
        self.gridLayout = QGridLayout(self.widget_password)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_capitals = QLabel(self.widget_password)
        self.lbl_capitals.setObjectName(u"lbl_capitals")
        font = QFont()
        font.setFamilies([u"Nexa-Trial"])
        self.lbl_capitals.setFont(font)

        self.gridLayout.addWidget(self.lbl_capitals, 3, 0, 1, 1)

        self.lbl_length = QLabel(self.widget_password)
        self.lbl_length.setObjectName(u"lbl_length")
        self.lbl_length.setFont(font)

        self.gridLayout.addWidget(self.lbl_length, 0, 0, 1, 1)

        self.slide_len = QSlider(self.widget_password)
        self.slide_len.setObjectName(u"slide_len")
        self.slide_len.setMaximumSize(QSize(175, 16777215))
        self.slide_len.setStyleSheet(u"")
        self.slide_len.setMinimum(8)
        self.slide_len.setMaximum(64)
        self.slide_len.setOrientation(Qt.Horizontal)
        self.slide_len.setTickPosition(QSlider.TicksAbove)

        self.gridLayout.addWidget(self.slide_len, 0, 2, 1, 1)

        self.chk_nums = QCheckBox(self.widget_password)
        self.chk_nums.setObjectName(u"chk_nums")

        self.gridLayout.addWidget(self.chk_nums, 1, 2, 1, 1, Qt.AlignRight)

        self.lbl_numbers = QLabel(self.widget_password)
        self.lbl_numbers.setObjectName(u"lbl_numbers")
        self.lbl_numbers.setFont(font)

        self.gridLayout.addWidget(self.lbl_numbers, 1, 0, 1, 1)

        self.lbl_len_no = QLabel(self.widget_password)
        self.lbl_len_no.setObjectName(u"lbl_len_no")
        self.lbl_len_no.setFont(font)

        self.gridLayout.addWidget(self.lbl_len_no, 0, 1, 1, 1)

        self.chk_spec = QCheckBox(self.widget_password)
        self.chk_spec.setObjectName(u"chk_spec")

        self.gridLayout.addWidget(self.chk_spec, 2, 2, 1, 1, Qt.AlignRight)

        self.lbl_spec = QLabel(self.widget_password)
        self.lbl_spec.setObjectName(u"lbl_spec")
        self.lbl_spec.setFont(font)

        self.gridLayout.addWidget(self.lbl_spec, 2, 0, 1, 1)

        self.chk_capitals = QCheckBox(self.widget_password)
        self.chk_capitals.setObjectName(u"chk_capitals")

        self.gridLayout.addWidget(self.chk_capitals, 3, 2, 1, 1, Qt.AlignRight)

#if QT_CONFIG(shortcut)
        self.lbl_capitals.setBuddy(self.chk_capitals)
        self.lbl_length.setBuddy(self.slide_len)
        self.lbl_numbers.setBuddy(self.chk_nums)
        self.lbl_len_no.setBuddy(self.slide_len)
        self.lbl_spec.setBuddy(self.chk_spec)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)
        self.slide_len.sliderMoved.connect(self.lbl_len_no.setNum)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_capitals.setText(QCoreApplication.translate("Form", u"Capitals", None))
        self.lbl_length.setText(QCoreApplication.translate("Form", u"Length", None))
        self.chk_nums.setText("")
        self.lbl_numbers.setText(QCoreApplication.translate("Form", u"Numbers", None))
        self.lbl_len_no.setText(QCoreApplication.translate("Form", u"8", None))
        self.chk_spec.setText("")
        self.lbl_spec.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Special Characters</p><p>(<span style=\" font-family:'Consolas','monospace'; font-size:12pt; color:#ffffff;\">!#$%&amp;()*+, -.:;&lt;=&gt;?[]^_`{|}~</span>)</p></body></html>", None))
        self.chk_capitals.setText("")
    # retranslateUi


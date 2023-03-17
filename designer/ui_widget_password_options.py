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
        Form.resize(508, 256)
        Form.setStyleSheet(u"QWidget#widget_password {\n"
"	background-color: rgb(23, 23, 23);\n"
"	border-radius: 5px;\n"
"}")
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_password = QWidget(Form)
        self.widget_password.setObjectName(u"widget_password")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_password.sizePolicy().hasHeightForWidth())
        self.widget_password.setSizePolicy(sizePolicy)
        self.widget_password.setStyleSheet(u"padding: 10px;")
        self.gridLayout = QGridLayout(self.widget_password)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.widget_password)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Nexa-Trial"])
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.lbl_length = QLabel(self.widget_password)
        self.lbl_length.setObjectName(u"lbl_length")
        self.lbl_length.setFont(font)

        self.gridLayout.addWidget(self.lbl_length, 0, 0, 1, 1)

        self.horizontalSlider = QSlider(self.widget_password)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximumSize(QSize(175, 16777215))
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setMinimum(8)
        self.horizontalSlider.setMaximum(64)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QSlider.TicksAbove)

        self.gridLayout.addWidget(self.horizontalSlider, 0, 2, 1, 1)

        self.checkBox = QCheckBox(self.widget_password)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 1, 2, 1, 1, Qt.AlignRight)

        self.lbl_numbers = QLabel(self.widget_password)
        self.lbl_numbers.setObjectName(u"lbl_numbers")
        self.lbl_numbers.setFont(font)

        self.gridLayout.addWidget(self.lbl_numbers, 1, 0, 1, 1)

        self.lbl_len_no = QLabel(self.widget_password)
        self.lbl_len_no.setObjectName(u"lbl_len_no")
        self.lbl_len_no.setFont(font)

        self.gridLayout.addWidget(self.lbl_len_no, 0, 1, 1, 1)

        self.checkBox_2 = QCheckBox(self.widget_password)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 2, 2, 1, 1, Qt.AlignRight)

        self.label_2 = QLabel(self.widget_password)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.widget_password)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout.addWidget(self.checkBox_3, 3, 2, 1, 1, Qt.AlignRight)


        self.gridLayout_2.addWidget(self.widget_password, 1, 0, 1, 1)

#if QT_CONFIG(shortcut)
        self.label_3.setBuddy(self.checkBox_3)
        self.lbl_length.setBuddy(self.horizontalSlider)
        self.lbl_numbers.setBuddy(self.checkBox)
        self.lbl_len_no.setBuddy(self.horizontalSlider)
        self.label_2.setBuddy(self.checkBox_2)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)
        self.horizontalSlider.sliderMoved.connect(self.lbl_len_no.setNum)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Capitals", None))
        self.lbl_length.setText(QCoreApplication.translate("Form", u"Length", None))
        self.checkBox.setText("")
        self.lbl_numbers.setText(QCoreApplication.translate("Form", u"Numbers", None))
        self.lbl_len_no.setText(QCoreApplication.translate("Form", u"8", None))
        self.checkBox_2.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Special Characters</p><p>(<span style=\" font-family:'Consolas','monospace'; font-size:12pt; color:#ffffff;\">!#$%&amp;()*+, -.:;&lt;=&gt;?[]^_`{|}~</span>)</p></body></html>", None))
        self.checkBox_3.setText("")
    # retranslateUi


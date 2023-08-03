# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_passphrase_options.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QLabel, QSizePolicy, QSlider, QWidget)
from icons import rc_search_icon

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(502, 272)
        Form.setStyleSheet(u"QWidget#widget_passphrase{\n"
"	background-color: rgb(23, 23, 23);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	border: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/down_arrow/down-arrow.png);\n"
"	width: 14px;\n"
"	height: 14px;\n"
"	padding-right: 2px;\n"
"}")
        self.widget_passphrase = QWidget(Form)
        self.widget_passphrase.setObjectName(u"widget_passphrase")
        self.widget_passphrase.setGeometry(QRect(0, 0, 499, 270))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_passphrase.sizePolicy().hasHeightForWidth())
        self.widget_passphrase.setSizePolicy(sizePolicy)
        self.widget_passphrase.setStyleSheet(u"padding: 10px;")
        self.gridLayout = QGridLayout(self.widget_passphrase)
        self.gridLayout.setObjectName(u"gridLayout")
        self.chk_num = QCheckBox(self.widget_passphrase)
        self.chk_num.setObjectName(u"chk_num")

        self.gridLayout.addWidget(self.chk_num, 2, 2, 1, 1, Qt.AlignRight)

        self.chk_capitalise = QCheckBox(self.widget_passphrase)
        self.chk_capitalise.setObjectName(u"chk_capitalise")

        self.gridLayout.addWidget(self.chk_capitalise, 3, 2, 1, 1, Qt.AlignRight)

        self.lbl_separator = QLabel(self.widget_passphrase)
        self.lbl_separator.setObjectName(u"lbl_separator")
        font = QFont()
        font.setFamilies([u"Nexa-Trial"])
        self.lbl_separator.setFont(font)

        self.gridLayout.addWidget(self.lbl_separator, 1, 0, 1, 1)

        self.slide_word_no = QSlider(self.widget_passphrase)
        self.slide_word_no.setObjectName(u"slide_word_no")
        self.slide_word_no.setMaximumSize(QSize(175, 16777215))
        self.slide_word_no.setStyleSheet(u"")
        self.slide_word_no.setMinimum(3)
        self.slide_word_no.setMaximum(20)
        self.slide_word_no.setValue(3)
        self.slide_word_no.setOrientation(Qt.Horizontal)
        self.slide_word_no.setTickPosition(QSlider.TicksAbove)
        self.slide_word_no.setTickInterval(2)

        self.gridLayout.addWidget(self.slide_word_no, 0, 2, 1, 1)

        self.lbl_inc_number = QLabel(self.widget_passphrase)
        self.lbl_inc_number.setObjectName(u"lbl_inc_number")
        self.lbl_inc_number.setFont(font)

        self.gridLayout.addWidget(self.lbl_inc_number, 2, 0, 1, 1)

        self.lbl_words = QLabel(self.widget_passphrase)
        self.lbl_words.setObjectName(u"lbl_words")
        self.lbl_words.setFont(font)

        self.gridLayout.addWidget(self.lbl_words, 0, 0, 1, 1)

        self.lbl_capitalise = QLabel(self.widget_passphrase)
        self.lbl_capitalise.setObjectName(u"lbl_capitalise")
        self.lbl_capitalise.setFont(font)

        self.gridLayout.addWidget(self.lbl_capitalise, 3, 0, 1, 1)

        self.lbl_word_no = QLabel(self.widget_passphrase)
        self.lbl_word_no.setObjectName(u"lbl_word_no")
        self.lbl_word_no.setFont(font)

        self.gridLayout.addWidget(self.lbl_word_no, 0, 1, 1, 1)

        self.combo_separator = QComboBox(self.widget_passphrase)
        self.combo_separator.addItem("")
        self.combo_separator.addItem("")
        self.combo_separator.addItem("")
        self.combo_separator.addItem("")
        self.combo_separator.setObjectName(u"combo_separator")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.combo_separator.sizePolicy().hasHeightForWidth())
        self.combo_separator.setSizePolicy(sizePolicy1)
        self.combo_separator.setMaximumSize(QSize(16777215, 30))
        self.combo_separator.setFont(font)
        self.combo_separator.setStyleSheet(u"border-radius:6px;\n"
"padding-bottom:8px;\n"
"padding-left:6px;\n"
"color: rgba(255, 255, 255, 200);\n"
"background-color: rgb(20,20,20);")
        self.combo_separator.setMaxVisibleItems(5)
        self.combo_separator.setFrame(True)

        self.gridLayout.addWidget(self.combo_separator, 1, 2, 1, 1)

#if QT_CONFIG(shortcut)
        self.lbl_separator.setBuddy(self.combo_separator)
        self.lbl_inc_number.setBuddy(self.chk_num)
        self.lbl_words.setBuddy(self.slide_word_no)
        self.lbl_capitalise.setBuddy(self.chk_capitalise)
        self.lbl_word_no.setBuddy(self.slide_word_no)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.slide_word_no, self.combo_separator)
        QWidget.setTabOrder(self.combo_separator, self.chk_num)
        QWidget.setTabOrder(self.chk_num, self.chk_capitalise)

        self.retranslateUi(Form)
        self.slide_word_no.sliderMoved.connect(self.lbl_word_no.setNum)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.chk_num.setText("")
        self.chk_capitalise.setText("")
        self.lbl_separator.setText(QCoreApplication.translate("Form", u"Word separator", None))
        self.lbl_inc_number.setText(QCoreApplication.translate("Form", u"Include number", None))
        self.lbl_words.setText(QCoreApplication.translate("Form", u"Number of words", None))
        self.lbl_capitalise.setText(QCoreApplication.translate("Form", u"Capitalise", None))
        self.lbl_word_no.setText(QCoreApplication.translate("Form", u"3", None))
        self.combo_separator.setItemText(0, QCoreApplication.translate("Form", u"-", None))
        self.combo_separator.setItemText(1, QCoreApplication.translate("Form", u".", None))
        self.combo_separator.setItemText(2, QCoreApplication.translate("Form", u",", None))
        self.combo_separator.setItemText(3, QCoreApplication.translate("Form", u"!", None))

    # retranslateUi


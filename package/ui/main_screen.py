

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
                               QHBoxLayout, QLineEdit, QPushButton,
                               QSizePolicy, QToolButton, QVBoxLayout, QWidget)


class Ui_Main(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(978, 664)
        Form.setStyleSheet(u"")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget#left_box{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, 		stop:0 rgba(0, 0, 0, 255), stop:1 rgba(92, 61, 88, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton#pushButton5 QMenu{\n"
"    height: 1px;\n"
"    border-bottom: 1px solid lightGray;\n"
"    background: #5A5A5A;\n"
"    margin-left: 2px;\n"
"    margin-right: 0px;\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"}")
        self.left_box = QWidget(self.widget)
        self.left_box.setObjectName(u"left_box")
        self.left_box.setGeometry(QRect(10, 0, 261, 621))
        self.left_box.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.left_box)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.toolButton = QToolButton(self.left_box)
        self.toolButton.setObjectName(u"toolButton")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.toolButton)

        self.pushButton_2 = QPushButton(self.left_box)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.left_box)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.left_box)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.line = QFrame(self.left_box)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.pushButton_5 = QPushButton(self.left_box)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton QMenu{\n"
"    height: 1px;\n"
"    border-bottom: 1px solid lightGray;\n"
"    background: #5A5A5A;\n"
"    margin-left: 2px;\n"
"    margin-right: 0px;\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.middle_box = QWidget(self.widget)
        self.middle_box.setObjectName(u"middle_box")
        self.middle_box.setGeometry(QRect(270, 70, 281, 531))
        self.middle_box.setStyleSheet(u"background-color: rgb(53, 134, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.verticalLayout_3 = QVBoxLayout(self.middle_box)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.comboBox = QComboBox(self.middle_box)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_3.addWidget(self.comboBox)

        self.right_box = QWidget(self.widget)
        self.right_box.setObjectName(u"right_box")
        self.right_box.setGeometry(QRect(550, 70, 391, 531))
        self.right_box.setStyleSheet(u"background-color: rgb(246, 65, 41);\n"
"border-bottom-right-radius: 10px")
        self.top_box = QWidget(self.widget)
        self.top_box.setObjectName(u"top_box")
        self.top_box.setGeometry(QRect(270, 20, 671, 51))
        self.top_box.setStyleSheet(u"background-color: rgb(0, 176, 80);\n"
"border-top-right-radius: 10px")
        self.horizontalLayout = QHBoxLayout(self.top_box)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.top_box)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.lineEdit = QLineEdit(self.top_box)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.middle_box.raise_()
        self.right_box.raise_()
        self.top_box.raise_()
        self.left_box.raise_()

        self.gridLayout.addWidget(self.widget, 0, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.toolButton.setText(QCoreApplication.translate("Form", u"...", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"+ New", None))
    # retranslateUi


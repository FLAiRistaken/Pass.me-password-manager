/********************************************************************************
** Form generated from reading UI file 'main_screen.ui'
**
** Created by: Qt User Interface Compiler version 6.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAIN_SCREEN_H
#define UI_MAIN_SCREEN_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListView>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Form
{
public:
    QGridLayout *gridLayout;
    QWidget *widget;
    QWidget *left_box;
    QVBoxLayout *verticalLayout_2;
    QToolButton *toolButton;
    QPushButton *pushButton_2;
    QPushButton *pushButton_3;
    QPushButton *pushButton_4;
    QFrame *line;
    QPushButton *pushButton_5;
    QWidget *middle_box;
    QVBoxLayout *verticalLayout_3;
    QComboBox *comboBox;
    QListView *listView;
    QWidget *right_box;
    QGridLayout *gridLayout_2;
    QWidget *widget_2;
    QWidget *top_box;
    QHBoxLayout *horizontalLayout;
    QPushButton *btnNew;
    QFrame *line_2;
    QLineEdit *lineEdit;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName("Form");
        Form->resize(978, 664);
        Form->setStyleSheet(QString::fromUtf8(""));
        gridLayout = new QGridLayout(Form);
        gridLayout->setObjectName("gridLayout");
        widget = new QWidget(Form);
        widget->setObjectName("widget");
        widget->setStyleSheet(QString::fromUtf8("QWidget#left_box{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, 		stop:0 rgba(0, 0, 0, 255), stop:1 rgba(92, 61, 88, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton#btnNew{\n"
"	background-color:rgba(148, 105, 141, 255);\n"
"	color:rgba(255, 255, 255, 220);\n"
"	border-radius:5px;\n"
"}"));
        left_box = new QWidget(widget);
        left_box->setObjectName("left_box");
        left_box->setGeometry(QRect(10, 0, 261, 621));
        left_box->setStyleSheet(QString::fromUtf8(""));
        verticalLayout_2 = new QVBoxLayout(left_box);
        verticalLayout_2->setObjectName("verticalLayout_2");
        toolButton = new QToolButton(left_box);
        toolButton->setObjectName("toolButton");
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(toolButton->sizePolicy().hasHeightForWidth());
        toolButton->setSizePolicy(sizePolicy);
        toolButton->setStyleSheet(QString::fromUtf8("border-radius:10px"));

        verticalLayout_2->addWidget(toolButton);

        pushButton_2 = new QPushButton(left_box);
        pushButton_2->setObjectName("pushButton_2");

        verticalLayout_2->addWidget(pushButton_2);

        pushButton_3 = new QPushButton(left_box);
        pushButton_3->setObjectName("pushButton_3");

        verticalLayout_2->addWidget(pushButton_3);

        pushButton_4 = new QPushButton(left_box);
        pushButton_4->setObjectName("pushButton_4");

        verticalLayout_2->addWidget(pushButton_4);

        line = new QFrame(left_box);
        line->setObjectName("line");
        line->setFrameShape(QFrame::HLine);
        line->setFrameShadow(QFrame::Sunken);

        verticalLayout_2->addWidget(line);

        pushButton_5 = new QPushButton(left_box);
        pushButton_5->setObjectName("pushButton_5");
        pushButton_5->setStyleSheet(QString::fromUtf8("QPushButton QMenu{\n"
"    height: 1px;\n"
"    border-bottom: 1px solid lightGray;\n"
"    background: #5A5A5A;\n"
"    margin-left: 2px;\n"
"    margin-right: 0px;\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"}"));

        verticalLayout_2->addWidget(pushButton_5);

        middle_box = new QWidget(widget);
        middle_box->setObjectName("middle_box");
        middle_box->setGeometry(QRect(270, 70, 281, 531));
        middle_box->setStyleSheet(QString::fromUtf8("background-color: rgb(53, 134, 255);\n"
"border-color: rgb(0, 0, 0);"));
        verticalLayout_3 = new QVBoxLayout(middle_box);
        verticalLayout_3->setObjectName("verticalLayout_3");
        comboBox = new QComboBox(middle_box);
        comboBox->setObjectName("comboBox");
        comboBox->setStyleSheet(QString::fromUtf8("border-radius:10px;"));

        verticalLayout_3->addWidget(comboBox);

        listView = new QListView(middle_box);
        listView->setObjectName("listView");
        listView->setStyleSheet(QString::fromUtf8("border-radius:10px;"));

        verticalLayout_3->addWidget(listView);

        right_box = new QWidget(widget);
        right_box->setObjectName("right_box");
        right_box->setGeometry(QRect(550, 70, 391, 531));
        right_box->setStyleSheet(QString::fromUtf8("background-color: rgb(246, 65, 41);\n"
"border-bottom-right-radius: 10px"));
        gridLayout_2 = new QGridLayout(right_box);
        gridLayout_2->setObjectName("gridLayout_2");
        widget_2 = new QWidget(right_box);
        widget_2->setObjectName("widget_2");

        gridLayout_2->addWidget(widget_2, 0, 0, 1, 1);

        top_box = new QWidget(widget);
        top_box->setObjectName("top_box");
        top_box->setGeometry(QRect(270, 20, 671, 51));
        top_box->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 176, 80);\n"
"border-top-right-radius: 10px\n"
""));
        horizontalLayout = new QHBoxLayout(top_box);
        horizontalLayout->setObjectName("horizontalLayout");
        btnNew = new QPushButton(top_box);
        btnNew->setObjectName("btnNew");
        btnNew->setStyleSheet(QString::fromUtf8("\n"
"	background-color:rgba(148, 105, 141, 255);\n"
"	color:rgba(255, 255, 255, 220);\n"
"	border-radius:5px;\n"
""));

        horizontalLayout->addWidget(btnNew);

        line_2 = new QFrame(top_box);
        line_2->setObjectName("line_2");
        line_2->setStyleSheet(QString::fromUtf8("color: rgb(0, 0, 0);"));
        line_2->setFrameShape(QFrame::VLine);
        line_2->setFrameShadow(QFrame::Sunken);

        horizontalLayout->addWidget(line_2);

        lineEdit = new QLineEdit(top_box);
        lineEdit->setObjectName("lineEdit");

        horizontalLayout->addWidget(lineEdit);

        middle_box->raise();
        right_box->raise();
        top_box->raise();
        left_box->raise();

        gridLayout->addWidget(widget, 0, 2, 1, 1);


        retranslateUi(Form);

        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QCoreApplication::translate("Form", "Form", nullptr));
        toolButton->setText(QCoreApplication::translate("Form", "...", nullptr));
        pushButton_2->setText(QCoreApplication::translate("Form", "PushButton", nullptr));
        pushButton_3->setText(QCoreApplication::translate("Form", "PushButton", nullptr));
        pushButton_4->setText(QCoreApplication::translate("Form", "PushButton", nullptr));
        pushButton_5->setText(QCoreApplication::translate("Form", "PushButton", nullptr));
        btnNew->setText(QCoreApplication::translate("Form", "+ New", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAIN_SCREEN_H

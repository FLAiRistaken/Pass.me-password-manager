/********************************************************************************
** Form generated from reading UI file 'new_item_screen.ui'
**
** Created by: Qt User Interface Compiler version 6.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_NEW_ITEM_SCREEN_H
#define UI_NEW_ITEM_SCREEN_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Form
{
public:
    QVBoxLayout *verticalLayout;
    QWidget *widget;
    QGridLayout *gridLayout_2;
    QFrame *divider;
    QLabel *lblNewItemTitle;
    QPushButton *btnClose;
    QFrame *button_group;
    QGridLayout *gridLayout;
    QToolButton *btnItem_Identity;
    QToolButton *btnItem_Bank_Card;
    QToolButton *btnItem_Bank_Acc;
    QToolButton *btnItem_Login;
    QToolButton *btnItem_Note;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName("Form");
        Form->resize(194, 0);
        Form->setStyleSheet(QString::fromUtf8(""));
        verticalLayout = new QVBoxLayout(Form);
        verticalLayout->setObjectName("verticalLayout");
        widget = new QWidget(Form);
        widget->setObjectName("widget");
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(widget->sizePolicy().hasHeightForWidth());
        widget->setSizePolicy(sizePolicy);
        widget->setMinimumSize(QSize(500, 537));
        widget->setStyleSheet(QString::fromUtf8("QToolButton{\n"
"	border-radius:6px;\n"
"	color: rgba(255, 255, 255, 220);\n"
"	padding: 10px;\n"
"}\n"
"QToolButton:hover{\n"
"	background-color: rgba(152, 108, 144, 115);\n"
"}\n"
"QPushButton#btnClose{\n"
"	color:rgba(255, 255, 255, 220);\n"
"}\n"
"QPushButton#btnClose:pressed{\n"
"	color: rgba(126, 126, 126, 220);\n"
"\n"
"}\n"
"QPushButton#btnClose:hover{\n"
"	color: rgba(190, 190, 190, 220);\n"
"}\n"
"\n"
"QWidget {\n"
"	background-color: rgba(32, 32, 32, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#button_group {\n"
"	background-color: rgba(255, 255, 255, 25);\n"
"	padding: 10px;\n"
"}\n"
"\n"
"QLabel#lblNewItemTitle {\n"
"	background-color: rgba(255, 255, 255, 25);\n"
"	padding: 5px;\n"
"}\n"
"\n"
""));
        gridLayout_2 = new QGridLayout(widget);
        gridLayout_2->setObjectName("gridLayout_2");
        gridLayout_2->setSizeConstraint(QLayout::SetMaximumSize);
        gridLayout_2->setContentsMargins(20, 20, 20, 20);
        divider = new QFrame(widget);
        divider->setObjectName("divider");
        QSizePolicy sizePolicy1(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(divider->sizePolicy().hasHeightForWidth());
        divider->setSizePolicy(sizePolicy1);
        divider->setMaximumSize(QSize(16777215, 1));
        divider->setStyleSheet(QString::fromUtf8("background-color: rgba(255, 255, 255, 80);\n"
"border: none;"));
        divider->setFrameShape(QFrame::HLine);
        divider->setFrameShadow(QFrame::Sunken);

        gridLayout_2->addWidget(divider, 3, 0, 1, 2);

        lblNewItemTitle = new QLabel(widget);
        lblNewItemTitle->setObjectName("lblNewItemTitle");
        QSizePolicy sizePolicy2(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(lblNewItemTitle->sizePolicy().hasHeightForWidth());
        lblNewItemTitle->setSizePolicy(sizePolicy2);
        lblNewItemTitle->setMaximumSize(QSize(364, 112));
        QFont font;
        font.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font.setPointSize(31);
        lblNewItemTitle->setFont(font);
        lblNewItemTitle->setStyleSheet(QString::fromUtf8("color: rgba(255,255,255, 220);"));
        lblNewItemTitle->setTextFormat(Qt::RichText);

        gridLayout_2->addWidget(lblNewItemTitle, 1, 0, 1, 2, Qt::AlignLeft);

        btnClose = new QPushButton(widget);
        btnClose->setObjectName("btnClose");
        QSizePolicy sizePolicy3(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(btnClose->sizePolicy().hasHeightForWidth());
        btnClose->setSizePolicy(sizePolicy3);
        btnClose->setMinimumSize(QSize(5, 0));
        btnClose->setMaximumSize(QSize(11, 21));
        QFont font1;
        font1.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font1.setPointSize(16);
        btnClose->setFont(font1);
        btnClose->setStyleSheet(QString::fromUtf8("border: none;"));

        gridLayout_2->addWidget(btnClose, 0, 0, 1, 1);

        button_group = new QFrame(widget);
        button_group->setObjectName("button_group");
        button_group->setStyleSheet(QString::fromUtf8(""));
        gridLayout = new QGridLayout(button_group);
        gridLayout->setObjectName("gridLayout");
        btnItem_Identity = new QToolButton(button_group);
        btnItem_Identity->setObjectName("btnItem_Identity");
        btnItem_Identity->setEnabled(true);
        QSizePolicy sizePolicy4(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy4.setHorizontalStretch(0);
        sizePolicy4.setVerticalStretch(0);
        sizePolicy4.setHeightForWidth(btnItem_Identity->sizePolicy().hasHeightForWidth());
        btnItem_Identity->setSizePolicy(sizePolicy4);
        btnItem_Identity->setMaximumSize(QSize(16777215, 75));
        btnItem_Identity->setFont(font1);
        btnItem_Identity->setLayoutDirection(Qt::LeftToRight);
        btnItem_Identity->setStyleSheet(QString::fromUtf8(""));
        btnItem_Identity->setPopupMode(QToolButton::InstantPopup);
        btnItem_Identity->setToolButtonStyle(Qt::ToolButtonTextBesideIcon);
        btnItem_Identity->setAutoRaise(false);
        btnItem_Identity->setArrowType(Qt::NoArrow);

        gridLayout->addWidget(btnItem_Identity, 1, 1, 1, 1);

        btnItem_Bank_Card = new QToolButton(button_group);
        btnItem_Bank_Card->setObjectName("btnItem_Bank_Card");
        btnItem_Bank_Card->setEnabled(true);
        sizePolicy4.setHeightForWidth(btnItem_Bank_Card->sizePolicy().hasHeightForWidth());
        btnItem_Bank_Card->setSizePolicy(sizePolicy4);
        btnItem_Bank_Card->setMaximumSize(QSize(16777215, 75));
        btnItem_Bank_Card->setFont(font1);
        btnItem_Bank_Card->setLayoutDirection(Qt::LeftToRight);
        btnItem_Bank_Card->setStyleSheet(QString::fromUtf8(""));
        btnItem_Bank_Card->setPopupMode(QToolButton::InstantPopup);
        btnItem_Bank_Card->setToolButtonStyle(Qt::ToolButtonTextBesideIcon);
        btnItem_Bank_Card->setAutoRaise(false);
        btnItem_Bank_Card->setArrowType(Qt::NoArrow);

        gridLayout->addWidget(btnItem_Bank_Card, 0, 1, 1, 1);

        btnItem_Bank_Acc = new QToolButton(button_group);
        btnItem_Bank_Acc->setObjectName("btnItem_Bank_Acc");
        btnItem_Bank_Acc->setEnabled(true);
        sizePolicy4.setHeightForWidth(btnItem_Bank_Acc->sizePolicy().hasHeightForWidth());
        btnItem_Bank_Acc->setSizePolicy(sizePolicy4);
        btnItem_Bank_Acc->setMaximumSize(QSize(16777215, 75));
        btnItem_Bank_Acc->setFont(font1);
        btnItem_Bank_Acc->setLayoutDirection(Qt::LeftToRight);
        btnItem_Bank_Acc->setStyleSheet(QString::fromUtf8(""));
        btnItem_Bank_Acc->setPopupMode(QToolButton::InstantPopup);
        btnItem_Bank_Acc->setToolButtonStyle(Qt::ToolButtonTextBesideIcon);
        btnItem_Bank_Acc->setAutoRaise(false);
        btnItem_Bank_Acc->setArrowType(Qt::NoArrow);

        gridLayout->addWidget(btnItem_Bank_Acc, 1, 0, 1, 1);

        btnItem_Login = new QToolButton(button_group);
        btnItem_Login->setObjectName("btnItem_Login");
        btnItem_Login->setEnabled(true);
        sizePolicy4.setHeightForWidth(btnItem_Login->sizePolicy().hasHeightForWidth());
        btnItem_Login->setSizePolicy(sizePolicy4);
        btnItem_Login->setMaximumSize(QSize(16777215, 75));
        btnItem_Login->setFont(font1);
        btnItem_Login->setLayoutDirection(Qt::LeftToRight);
        btnItem_Login->setStyleSheet(QString::fromUtf8(""));
        btnItem_Login->setPopupMode(QToolButton::InstantPopup);
        btnItem_Login->setToolButtonStyle(Qt::ToolButtonTextBesideIcon);
        btnItem_Login->setAutoRaise(false);
        btnItem_Login->setArrowType(Qt::NoArrow);

        gridLayout->addWidget(btnItem_Login, 0, 0, 1, 1);

        btnItem_Note = new QToolButton(button_group);
        btnItem_Note->setObjectName("btnItem_Note");
        btnItem_Note->setEnabled(true);
        sizePolicy4.setHeightForWidth(btnItem_Note->sizePolicy().hasHeightForWidth());
        btnItem_Note->setSizePolicy(sizePolicy4);
        btnItem_Note->setMaximumSize(QSize(16777215, 75));
        btnItem_Note->setFont(font1);
        btnItem_Note->setLayoutDirection(Qt::LeftToRight);
        btnItem_Note->setStyleSheet(QString::fromUtf8(""));
        btnItem_Note->setPopupMode(QToolButton::InstantPopup);
        btnItem_Note->setToolButtonStyle(Qt::ToolButtonTextBesideIcon);
        btnItem_Note->setAutoRaise(false);
        btnItem_Note->setArrowType(Qt::NoArrow);

        gridLayout->addWidget(btnItem_Note, 2, 0, 1, 1);


        gridLayout_2->addWidget(button_group, 4, 0, 1, 2);


        verticalLayout->addWidget(widget);


        retranslateUi(Form);

        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QCoreApplication::translate("Form", "Form", nullptr));
        lblNewItemTitle->setText(QCoreApplication::translate("Form", "<html><head/><body><p>Select desired item </p><p>to add to your <span style=\" font-weight:700;\">pass.me</span></p></body></html>", nullptr));
        btnClose->setText(QCoreApplication::translate("Form", "X", nullptr));
        btnItem_Identity->setText(QCoreApplication::translate("Form", "identity", nullptr));
        btnItem_Bank_Card->setText(QCoreApplication::translate("Form", "bank card", nullptr));
        btnItem_Bank_Acc->setText(QCoreApplication::translate("Form", "bank account", nullptr));
        btnItem_Login->setText(QCoreApplication::translate("Form", "login", nullptr));
        btnItem_Note->setText(QCoreApplication::translate("Form", "secure note", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_NEW_ITEM_SCREEN_H

/********************************************************************************
** Form generated from reading UI file 'loginScreen.ui'
**
** Created by: Qt User Interface Compiler version 6.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_LOGINSCREEN_H
#define UI_LOGINSCREEN_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Form
{
public:
    QGridLayout *gridLayout;
    QWidget *widget;
    QWidget *leftBox;
    QVBoxLayout *verticalLayout;
    QSpacerItem *verticalSpacer_5;
    QVBoxLayout *verticalLayout_2;
    QLabel *lblTitle;
    QLabel *lblSubTitle;
    QSpacerItem *verticalSpacer_4;
    QWidget *rightBox;
    QGridLayout *gridLayout_2;
    QLabel *lblMasterPassword;
    QSpacerItem *verticalSpacer_2;
    QLabel *lblEmail;
    QLabel *lblMassPassHint;
    QPushButton *btnLogin;
    QSpacerItem *verticalSpacer_3;
    QLabel *lblHelp;
    QLineEdit *lineEdit_MastPassword;
    QPushButton *btnCreate;
    QLabel *lblLogin;
    QSpacerItem *verticalSpacer;
    QLineEdit *lineEdit_Email;
    QLabel *lblNew;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName("Form");
        Form->resize(834, 479);
        Form->setMinimumSize(QSize(834, 479));
        gridLayout = new QGridLayout(Form);
        gridLayout->setObjectName("gridLayout");
        widget = new QWidget(Form);
        widget->setObjectName("widget");
        widget->setMinimumSize(QSize(834, 479));
        QFont font;
        font.setFamilies({QString::fromUtf8("Nexa-Trial")});
        widget->setFont(font);
        widget->setStyleSheet(QString::fromUtf8("QPushButton#btnLogin{\n"
"	background-color:rgba(148, 105, 141, 255);\n"
"	color:rgba(255, 255, 255, 220);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#btnLogin:pressed{\n"
"\n"
"	background-color:rgba(74, 53, 70, 255);\n"
"\n"
"}\n"
"QPushButton#btnLogin:hover{\n"
"	background-color:rgba(111, 77, 104, 255);\n"
"}\n"
"QPushButton#btnCreate{\n"
"	background-color:rgba(170, 170, 170, 255);\n"
"	color:rgba(255, 255, 255, 200);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#btnCreate:hover{\n"
"	background-color:rgba(140, 140, 140, 255);\n"
"}\n"
"QWidget#leftBox{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, 		stop:0 rgba(0, 0, 0, 255), stop:1 rgba(92, 61, 88, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"QWidget#rightBox{\n"
"	background-color: rgba(255, 255, 255, 255);\n"
"	border-radius: 10px\n"
"}"));
        leftBox = new QWidget(widget);
        leftBox->setObjectName("leftBox");
        leftBox->setGeometry(QRect(12, 3, 281, 451));
        leftBox->setStyleSheet(QString::fromUtf8(""));
        verticalLayout = new QVBoxLayout(leftBox);
        verticalLayout->setObjectName("verticalLayout");
        verticalLayout->setContentsMargins(20, -1, -1, -1);
        verticalSpacer_5 = new QSpacerItem(20, 30, QSizePolicy::Minimum, QSizePolicy::Preferred);

        verticalLayout->addItem(verticalSpacer_5);

        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setObjectName("verticalLayout_2");
        lblTitle = new QLabel(leftBox);
        lblTitle->setObjectName("lblTitle");
        lblTitle->setMaximumSize(QSize(16777215, 60));
        QFont font1;
        font1.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font1.setPointSize(50);
        font1.setBold(false);
        font1.setItalic(false);
        lblTitle->setFont(font1);
        lblTitle->setStyleSheet(QString::fromUtf8("color:rgba(255, 255, 255, 225);"));

        verticalLayout_2->addWidget(lblTitle);

        lblSubTitle = new QLabel(leftBox);
        lblSubTitle->setObjectName("lblSubTitle");
        QFont font2;
        font2.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font2.setPointSize(26);
        lblSubTitle->setFont(font2);
        lblSubTitle->setStyleSheet(QString::fromUtf8("color:rgba(255, 255, 255, 225)"));
        lblSubTitle->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignTop);
        lblSubTitle->setIndent(0);

        verticalLayout_2->addWidget(lblSubTitle);


        verticalLayout->addLayout(verticalLayout_2);

        verticalSpacer_4 = new QSpacerItem(20, 150, QSizePolicy::Minimum, QSizePolicy::Preferred);

        verticalLayout->addItem(verticalSpacer_4);

        rightBox = new QWidget(widget);
        rightBox->setObjectName("rightBox");
        rightBox->setGeometry(QRect(280, 40, 501, 381));
        gridLayout_2 = new QGridLayout(rightBox);
        gridLayout_2->setObjectName("gridLayout_2");
        gridLayout_2->setContentsMargins(30, 20, -1, -1);
        lblMasterPassword = new QLabel(rightBox);
        lblMasterPassword->setObjectName("lblMasterPassword");
        lblMasterPassword->setFont(font);
        lblMasterPassword->setStyleSheet(QString::fromUtf8("color:rgba(0, 0, 0, 200)"));

        gridLayout_2->addWidget(lblMasterPassword, 9, 0, 1, 2);

        verticalSpacer_2 = new QSpacerItem(20, 20, QSizePolicy::Minimum, QSizePolicy::Preferred);

        gridLayout_2->addItem(verticalSpacer_2, 12, 0, 1, 1);

        lblEmail = new QLabel(rightBox);
        lblEmail->setObjectName("lblEmail");
        lblEmail->setFont(font);
        lblEmail->setStyleSheet(QString::fromUtf8("color:rgba(0, 0, 0, 200)"));

        gridLayout_2->addWidget(lblEmail, 5, 0, 1, 1);

        lblMassPassHint = new QLabel(rightBox);
        lblMassPassHint->setObjectName("lblMassPassHint");
        QFont font3;
        font3.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font3.setPointSize(12);
        font3.setBold(false);
        font3.setItalic(false);
        lblMassPassHint->setFont(font3);
        lblMassPassHint->setStyleSheet(QString::fromUtf8("color: rgba(0, 0, 0, 200);"));

        gridLayout_2->addWidget(lblMassPassHint, 11, 0, 1, 2);

        btnLogin = new QPushButton(rightBox);
        btnLogin->setObjectName("btnLogin");
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(btnLogin->sizePolicy().hasHeightForWidth());
        btnLogin->setSizePolicy(sizePolicy);
        btnLogin->setMinimumSize(QSize(350, 30));
        btnLogin->setBaseSize(QSize(0, 0));
        QFont font4;
        font4.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font4.setPointSize(16);
        font4.setItalic(false);
        btnLogin->setFont(font4);
        btnLogin->setStyleSheet(QString::fromUtf8(""));

        gridLayout_2->addWidget(btnLogin, 13, 0, 1, 1);

        verticalSpacer_3 = new QSpacerItem(20, 10, QSizePolicy::Minimum, QSizePolicy::Preferred);

        gridLayout_2->addItem(verticalSpacer_3, 4, 0, 1, 1);

        lblHelp = new QLabel(rightBox);
        lblHelp->setObjectName("lblHelp");
        QFont font5;
        font5.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font5.setPointSize(12);
        font5.setItalic(false);
        lblHelp->setFont(font5);
        lblHelp->setStyleSheet(QString::fromUtf8("color: rgba(0, 0, 0, 200);"));
        lblHelp->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(lblHelp, 11, 2, 1, 1);

        lineEdit_MastPassword = new QLineEdit(rightBox);
        lineEdit_MastPassword->setObjectName("lineEdit_MastPassword");
        lineEdit_MastPassword->setMinimumSize(QSize(350, 30));
        QFont font6;
        font6.setFamilies({QString::fromUtf8(".AppleSystemUIFont")});
        lineEdit_MastPassword->setFont(font6);
        lineEdit_MastPassword->setStyleSheet(QString::fromUtf8("background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px"));
        lineEdit_MastPassword->setEchoMode(QLineEdit::Password);

        gridLayout_2->addWidget(lineEdit_MastPassword, 10, 0, 1, 3);

        btnCreate = new QPushButton(rightBox);
        btnCreate->setObjectName("btnCreate");
        btnCreate->setMinimumSize(QSize(110, 30));
        QFont font7;
        font7.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font7.setPointSize(13);
        font7.setItalic(false);
        btnCreate->setFont(font7);
        btnCreate->setStyleSheet(QString::fromUtf8(""));

        gridLayout_2->addWidget(btnCreate, 2, 3, 1, 1);

        lblLogin = new QLabel(rightBox);
        lblLogin->setObjectName("lblLogin");
        QFont font8;
        font8.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font8.setPointSize(40);
        font8.setBold(true);
        font8.setItalic(false);
        font8.setUnderline(false);
        font8.setStrikeOut(false);
        lblLogin->setFont(font8);
        lblLogin->setStyleSheet(QString::fromUtf8("color: rgba(0, 0, 0, 220);"));

        gridLayout_2->addWidget(lblLogin, 3, 0, 1, 4);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_2->addItem(verticalSpacer, 14, 0, 1, 1);

        lineEdit_Email = new QLineEdit(rightBox);
        lineEdit_Email->setObjectName("lineEdit_Email");
        lineEdit_Email->setMinimumSize(QSize(350, 30));
        lineEdit_Email->setFont(font6);
        lineEdit_Email->setStyleSheet(QString::fromUtf8("background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px"));
        lineEdit_Email->setEchoMode(QLineEdit::Normal);

        gridLayout_2->addWidget(lineEdit_Email, 6, 0, 1, 3);

        lblNew = new QLabel(rightBox);
        lblNew->setObjectName("lblNew");
        lblNew->setMinimumSize(QSize(110, 0));
        lblNew->setFont(font);
        lblNew->setStyleSheet(QString::fromUtf8("color: rgba(0, 0, 0, 170);"));

        gridLayout_2->addWidget(lblNew, 2, 2, 1, 1);

        rightBox->raise();
        leftBox->raise();

        gridLayout->addWidget(widget, 0, 0, 1, 1);


        retranslateUi(Form);

        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QCoreApplication::translate("Form", "Form", nullptr));
        lblTitle->setText(QCoreApplication::translate("Form", "pass.me", nullptr));
        lblSubTitle->setText(QCoreApplication::translate("Form", "<html><head/><body>\n"
"<p style=\"line-height:0.4\"><span>\n"
"welcome to the \n"
"</span></p>\n"
"<p style=\"line-height:0.4\"><span>\n"
"pass.me app\n"
"</span></p>\n"
"</body></html>", nullptr));
        lblMasterPassword->setText(QCoreApplication::translate("Form", "master password", nullptr));
        lblEmail->setText(QCoreApplication::translate("Form", "email", nullptr));
        lblMassPassHint->setText(QCoreApplication::translate("Form", "get master password hint", nullptr));
        btnLogin->setText(QCoreApplication::translate("Form", "log in", nullptr));
        lblHelp->setText(QCoreApplication::translate("Form", "help?", nullptr));
        lineEdit_MastPassword->setPlaceholderText(QString());
        btnCreate->setText(QCoreApplication::translate("Form", "create account", nullptr));
        lblLogin->setText(QCoreApplication::translate("Form", "log in to pass.me", nullptr));
        lineEdit_Email->setPlaceholderText(QString());
        lblNew->setText(QCoreApplication::translate("Form", "new to pass.me?", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LOGINSCREEN_H

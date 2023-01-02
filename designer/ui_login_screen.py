/********************************************************************************
** Form generated from reading UI file 'login_screen.ui'
**
** Created by: Qt User Interface Compiler version 6.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_LOGIN_SCREEN_H
#define UI_LOGIN_SCREEN_H

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
    QPushButton *btnClose;
    QSpacerItem *verticalSpacer_5;
    QVBoxLayout *verticalLayout_2;
    QLabel *lblTitle;
    QLabel *lblSubTitle;
    QSpacerItem *verticalSpacer_4;
    QWidget *rightBox_Hint;
    QGridLayout *gridLayout_5;
    QSpacerItem *verticalSpacer_12;
    QSpacerItem *verticalSpacer_14;
    QLineEdit *lineEdit_Email_Hint;
    QLabel *lblEmail_Hint;
    QLabel *lblMassHint;
    QPushButton *btnBack;
    QSpacerItem *verticalSpacer_13;
    QLabel *lblError;
    QPushButton *btnGetHint;
    QSpacerItem *horizontalSpacer;
    QWidget *rightBox;
    QGridLayout *gridLayout_2;
    QLabel *lblNew;
    QLabel *lblHelp;
    QSpacerItem *verticalSpacer_3;
    QSpacerItem *verticalSpacer;
    QPushButton *btnLogin;
    QSpacerItem *verticalSpacer_2;
    QLabel *lblEmail;
    QLineEdit *lineEdit_Email;
    QPushButton *btnCreate;
    QLineEdit *lineEdit_MastPassword;
    QLabel *lblLogin;
    QPushButton *btnHint;
    QLabel *lblMasterPassword;

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
"	background-color:rgba(74, 53, 70, 255);\n"
"}\n"
"QPushButton#btnLogin:hover{\n"
"	background-color:rgba(111, 77, 104, 255);\n"
"}\n"
"QPushButton#btnLogin:disabled{\n"
"	background-color:rgba(148, 105, 141, 100);\n"
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
"}\n"
"QPushButton#btnClose{\n"
"	color:rgba(255, 255, 255, 220);\n"
"}\n"
"QPushButton#btnClose:pressed{\n"
"	co"
                        "lor: rgba(126, 126, 126, 220);\n"
"\n"
"}\n"
"QPushButton#btnClose:hover{\n"
"	color: rgba(190, 190, 190, 220);\n"
"}\n"
"QWidget#rightBox_Hint{\n"
"	background-color: rgba(255, 255, 255, 255);\n"
"	border-radius: 10px\n"
"}\n"
"QPushButton#btnGetHint{\n"
"	background-color:rgba(148, 105, 141, 255);\n"
"	color:rgba(255, 255, 255, 220);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#btnGetHint:pressed{\n"
"\n"
"	background-color:rgba(74, 53, 70, 255);\n"
"\n"
"}\n"
"QPushButton#btnGetHint:hover{\n"
"	background-color:rgba(111, 77, 104, 255);\n"
"}"));
        leftBox = new QWidget(widget);
        leftBox->setObjectName("leftBox");
        leftBox->setGeometry(QRect(12, 3, 281, 451));
        leftBox->setMinimumSize(QSize(281, 451));
        leftBox->setStyleSheet(QString::fromUtf8(""));
        verticalLayout = new QVBoxLayout(leftBox);
        verticalLayout->setObjectName("verticalLayout");
        verticalLayout->setContentsMargins(20, 20, -1, -1);
        btnClose = new QPushButton(leftBox);
        btnClose->setObjectName("btnClose");
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(btnClose->sizePolicy().hasHeightForWidth());
        btnClose->setSizePolicy(sizePolicy);
        btnClose->setMinimumSize(QSize(5, 0));
        QFont font1;
        font1.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font1.setPointSize(16);
        btnClose->setFont(font1);
        btnClose->setStyleSheet(QString::fromUtf8("border: none;"));

        verticalLayout->addWidget(btnClose);

        verticalSpacer_5 = new QSpacerItem(20, 30, QSizePolicy::Minimum, QSizePolicy::Preferred);

        verticalLayout->addItem(verticalSpacer_5);

        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setObjectName("verticalLayout_2");
        lblTitle = new QLabel(leftBox);
        lblTitle->setObjectName("lblTitle");
        lblTitle->setMaximumSize(QSize(16777215, 60));
        QFont font2;
        font2.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font2.setPointSize(50);
        font2.setBold(false);
        font2.setItalic(false);
        lblTitle->setFont(font2);
        lblTitle->setStyleSheet(QString::fromUtf8("color:rgba(255, 255, 255, 225);"));

        verticalLayout_2->addWidget(lblTitle);

        lblSubTitle = new QLabel(leftBox);
        lblSubTitle->setObjectName("lblSubTitle");
        QFont font3;
        font3.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font3.setPointSize(26);
        lblSubTitle->setFont(font3);
        lblSubTitle->setStyleSheet(QString::fromUtf8("color:rgba(255, 255, 255, 225)"));
        lblSubTitle->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignTop);
        lblSubTitle->setIndent(0);

        verticalLayout_2->addWidget(lblSubTitle);


        verticalLayout->addLayout(verticalLayout_2);

        verticalSpacer_4 = new QSpacerItem(20, 150, QSizePolicy::Minimum, QSizePolicy::Preferred);

        verticalLayout->addItem(verticalSpacer_4);

        rightBox_Hint = new QWidget(widget);
        rightBox_Hint->setObjectName("rightBox_Hint");
        rightBox_Hint->setEnabled(false);
        rightBox_Hint->setGeometry(QRect(280, 40, 501, 381));
        rightBox_Hint->setMinimumSize(QSize(501, 381));
        gridLayout_5 = new QGridLayout(rightBox_Hint);
        gridLayout_5->setObjectName("gridLayout_5");
        gridLayout_5->setContentsMargins(30, 20, -1, -1);
        verticalSpacer_12 = new QSpacerItem(20, 20, QSizePolicy::Minimum, QSizePolicy::Preferred);

        gridLayout_5->addItem(verticalSpacer_12, 8, 0, 1, 1);

        verticalSpacer_14 = new QSpacerItem(20, 10, QSizePolicy::Minimum, QSizePolicy::Preferred);

        gridLayout_5->addItem(verticalSpacer_14, 3, 0, 1, 1);

        lineEdit_Email_Hint = new QLineEdit(rightBox_Hint);
        lineEdit_Email_Hint->setObjectName("lineEdit_Email_Hint");
        lineEdit_Email_Hint->setMinimumSize(QSize(350, 30));
        QFont font4;
        font4.setFamilies({QString::fromUtf8(".AppleSystemUIFont")});
        lineEdit_Email_Hint->setFont(font4);
        lineEdit_Email_Hint->setStyleSheet(QString::fromUtf8("background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px"));
        lineEdit_Email_Hint->setEchoMode(QLineEdit::Normal);

        gridLayout_5->addWidget(lineEdit_Email_Hint, 5, 0, 1, 1);

        lblEmail_Hint = new QLabel(rightBox_Hint);
        lblEmail_Hint->setObjectName("lblEmail_Hint");
        lblEmail_Hint->setFont(font);
        lblEmail_Hint->setStyleSheet(QString::fromUtf8("color:rgba(0, 0, 0, 200)"));

        gridLayout_5->addWidget(lblEmail_Hint, 4, 0, 1, 1);

        lblMassHint = new QLabel(rightBox_Hint);
        lblMassHint->setObjectName("lblMassHint");
        QFont font5;
        font5.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font5.setPointSize(40);
        font5.setBold(true);
        font5.setItalic(false);
        font5.setUnderline(false);
        font5.setStrikeOut(false);
        lblMassHint->setFont(font5);
        lblMassHint->setStyleSheet(QString::fromUtf8("color: rgba(0, 0, 0, 220);"));

        gridLayout_5->addWidget(lblMassHint, 2, 0, 1, 3);

        btnBack = new QPushButton(rightBox_Hint);
        btnBack->setObjectName("btnBack");
        sizePolicy.setHeightForWidth(btnBack->sizePolicy().hasHeightForWidth());
        btnBack->setSizePolicy(sizePolicy);
        btnBack->setMinimumSize(QSize(5, 0));
        QFont font6;
        font6.setFamilies({QString::fromUtf8("Waseem")});
        font6.setPointSize(25);
        btnBack->setFont(font6);
        btnBack->setStyleSheet(QString::fromUtf8("border: none;\n"
"color: rgb(0, 0, 0);"));

        gridLayout_5->addWidget(btnBack, 0, 0, 1, 3);

        verticalSpacer_13 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_5->addItem(verticalSpacer_13, 11, 0, 1, 1);

        lblError = new QLabel(rightBox_Hint);
        lblError->setObjectName("lblError");
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(lblError->sizePolicy().hasHeightForWidth());
        lblError->setSizePolicy(sizePolicy1);
        lblError->setMinimumSize(QSize(0, 40));
        QFont font7;
        font7.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font7.setPointSize(12);
        lblError->setFont(font7);
        lblError->setStyleSheet(QString::fromUtf8("color: rgba(0, 0, 0 ,180); "));

        gridLayout_5->addWidget(lblError, 6, 0, 1, 1);

        btnGetHint = new QPushButton(rightBox_Hint);
        btnGetHint->setObjectName("btnGetHint");
        sizePolicy.setHeightForWidth(btnGetHint->sizePolicy().hasHeightForWidth());
        btnGetHint->setSizePolicy(sizePolicy);
        btnGetHint->setMinimumSize(QSize(350, 30));
        btnGetHint->setBaseSize(QSize(0, 0));
        QFont font8;
        font8.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font8.setPointSize(16);
        font8.setItalic(false);
        btnGetHint->setFont(font8);
        btnGetHint->setStyleSheet(QString::fromUtf8(""));

        gridLayout_5->addWidget(btnGetHint, 10, 0, 1, 1);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_5->addItem(horizontalSpacer, 5, 2, 1, 1);

        rightBox = new QWidget(widget);
        rightBox->setObjectName("rightBox");
        rightBox->setGeometry(QRect(280, 40, 501, 381));
        rightBox->setMinimumSize(QSize(501, 381));
        gridLayout_2 = new QGridLayout(rightBox);
        gridLayout_2->setObjectName("gridLayout_2");
        gridLayout_2->setContentsMargins(30, 20, -1, -1);
        lblNew = new QLabel(rightBox);
        lblNew->setObjectName("lblNew");
        lblNew->setMinimumSize(QSize(110, 0));
        lblNew->setFont(font);
        lblNew->setStyleSheet(QString::fromUtf8("color: rgba(0, 0, 0, 170);"));

        gridLayout_2->addWidget(lblNew, 2, 1, 1, 1);

        lblHelp = new QLabel(rightBox);
        lblHelp->setObjectName("lblHelp");
        QFont font9;
        font9.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font9.setPointSize(12);
        font9.setItalic(false);
        lblHelp->setFont(font9);
        lblHelp->setStyleSheet(QString::fromUtf8("color: rgba(0, 0, 0, 200);"));
        lblHelp->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(lblHelp, 9, 1, 1, 1);

        verticalSpacer_3 = new QSpacerItem(20, 10, QSizePolicy::Minimum, QSizePolicy::Preferred);

        gridLayout_2->addItem(verticalSpacer_3, 4, 0, 1, 1);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_2->addItem(verticalSpacer, 12, 0, 1, 1);

        btnLogin = new QPushButton(rightBox);
        btnLogin->setObjectName("btnLogin");
        sizePolicy.setHeightForWidth(btnLogin->sizePolicy().hasHeightForWidth());
        btnLogin->setSizePolicy(sizePolicy);
        btnLogin->setMinimumSize(QSize(350, 30));
        btnLogin->setBaseSize(QSize(0, 0));
        btnLogin->setFont(font8);
        btnLogin->setStyleSheet(QString::fromUtf8(""));

        gridLayout_2->addWidget(btnLogin, 11, 0, 1, 1);

        verticalSpacer_2 = new QSpacerItem(20, 20, QSizePolicy::Minimum, QSizePolicy::Preferred);

        gridLayout_2->addItem(verticalSpacer_2, 10, 0, 1, 1);

        lblEmail = new QLabel(rightBox);
        lblEmail->setObjectName("lblEmail");
        lblEmail->setFont(font);
        lblEmail->setStyleSheet(QString::fromUtf8("color:rgba(0, 0, 0, 200)"));

        gridLayout_2->addWidget(lblEmail, 5, 0, 1, 1);

        lineEdit_Email = new QLineEdit(rightBox);
        lineEdit_Email->setObjectName("lineEdit_Email");
        lineEdit_Email->setMinimumSize(QSize(350, 30));
        lineEdit_Email->setFont(font4);
        lineEdit_Email->setStyleSheet(QString::fromUtf8("background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px"));
        lineEdit_Email->setEchoMode(QLineEdit::Normal);

        gridLayout_2->addWidget(lineEdit_Email, 6, 0, 1, 2);

        btnCreate = new QPushButton(rightBox);
        btnCreate->setObjectName("btnCreate");
        btnCreate->setMinimumSize(QSize(110, 30));
        QFont font10;
        font10.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font10.setPointSize(13);
        font10.setItalic(false);
        btnCreate->setFont(font10);
        btnCreate->setStyleSheet(QString::fromUtf8(""));

        gridLayout_2->addWidget(btnCreate, 2, 2, 1, 1);

        lineEdit_MastPassword = new QLineEdit(rightBox);
        lineEdit_MastPassword->setObjectName("lineEdit_MastPassword");
        lineEdit_MastPassword->setMinimumSize(QSize(350, 30));
        lineEdit_MastPassword->setFont(font4);
        lineEdit_MastPassword->setStyleSheet(QString::fromUtf8("background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px"));
        lineEdit_MastPassword->setEchoMode(QLineEdit::Password);

        gridLayout_2->addWidget(lineEdit_MastPassword, 8, 0, 1, 2);

        lblLogin = new QLabel(rightBox);
        lblLogin->setObjectName("lblLogin");
        lblLogin->setFont(font5);
        lblLogin->setStyleSheet(QString::fromUtf8("color: rgba(0, 0, 0, 220);"));

        gridLayout_2->addWidget(lblLogin, 3, 0, 1, 3);

        btnHint = new QPushButton(rightBox);
        btnHint->setObjectName("btnHint");
        btnHint->setFont(font);
        btnHint->setStyleSheet(QString::fromUtf8("border: none;\n"
"color: rgba(0, 0, 0, 200);"));
        btnHint->setFlat(false);

        gridLayout_2->addWidget(btnHint, 9, 0, 1, 1, Qt::AlignLeft);

        lblMasterPassword = new QLabel(rightBox);
        lblMasterPassword->setObjectName("lblMasterPassword");
        lblMasterPassword->setFont(font);
        lblMasterPassword->setStyleSheet(QString::fromUtf8("color:rgba(0, 0, 0, 200)"));

        gridLayout_2->addWidget(lblMasterPassword, 7, 0, 1, 1);

        rightBox_Hint->raise();
        rightBox->raise();
        leftBox->raise();

        gridLayout->addWidget(widget, 0, 0, 1, 1);


        retranslateUi(Form);

        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QCoreApplication::translate("Form", "Form", nullptr));
        btnClose->setText(QCoreApplication::translate("Form", "X", nullptr));
        lblTitle->setText(QCoreApplication::translate("Form", "pass.me", nullptr));
        lblSubTitle->setText(QCoreApplication::translate("Form", "<html><head/><body>\n"
"<p style=\"line-height:0.4\"><span>\n"
"welcome to the \n"
"</span></p>\n"
"<p style=\"line-height:0.4\"><span>\n"
"pass.me app\n"
"</span></p>\n"
"</body></html>", nullptr));
        lineEdit_Email_Hint->setPlaceholderText(QString());
        lblEmail_Hint->setText(QCoreApplication::translate("Form", "email", nullptr));
        lblMassHint->setText(QCoreApplication::translate("Form", "master password hint", nullptr));
        btnBack->setText(QCoreApplication::translate("Form", "<", nullptr));
        lblError->setText(QCoreApplication::translate("Form", "\n"
"<html><head/><body>\n"
"<p style=\"line-height:0.4\"><span>\n"
"enter the email for your account. \n"
"</span></p>\n"
"<p style=\"line-height:0.4\"><span>\n"
"if a matching record is found, an email containing your hint will be sent\n"
"</span></p>\n"
"</body></html>", nullptr));
        btnGetHint->setText(QCoreApplication::translate("Form", "get hint", nullptr));
        lblNew->setText(QCoreApplication::translate("Form", "new to pass.me?", nullptr));
        lblHelp->setText(QCoreApplication::translate("Form", "help?", nullptr));
        btnLogin->setText(QCoreApplication::translate("Form", "log in", nullptr));
        lblEmail->setText(QCoreApplication::translate("Form", "email", nullptr));
        lineEdit_Email->setPlaceholderText(QString());
        btnCreate->setText(QCoreApplication::translate("Form", "create account", nullptr));
        lineEdit_MastPassword->setPlaceholderText(QString());
        lblLogin->setText(QCoreApplication::translate("Form", "log in to pass.me", nullptr));
        btnHint->setText(QCoreApplication::translate("Form", "get master password hint", nullptr));
        lblMasterPassword->setText(QCoreApplication::translate("Form", "master password", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LOGIN_SCREEN_H

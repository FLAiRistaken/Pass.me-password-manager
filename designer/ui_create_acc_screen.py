/********************************************************************************
** Form generated from reading UI file 'create_acc_screen.ui'
**
** Created by: Qt User Interface Compiler version 6.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CREATE_ACC_SCREEN_H
#define UI_CREATE_ACC_SCREEN_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QProgressBar>
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
    QWidget *rightBox;
    QGridLayout *gridLayout_2;
    QSpacerItem *verticalSpacer;
    QLineEdit *lineEdit_PassHint;
    QLabel *lblMasterPassword;
    QLabel *lblPasswordHint;
    QPushButton *btnCreate;
    QSpacerItem *verticalSpacer_3;
    QLabel *lblHintDesc;
    QLabel *lblMasterPassword2;
    QLabel *lblPassDesc;
    QLineEdit *lineEdit_Email;
    QLineEdit *lineEdit_MastPassword;
    QLabel *lblNew;
    QLineEdit *lineEdit_Name;
    QLabel *lblCreate;
    QLabel *lblName;
    QLineEdit *lineEdit_MastPassword2;
    QSpacerItem *verticalSpacer_2;
    QPushButton *btnLogin;
    QSpacerItem *verticalSpacer_6;
    QProgressBar *passStrengthBar;
    QLabel *lblEmail;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName("Form");
        Form->resize(869, 730);
        Form->setMinimumSize(QSize(824, 699));
        gridLayout = new QGridLayout(Form);
        gridLayout->setObjectName("gridLayout");
        widget = new QWidget(Form);
        widget->setObjectName("widget");
        widget->setMinimumSize(QSize(800, 675));
        QFont font;
        font.setFamilies({QString::fromUtf8("Nexa-Trial")});
        widget->setFont(font);
        widget->setStyleSheet(QString::fromUtf8("QPushButton#btnCreate{\n"
"	background-color:rgba(148, 105, 141, 255);\n"
"	color:rgba(255, 255, 255, 220);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#btnCreate:pressed{\n"
"\n"
"	background-color:rgba(74, 53, 70, 255);\n"
"\n"
"}\n"
"QPushButton#btnCreate:hover{\n"
"	background-color:rgba(111, 77, 104, 255);\n"
"}\n"
"QPushButton#btnLogin{\n"
"	background-color:rgba(170, 170, 170, 255);\n"
"	color:rgba(255, 255, 255, 200);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#btnLogin:hover{\n"
"	background-color:rgba(140, 140, 140, 255);\n"
"}\n"
"\n"
"QProgressBar#passStrengthBar{\n"
"	background-color: rgba(140, 140, 140, 255);\n"
"}\n"
"QProgressBar#passStrengthBar::chunk{\n"
"	background-color: rgba(110, 77, 103, 220);\n"
"	border-radius:5px;\n"
"}\n"
"QWidget#leftBox{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, 		stop:0 rgba(0, 0, 0, 255), stop:1 rgba(92, 61, 88, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"QWidget#rightBox{\n"
"	background-color: rgba(255, 255, 255, 255);\n"
"	b"
                        "order-radius: 10px\n"
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
"}"));
        leftBox = new QWidget(widget);
        leftBox->setObjectName("leftBox");
        leftBox->setGeometry(QRect(0, 0, 281, 680));
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

        rightBox = new QWidget(widget);
        rightBox->setObjectName("rightBox");
        rightBox->setGeometry(QRect(270, 40, 501, 610));
        gridLayout_2 = new QGridLayout(rightBox);
        gridLayout_2->setObjectName("gridLayout_2");
        gridLayout_2->setContentsMargins(30, 20, -1, 50);
        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_2->addItem(verticalSpacer, 31, 0, 1, 1);

        lineEdit_PassHint = new QLineEdit(rightBox);
        lineEdit_PassHint->setObjectName("lineEdit_PassHint");
        lineEdit_PassHint->setMinimumSize(QSize(350, 30));
        QFont font4;
        font4.setFamilies({QString::fromUtf8(".AppleSystemUIFont")});
        lineEdit_PassHint->setFont(font4);
        lineEdit_PassHint->setStyleSheet(QString::fromUtf8("background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px"));
        lineEdit_PassHint->setEchoMode(QLineEdit::Password);

        gridLayout_2->addWidget(lineEdit_PassHint, 21, 0, 1, 1);

        lblMasterPassword = new QLabel(rightBox);
        lblMasterPassword->setObjectName("lblMasterPassword");
        lblMasterPassword->setFont(font);
        lblMasterPassword->setStyleSheet(QString::fromUtf8("color:rgba(0, 0, 0, 200)"));

        gridLayout_2->addWidget(lblMasterPassword, 13, 0, 1, 2);

        lblPasswordHint = new QLabel(rightBox);
        lblPasswordHint->setObjectName("lblPasswordHint");
        lblPasswordHint->setFont(font);
        lblPasswordHint->setStyleSheet(QString::fromUtf8("color:rgba(0, 0, 0, 200)"));

        gridLayout_2->addWidget(lblPasswordHint, 20, 0, 1, 1);

        btnCreate = new QPushButton(rightBox);
        btnCreate->setObjectName("btnCreate");
        sizePolicy.setHeightForWidth(btnCreate->sizePolicy().hasHeightForWidth());
        btnCreate->setSizePolicy(sizePolicy);
        btnCreate->setMinimumSize(QSize(350, 30));
        btnCreate->setBaseSize(QSize(0, 0));
        QFont font5;
        font5.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font5.setPointSize(16);
        font5.setItalic(false);
        btnCreate->setFont(font5);
        btnCreate->setStyleSheet(QString::fromUtf8(""));

        gridLayout_2->addWidget(btnCreate, 30, 0, 1, 1);

        verticalSpacer_3 = new QSpacerItem(20, 10, QSizePolicy::Minimum, QSizePolicy::Preferred);

        gridLayout_2->addItem(verticalSpacer_3, 5, 0, 1, 1);

        lblHintDesc = new QLabel(rightBox);
        lblHintDesc->setObjectName("lblHintDesc");
        QFont font6;
        font6.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font6.setPointSize(12);
        lblHintDesc->setFont(font6);
        lblHintDesc->setStyleSheet(QString::fromUtf8("color: rgba(0, 0, 0, 120);"));

        gridLayout_2->addWidget(lblHintDesc, 22, 0, 1, 3);

        lblMasterPassword2 = new QLabel(rightBox);
        lblMasterPassword2->setObjectName("lblMasterPassword2");
        lblMasterPassword2->setFont(font);
        lblMasterPassword2->setStyleSheet(QString::fromUtf8("color:rgba(0, 0, 0, 200)"));

        gridLayout_2->addWidget(lblMasterPassword2, 18, 0, 1, 2);

        lblPassDesc = new QLabel(rightBox);
        lblPassDesc->setObjectName("lblPassDesc");
        lblPassDesc->setFont(font6);
        lblPassDesc->setStyleSheet(QString::fromUtf8("color: rgba(0, 0, 0, 120);"));

        gridLayout_2->addWidget(lblPassDesc, 15, 0, 1, 3);

        lineEdit_Email = new QLineEdit(rightBox);
        lineEdit_Email->setObjectName("lineEdit_Email");
        lineEdit_Email->setMinimumSize(QSize(350, 30));
        lineEdit_Email->setFont(font4);
        lineEdit_Email->setStyleSheet(QString::fromUtf8("background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px"));
        lineEdit_Email->setEchoMode(QLineEdit::Normal);

        gridLayout_2->addWidget(lineEdit_Email, 8, 0, 1, 2);

        lineEdit_MastPassword = new QLineEdit(rightBox);
        lineEdit_MastPassword->setObjectName("lineEdit_MastPassword");
        lineEdit_MastPassword->setMinimumSize(QSize(350, 30));
        lineEdit_MastPassword->setFont(font4);
        lineEdit_MastPassword->setStyleSheet(QString::fromUtf8("background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px"));
        lineEdit_MastPassword->setEchoMode(QLineEdit::Password);

        gridLayout_2->addWidget(lineEdit_MastPassword, 14, 0, 1, 2);

        lblNew = new QLabel(rightBox);
        lblNew->setObjectName("lblNew");
        lblNew->setMinimumSize(QSize(95, 32));
        lblNew->setFont(font);
        lblNew->setStyleSheet(QString::fromUtf8("color: rgba(0, 0, 0, 170);"));

        gridLayout_2->addWidget(lblNew, 1, 2, 1, 1);

        lineEdit_Name = new QLineEdit(rightBox);
        lineEdit_Name->setObjectName("lineEdit_Name");
        lineEdit_Name->setMinimumSize(QSize(350, 30));
        lineEdit_Name->setFont(font4);
        lineEdit_Name->setStyleSheet(QString::fromUtf8("background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px"));
        lineEdit_Name->setEchoMode(QLineEdit::Normal);

        gridLayout_2->addWidget(lineEdit_Name, 10, 0, 1, 1);

        lblCreate = new QLabel(rightBox);
        lblCreate->setObjectName("lblCreate");
        QFont font7;
        font7.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font7.setPointSize(40);
        font7.setBold(true);
        font7.setItalic(false);
        font7.setUnderline(false);
        font7.setStrikeOut(false);
        lblCreate->setFont(font7);
        lblCreate->setStyleSheet(QString::fromUtf8("color: rgba(0, 0, 0, 220);"));

        gridLayout_2->addWidget(lblCreate, 3, 0, 2, 4);

        lblName = new QLabel(rightBox);
        lblName->setObjectName("lblName");
        lblName->setFont(font);
        lblName->setStyleSheet(QString::fromUtf8("color:rgba(0, 0, 0, 200)"));

        gridLayout_2->addWidget(lblName, 9, 0, 1, 1);

        lineEdit_MastPassword2 = new QLineEdit(rightBox);
        lineEdit_MastPassword2->setObjectName("lineEdit_MastPassword2");
        lineEdit_MastPassword2->setMinimumSize(QSize(350, 30));
        lineEdit_MastPassword2->setFont(font4);
        lineEdit_MastPassword2->setStyleSheet(QString::fromUtf8("background-color: rgba(94, 65, 87, 100);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px"));
        lineEdit_MastPassword2->setEchoMode(QLineEdit::Password);

        gridLayout_2->addWidget(lineEdit_MastPassword2, 19, 0, 1, 1);

        verticalSpacer_2 = new QSpacerItem(20, 20, QSizePolicy::Minimum, QSizePolicy::Preferred);

        gridLayout_2->addItem(verticalSpacer_2, 28, 0, 1, 1);

        btnLogin = new QPushButton(rightBox);
        btnLogin->setObjectName("btnLogin");
        btnLogin->setMinimumSize(QSize(110, 30));
        QFont font8;
        font8.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font8.setPointSize(13);
        font8.setItalic(false);
        btnLogin->setFont(font8);
        btnLogin->setStyleSheet(QString::fromUtf8(""));

        gridLayout_2->addWidget(btnLogin, 1, 3, 1, 1);

        verticalSpacer_6 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_2->addItem(verticalSpacer_6, 32, 0, 1, 1);

        passStrengthBar = new QProgressBar(rightBox);
        passStrengthBar->setObjectName("passStrengthBar");
        passStrengthBar->setStyleSheet(QString::fromUtf8("background-color: rgb(110, 77, 103);"));
        passStrengthBar->setValue(24);
        passStrengthBar->setTextVisible(true);
        passStrengthBar->setInvertedAppearance(false);

        gridLayout_2->addWidget(passStrengthBar, 17, 0, 1, 1);

        lblEmail = new QLabel(rightBox);
        lblEmail->setObjectName("lblEmail");
        lblEmail->setFont(font);
        lblEmail->setStyleSheet(QString::fromUtf8("color:rgba(0, 0, 0, 200)"));

        gridLayout_2->addWidget(lblEmail, 6, 0, 1, 1);

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
        lineEdit_PassHint->setPlaceholderText(QString());
        lblMasterPassword->setText(QCoreApplication::translate("Form", "<html><head/><body><p>master password <span style=\" font-family:'Arial'; font-size:9pt; color:#a3a3a3;\">(required)</span></p></body></html>", nullptr));
        lblPasswordHint->setText(QCoreApplication::translate("Form", "<html><head/><body><p>master password hint <span style=\" font-family:'Arial'; font-size:9pt; color:#a3a3a3;\">(optional)</span></p></body></html>", nullptr));
        btnCreate->setText(QCoreApplication::translate("Form", "create account", nullptr));
        lblHintDesc->setText(QCoreApplication::translate("Form", "can help you remeber your master password if forgotten", nullptr));
        lblMasterPassword2->setText(QCoreApplication::translate("Form", "<html><head/><body><p>re-type master password <span style=\" font-family:'Arial'; font-size:9pt; color:#a3a3a3;\">(required)</span></p></body></html>", nullptr));
        lblPassDesc->setText(QCoreApplication::translate("Form", "used to access your pass.me. \n"
"NOTE: if forgotten, cannot be recovered", nullptr));
        lineEdit_Email->setPlaceholderText(QString());
        lineEdit_MastPassword->setPlaceholderText(QString());
        lblNew->setText(QCoreApplication::translate("Form", "exisiting user?", nullptr));
        lineEdit_Name->setPlaceholderText(QString());
        lblCreate->setText(QCoreApplication::translate("Form", "create your pass.me", nullptr));
        lblName->setText(QCoreApplication::translate("Form", "<html><head/><body><p>name <span style=\" font-family:'Arial'; font-size:9pt; color:#a3a3a3;\">(optional)</span></p></body></html>", nullptr));
        lineEdit_MastPassword2->setPlaceholderText(QString());
        btnLogin->setText(QCoreApplication::translate("Form", "log in", nullptr));
        lblEmail->setText(QCoreApplication::translate("Form", "<html><head/><body><p>email <span style=\" font-family:'Arial'; font-size:9pt; color:#a3a3a3;\">(required)</span></p></body></html>", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CREATE_ACC_SCREEN_H

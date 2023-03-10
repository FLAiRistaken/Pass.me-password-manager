/********************************************************************************
** Form generated from reading UI file 'new_login_screen.ui'
**
** Created by: Qt User Interface Compiler version 6.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_NEW_LOGIN_SCREEN_H
#define UI_NEW_LOGIN_SCREEN_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Form
{
public:
    QWidget *widget;
    QGridLayout *gridLayout_2;
    QPushButton *btnBack;
    QLabel *lblNewItemTitle;
    QFrame *divider;
    QFrame *text_fields_group;
    QGridLayout *gridLayout;
    QTextEdit *textEdit;
    QToolButton *btnSave;
    QLabel *lblEmail_5;
    QFrame *main_data_entry_group;
    QGridLayout *gridLayout_3;
    QLineEdit *lineEdit_Name_4;
    QLabel *lblEmail_2;
    QLineEdit *lineEdit_Name_3;
    QLineEdit *lineEdit_Name_2;
    QLabel *lblEmail;
    QLabel *lblEmail_3;
    QLineEdit *lineEdit_Name;
    QLabel *lblEmail_4;
    QComboBox *comboFolders;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName("Form");
        Form->resize(194, 0);
        widget = new QWidget(Form);
        widget->setObjectName("widget");
        widget->setGeometry(QRect(30, 20, 500, 700));
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(widget->sizePolicy().hasHeightForWidth());
        widget->setSizePolicy(sizePolicy);
        widget->setMinimumSize(QSize(500, 700));
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
"QFrame#text_fields_group {\n"
"	padding: 5px;\n"
"}\n"
"QFrame#main_data_entry_group{\n"
"	background-color: rgba(70, 70, 70, 255);\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
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
        btnBack = new QPushButton(widget);
        btnBack->setObjectName("btnBack");
        QSizePolicy sizePolicy1(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(btnBack->sizePolicy().hasHeightForWidth());
        btnBack->setSizePolicy(sizePolicy1);
        btnBack->setMinimumSize(QSize(0, 0));
        btnBack->setMaximumSize(QSize(18, 21));
        QFont font;
        font.setFamilies({QString::fromUtf8("Waseem")});
        font.setPointSize(25);
        btnBack->setFont(font);
        btnBack->setStyleSheet(QString::fromUtf8("border: none;\n"
""));

        gridLayout_2->addWidget(btnBack, 1, 0, 1, 2);

        lblNewItemTitle = new QLabel(widget);
        lblNewItemTitle->setObjectName("lblNewItemTitle");
        QSizePolicy sizePolicy2(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(lblNewItemTitle->sizePolicy().hasHeightForWidth());
        lblNewItemTitle->setSizePolicy(sizePolicy2);
        lblNewItemTitle->setMaximumSize(QSize(364, 112));
        QFont font1;
        font1.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font1.setPointSize(31);
        lblNewItemTitle->setFont(font1);
        lblNewItemTitle->setStyleSheet(QString::fromUtf8("color: rgba(255,255,255, 220);"));
        lblNewItemTitle->setTextFormat(Qt::RichText);

        gridLayout_2->addWidget(lblNewItemTitle, 2, 0, 1, 2, Qt::AlignLeft);

        divider = new QFrame(widget);
        divider->setObjectName("divider");
        QSizePolicy sizePolicy3(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(divider->sizePolicy().hasHeightForWidth());
        divider->setSizePolicy(sizePolicy3);
        divider->setMaximumSize(QSize(16777215, 1));
        divider->setStyleSheet(QString::fromUtf8("background-color: rgba(255, 255, 255, 80);\n"
"border: none;"));
        divider->setFrameShape(QFrame::HLine);
        divider->setFrameShadow(QFrame::Sunken);

        gridLayout_2->addWidget(divider, 4, 0, 1, 2);

        text_fields_group = new QFrame(widget);
        text_fields_group->setObjectName("text_fields_group");
        text_fields_group->setMinimumSize(QSize(430, 351));
        text_fields_group->setStyleSheet(QString::fromUtf8(""));
        gridLayout = new QGridLayout(text_fields_group);
        gridLayout->setObjectName("gridLayout");
        textEdit = new QTextEdit(text_fields_group);
        textEdit->setObjectName("textEdit");
        textEdit->setStyleSheet(QString::fromUtf8("background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px;"));

        gridLayout->addWidget(textEdit, 4, 0, 1, 1);

        btnSave = new QToolButton(text_fields_group);
        btnSave->setObjectName("btnSave");
        btnSave->setEnabled(true);
        QSizePolicy sizePolicy4(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy4.setHorizontalStretch(0);
        sizePolicy4.setVerticalStretch(0);
        sizePolicy4.setHeightForWidth(btnSave->sizePolicy().hasHeightForWidth());
        btnSave->setSizePolicy(sizePolicy4);
        btnSave->setMaximumSize(QSize(16777215, 75));
        QFont font2;
        font2.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font2.setPointSize(16);
        btnSave->setFont(font2);
        btnSave->setLayoutDirection(Qt::LeftToRight);
        btnSave->setStyleSheet(QString::fromUtf8("background-color:rgba(148, 105, 141, 220);"));
        btnSave->setPopupMode(QToolButton::InstantPopup);
        btnSave->setToolButtonStyle(Qt::ToolButtonTextBesideIcon);
        btnSave->setAutoRaise(false);
        btnSave->setArrowType(Qt::NoArrow);

        gridLayout->addWidget(btnSave, 6, 0, 1, 1);

        lblEmail_5 = new QLabel(text_fields_group);
        lblEmail_5->setObjectName("lblEmail_5");
        lblEmail_5->setMinimumSize(QSize(0, 10));
        lblEmail_5->setMaximumSize(QSize(16777215, 10));
        QFont font3;
        font3.setFamilies({QString::fromUtf8("Nexa-Trial")});
        lblEmail_5->setFont(font3);
        lblEmail_5->setStyleSheet(QString::fromUtf8("background-color: rgba(255, 255, 255, 0);"));

        gridLayout->addWidget(lblEmail_5, 3, 0, 1, 1);

        main_data_entry_group = new QFrame(text_fields_group);
        main_data_entry_group->setObjectName("main_data_entry_group");
        main_data_entry_group->setMinimumSize(QSize(200, 200));
        main_data_entry_group->setStyleSheet(QString::fromUtf8(""));
        main_data_entry_group->setFrameShape(QFrame::StyledPanel);
        main_data_entry_group->setFrameShadow(QFrame::Raised);
        gridLayout_3 = new QGridLayout(main_data_entry_group);
        gridLayout_3->setObjectName("gridLayout_3");
        lineEdit_Name_4 = new QLineEdit(main_data_entry_group);
        lineEdit_Name_4->setObjectName("lineEdit_Name_4");
        lineEdit_Name_4->setMinimumSize(QSize(0, 30));
        QFont font4;
        font4.setFamilies({QString::fromUtf8(".AppleSystemUIFont")});
        lineEdit_Name_4->setFont(font4);
        lineEdit_Name_4->setStyleSheet(QString::fromUtf8("background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px"));
        lineEdit_Name_4->setEchoMode(QLineEdit::Normal);

        gridLayout_3->addWidget(lineEdit_Name_4, 3, 0, 1, 1);

        lblEmail_2 = new QLabel(main_data_entry_group);
        lblEmail_2->setObjectName("lblEmail_2");
        lblEmail_2->setMinimumSize(QSize(0, 10));
        lblEmail_2->setMaximumSize(QSize(16777215, 12));
        lblEmail_2->setFont(font3);
        lblEmail_2->setStyleSheet(QString::fromUtf8("background-color: rgba(255, 255, 255, 0);"));

        gridLayout_3->addWidget(lblEmail_2, 2, 0, 1, 1);

        lineEdit_Name_3 = new QLineEdit(main_data_entry_group);
        lineEdit_Name_3->setObjectName("lineEdit_Name_3");
        lineEdit_Name_3->setMinimumSize(QSize(0, 30));
        lineEdit_Name_3->setFont(font4);
        lineEdit_Name_3->setStyleSheet(QString::fromUtf8("background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px"));
        lineEdit_Name_3->setEchoMode(QLineEdit::Normal);

        gridLayout_3->addWidget(lineEdit_Name_3, 5, 0, 1, 1);

        lineEdit_Name_2 = new QLineEdit(main_data_entry_group);
        lineEdit_Name_2->setObjectName("lineEdit_Name_2");
        lineEdit_Name_2->setMinimumSize(QSize(0, 30));
        lineEdit_Name_2->setFont(font4);
        lineEdit_Name_2->setStyleSheet(QString::fromUtf8("background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px"));
        lineEdit_Name_2->setEchoMode(QLineEdit::Normal);

        gridLayout_3->addWidget(lineEdit_Name_2, 1, 0, 1, 1);

        lblEmail = new QLabel(main_data_entry_group);
        lblEmail->setObjectName("lblEmail");
        lblEmail->setMinimumSize(QSize(0, 10));
        lblEmail->setMaximumSize(QSize(16777215, 10));
        lblEmail->setFont(font3);
        lblEmail->setStyleSheet(QString::fromUtf8("background-color: rgba(255, 255, 255, 0);"));

        gridLayout_3->addWidget(lblEmail, 0, 0, 1, 1);

        lblEmail_3 = new QLabel(main_data_entry_group);
        lblEmail_3->setObjectName("lblEmail_3");
        lblEmail_3->setMinimumSize(QSize(0, 10));
        lblEmail_3->setMaximumSize(QSize(16777215, 10));
        lblEmail_3->setFont(font3);
        lblEmail_3->setStyleSheet(QString::fromUtf8("background-color: rgba(255, 255, 255, 0);"));

        gridLayout_3->addWidget(lblEmail_3, 4, 0, 1, 1);


        gridLayout->addWidget(main_data_entry_group, 2, 0, 1, 1);

        lineEdit_Name = new QLineEdit(text_fields_group);
        lineEdit_Name->setObjectName("lineEdit_Name");
        lineEdit_Name->setMinimumSize(QSize(0, 40));
        lineEdit_Name->setFont(font4);
        lineEdit_Name->setStyleSheet(QString::fromUtf8("background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px"));
        lineEdit_Name->setEchoMode(QLineEdit::Normal);

        gridLayout->addWidget(lineEdit_Name, 1, 0, 1, 1);

        lblEmail_4 = new QLabel(text_fields_group);
        lblEmail_4->setObjectName("lblEmail_4");
        lblEmail_4->setMinimumSize(QSize(0, 10));
        lblEmail_4->setMaximumSize(QSize(16777215, 10));
        lblEmail_4->setFont(font3);
        lblEmail_4->setStyleSheet(QString::fromUtf8("background-color: rgba(255, 255, 255, 0);"));

        gridLayout->addWidget(lblEmail_4, 0, 0, 1, 1);

        comboFolders = new QComboBox(text_fields_group);
        comboFolders->addItem(QString());
        comboFolders->addItem(QString());
        comboFolders->addItem(QString());
        comboFolders->addItem(QString());
        comboFolders->addItem(QString());
        comboFolders->addItem(QString());
        comboFolders->addItem(QString());
        comboFolders->addItem(QString());
        comboFolders->addItem(QString());
        comboFolders->addItem(QString());
        comboFolders->setObjectName("comboFolders");
        QSizePolicy sizePolicy5(QSizePolicy::Preferred, QSizePolicy::Expanding);
        sizePolicy5.setHorizontalStretch(0);
        sizePolicy5.setVerticalStretch(0);
        sizePolicy5.setHeightForWidth(comboFolders->sizePolicy().hasHeightForWidth());
        comboFolders->setSizePolicy(sizePolicy5);
        comboFolders->setMaximumSize(QSize(16777215, 30));
        comboFolders->setFont(font3);
        comboFolders->setStyleSheet(QString::fromUtf8("border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:6px;\n"
"color: rgba(255, 255, 255, 200);"));

        gridLayout->addWidget(comboFolders, 5, 0, 1, 1);


        gridLayout_2->addWidget(text_fields_group, 5, 0, 1, 2);


        retranslateUi(Form);

        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QCoreApplication::translate("Form", "Form", nullptr));
        btnBack->setText(QCoreApplication::translate("Form", "<", nullptr));
        lblNewItemTitle->setText(QCoreApplication::translate("Form", "<html><head/><body><p><span style=\" font-weight:700;\">New Login</span></p></body></html>", nullptr));
        btnSave->setText(QCoreApplication::translate("Form", "save", nullptr));
        lblEmail_5->setText(QCoreApplication::translate("Form", "notes", nullptr));
        lineEdit_Name_4->setPlaceholderText(QString());
        lblEmail_2->setText(QCoreApplication::translate("Form", "password", nullptr));
        lineEdit_Name_3->setPlaceholderText(QString());
        lineEdit_Name_2->setPlaceholderText(QString());
        lblEmail->setText(QCoreApplication::translate("Form", "email / username", nullptr));
        lblEmail_3->setText(QCoreApplication::translate("Form", "website", nullptr));
        lineEdit_Name->setPlaceholderText(QString());
        lblEmail_4->setText(QCoreApplication::translate("Form", "name", nullptr));
        comboFolders->setItemText(0, QCoreApplication::translate("Form", "No folder", nullptr));
        comboFolders->setItemText(1, QCoreApplication::translate("Form", "Business", nullptr));
        comboFolders->setItemText(2, QCoreApplication::translate("Form", "Email", nullptr));
        comboFolders->setItemText(3, QCoreApplication::translate("Form", "Entertainment", nullptr));
        comboFolders->setItemText(4, QCoreApplication::translate("Form", "Education", nullptr));
        comboFolders->setItemText(5, QCoreApplication::translate("Form", "Encrypted notes", nullptr));
        comboFolders->setItemText(6, QCoreApplication::translate("Form", "Finance", nullptr));
        comboFolders->setItemText(7, QCoreApplication::translate("Form", "Games", nullptr));
        comboFolders->setItemText(8, QCoreApplication::translate("Form", "Shopping", nullptr));
        comboFolders->setItemText(9, QCoreApplication::translate("Form", "Social", nullptr));

    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_NEW_LOGIN_SCREEN_H

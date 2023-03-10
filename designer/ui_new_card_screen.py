/********************************************************************************
** Form generated from reading UI file 'new_card_screen.ui'
**
** Created by: Qt User Interface Compiler version 6.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_NEW_CARD_SCREEN_H
#define UI_NEW_CARD_SCREEN_H

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
    QLabel *lblNewCardTitle;
    QFrame *divider;
    QFrame *text_fields_group;
    QGridLayout *gridLayout;
    QTextEdit *textEdit_Notes;
    QToolButton *btnSave;
    QLabel *lblNotes;
    QFrame *main_data_entry_group;
    QGridLayout *gridLayout_3;
    QComboBox *comboBrand;
    QLabel *lblCvv;
    QLabel *lblExpirationDate;
    QLabel *lblCardNumber;
    QComboBox *comboExpirYear;
    QLineEdit *lineEdit_CardholderName;
    QLineEdit *lineEdit_CardNumber;
    QComboBox *comboExpirMonth;
    QLineEdit *lineEdit_CVV;
    QLabel *lblCardholderName;
    QLabel *lblBrand;
    QLineEdit *lineEdit_Name;
    QLabel *lblName;
    QComboBox *comboFolders;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName("Form");
        Form->resize(535, 811);
        widget = new QWidget(Form);
        widget->setObjectName("widget");
        widget->setGeometry(QRect(30, 10, 500, 800));
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(widget->sizePolicy().hasHeightForWidth());
        widget->setSizePolicy(sizePolicy);
        widget->setMinimumSize(QSize(500, 800));
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

        lblNewCardTitle = new QLabel(widget);
        lblNewCardTitle->setObjectName("lblNewCardTitle");
        QSizePolicy sizePolicy2(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(lblNewCardTitle->sizePolicy().hasHeightForWidth());
        lblNewCardTitle->setSizePolicy(sizePolicy2);
        lblNewCardTitle->setMaximumSize(QSize(364, 112));
        QFont font1;
        font1.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font1.setPointSize(31);
        lblNewCardTitle->setFont(font1);
        lblNewCardTitle->setStyleSheet(QString::fromUtf8("color: rgba(255,255,255, 220);"));
        lblNewCardTitle->setTextFormat(Qt::RichText);

        gridLayout_2->addWidget(lblNewCardTitle, 2, 0, 1, 2, Qt::AlignLeft);

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
        textEdit_Notes = new QTextEdit(text_fields_group);
        textEdit_Notes->setObjectName("textEdit_Notes");
        textEdit_Notes->setStyleSheet(QString::fromUtf8("background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px;"));

        gridLayout->addWidget(textEdit_Notes, 4, 0, 1, 1);

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

        lblNotes = new QLabel(text_fields_group);
        lblNotes->setObjectName("lblNotes");
        lblNotes->setMinimumSize(QSize(0, 10));
        lblNotes->setMaximumSize(QSize(16777215, 10));
        QFont font3;
        font3.setFamilies({QString::fromUtf8("Nexa-Trial")});
        lblNotes->setFont(font3);
        lblNotes->setStyleSheet(QString::fromUtf8("background-color: rgba(255, 255, 255, 0);"));

        gridLayout->addWidget(lblNotes, 3, 0, 1, 1);

        main_data_entry_group = new QFrame(text_fields_group);
        main_data_entry_group->setObjectName("main_data_entry_group");
        main_data_entry_group->setMinimumSize(QSize(200, 340));
        main_data_entry_group->setStyleSheet(QString::fromUtf8(""));
        main_data_entry_group->setFrameShape(QFrame::StyledPanel);
        main_data_entry_group->setFrameShadow(QFrame::Raised);
        gridLayout_3 = new QGridLayout(main_data_entry_group);
        gridLayout_3->setObjectName("gridLayout_3");
        comboBrand = new QComboBox(main_data_entry_group);
        comboBrand->addItem(QString());
        comboBrand->addItem(QString());
        comboBrand->addItem(QString());
        comboBrand->addItem(QString());
        comboBrand->addItem(QString());
        comboBrand->setObjectName("comboBrand");
        QSizePolicy sizePolicy5(QSizePolicy::Preferred, QSizePolicy::Expanding);
        sizePolicy5.setHorizontalStretch(0);
        sizePolicy5.setVerticalStretch(0);
        sizePolicy5.setHeightForWidth(comboBrand->sizePolicy().hasHeightForWidth());
        comboBrand->setSizePolicy(sizePolicy5);
        comboBrand->setMaximumSize(QSize(16777215, 30));
        comboBrand->setFont(font3);
        comboBrand->setStyleSheet(QString::fromUtf8("border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:6px;\n"
"color: rgba(255, 255, 255, 200);"));
        comboBrand->setFrame(true);

        gridLayout_3->addWidget(comboBrand, 8, 0, 1, 2);

        lblCvv = new QLabel(main_data_entry_group);
        lblCvv->setObjectName("lblCvv");
        lblCvv->setMinimumSize(QSize(0, 10));
        lblCvv->setMaximumSize(QSize(16777215, 10));
        lblCvv->setFont(font3);
        lblCvv->setStyleSheet(QString::fromUtf8("background-color: rgba(255, 255, 255, 0);"));

        gridLayout_3->addWidget(lblCvv, 9, 0, 1, 1);

        lblExpirationDate = new QLabel(main_data_entry_group);
        lblExpirationDate->setObjectName("lblExpirationDate");
        lblExpirationDate->setMinimumSize(QSize(0, 10));
        lblExpirationDate->setMaximumSize(QSize(16777215, 12));
        lblExpirationDate->setFont(font3);
        lblExpirationDate->setStyleSheet(QString::fromUtf8("background-color: rgba(255, 255, 255, 0);"));

        gridLayout_3->addWidget(lblExpirationDate, 4, 0, 1, 1);

        lblCardNumber = new QLabel(main_data_entry_group);
        lblCardNumber->setObjectName("lblCardNumber");
        lblCardNumber->setMinimumSize(QSize(0, 10));
        lblCardNumber->setMaximumSize(QSize(16777215, 12));
        lblCardNumber->setFont(font3);
        lblCardNumber->setStyleSheet(QString::fromUtf8("background-color: rgba(255, 255, 255, 0);"));

        gridLayout_3->addWidget(lblCardNumber, 2, 0, 1, 1);

        comboExpirYear = new QComboBox(main_data_entry_group);
        comboExpirYear->addItem(QString());
        comboExpirYear->addItem(QString());
        comboExpirYear->addItem(QString());
        comboExpirYear->addItem(QString());
        comboExpirYear->addItem(QString());
        comboExpirYear->addItem(QString());
        comboExpirYear->addItem(QString());
        comboExpirYear->addItem(QString());
        comboExpirYear->setObjectName("comboExpirYear");
        sizePolicy5.setHeightForWidth(comboExpirYear->sizePolicy().hasHeightForWidth());
        comboExpirYear->setSizePolicy(sizePolicy5);
        comboExpirYear->setMaximumSize(QSize(16777215, 30));
        comboExpirYear->setFont(font3);
        comboExpirYear->setStyleSheet(QString::fromUtf8("border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:6px;\n"
"color: rgba(255, 255, 255, 200);"));

        gridLayout_3->addWidget(comboExpirYear, 6, 1, 1, 1);

        lineEdit_CardholderName = new QLineEdit(main_data_entry_group);
        lineEdit_CardholderName->setObjectName("lineEdit_CardholderName");
        lineEdit_CardholderName->setMinimumSize(QSize(0, 30));
        QFont font4;
        font4.setFamilies({QString::fromUtf8(".AppleSystemUIFont")});
        lineEdit_CardholderName->setFont(font4);
        lineEdit_CardholderName->setStyleSheet(QString::fromUtf8("background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px"));
        lineEdit_CardholderName->setEchoMode(QLineEdit::Normal);

        gridLayout_3->addWidget(lineEdit_CardholderName, 1, 0, 1, 2);

        lineEdit_CardNumber = new QLineEdit(main_data_entry_group);
        lineEdit_CardNumber->setObjectName("lineEdit_CardNumber");
        lineEdit_CardNumber->setMinimumSize(QSize(0, 30));
        lineEdit_CardNumber->setFont(font4);
        lineEdit_CardNumber->setStyleSheet(QString::fromUtf8("background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px"));
        lineEdit_CardNumber->setMaxLength(16);
        lineEdit_CardNumber->setEchoMode(QLineEdit::Normal);

        gridLayout_3->addWidget(lineEdit_CardNumber, 3, 0, 1, 2);

        comboExpirMonth = new QComboBox(main_data_entry_group);
        comboExpirMonth->addItem(QString());
        comboExpirMonth->addItem(QString());
        comboExpirMonth->addItem(QString());
        comboExpirMonth->addItem(QString());
        comboExpirMonth->addItem(QString());
        comboExpirMonth->addItem(QString());
        comboExpirMonth->addItem(QString());
        comboExpirMonth->addItem(QString());
        comboExpirMonth->addItem(QString());
        comboExpirMonth->addItem(QString());
        comboExpirMonth->addItem(QString());
        comboExpirMonth->addItem(QString());
        comboExpirMonth->addItem(QString());
        comboExpirMonth->setObjectName("comboExpirMonth");
        sizePolicy5.setHeightForWidth(comboExpirMonth->sizePolicy().hasHeightForWidth());
        comboExpirMonth->setSizePolicy(sizePolicy5);
        comboExpirMonth->setMaximumSize(QSize(16777215, 30));
        comboExpirMonth->setFont(font3);
        comboExpirMonth->setStyleSheet(QString::fromUtf8("border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:6px;\n"
"color: rgba(255, 255, 255, 200);"));
        comboExpirMonth->setFrame(true);

        gridLayout_3->addWidget(comboExpirMonth, 6, 0, 1, 1);

        lineEdit_CVV = new QLineEdit(main_data_entry_group);
        lineEdit_CVV->setObjectName("lineEdit_CVV");
        lineEdit_CVV->setMinimumSize(QSize(0, 30));
        lineEdit_CVV->setFont(font4);
        lineEdit_CVV->setStyleSheet(QString::fromUtf8("background-color: rgba(43, 43, 43, 200);\n"
"border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px"));
        lineEdit_CVV->setMaxLength(3);
        lineEdit_CVV->setEchoMode(QLineEdit::Normal);

        gridLayout_3->addWidget(lineEdit_CVV, 10, 0, 1, 2);

        lblCardholderName = new QLabel(main_data_entry_group);
        lblCardholderName->setObjectName("lblCardholderName");
        lblCardholderName->setMinimumSize(QSize(0, 10));
        lblCardholderName->setMaximumSize(QSize(16777215, 10));
        lblCardholderName->setFont(font3);
        lblCardholderName->setStyleSheet(QString::fromUtf8("background-color: rgba(255, 255, 255, 0);"));

        gridLayout_3->addWidget(lblCardholderName, 0, 0, 1, 1);

        lblBrand = new QLabel(main_data_entry_group);
        lblBrand->setObjectName("lblBrand");
        lblBrand->setMinimumSize(QSize(0, 10));
        lblBrand->setMaximumSize(QSize(16777215, 12));
        lblBrand->setFont(font3);
        lblBrand->setStyleSheet(QString::fromUtf8("background-color: rgba(255, 255, 255, 0);"));

        gridLayout_3->addWidget(lblBrand, 7, 0, 1, 1);


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

        lblName = new QLabel(text_fields_group);
        lblName->setObjectName("lblName");
        lblName->setMinimumSize(QSize(0, 10));
        lblName->setMaximumSize(QSize(16777215, 10));
        lblName->setFont(font3);
        lblName->setStyleSheet(QString::fromUtf8("background-color: rgba(255, 255, 255, 0);"));

        gridLayout->addWidget(lblName, 0, 0, 1, 1);

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
        lblNewCardTitle->setText(QCoreApplication::translate("Form", "<html><head/><body><p><span style=\" font-weight:700;\">New Bank Card</span></p></body></html>", nullptr));
        btnSave->setText(QCoreApplication::translate("Form", "save", nullptr));
        lblNotes->setText(QCoreApplication::translate("Form", "notes", nullptr));
        comboBrand->setItemText(0, QCoreApplication::translate("Form", "- Select -", nullptr));
        comboBrand->setItemText(1, QCoreApplication::translate("Form", "Visa", nullptr));
        comboBrand->setItemText(2, QCoreApplication::translate("Form", "Mastercard", nullptr));
        comboBrand->setItemText(3, QCoreApplication::translate("Form", "American Express", nullptr));
        comboBrand->setItemText(4, QCoreApplication::translate("Form", "Other", nullptr));

        lblCvv->setText(QCoreApplication::translate("Form", "CVV", nullptr));
        lblExpirationDate->setText(QCoreApplication::translate("Form", "expiration date", nullptr));
        lblCardNumber->setText(QCoreApplication::translate("Form", "card number", nullptr));
        comboExpirYear->setItemText(0, QCoreApplication::translate("Form", "- Select -", nullptr));
        comboExpirYear->setItemText(1, QCoreApplication::translate("Form", "2023", nullptr));
        comboExpirYear->setItemText(2, QCoreApplication::translate("Form", "2024", nullptr));
        comboExpirYear->setItemText(3, QCoreApplication::translate("Form", "2025", nullptr));
        comboExpirYear->setItemText(4, QCoreApplication::translate("Form", "2026", nullptr));
        comboExpirYear->setItemText(5, QCoreApplication::translate("Form", "2027", nullptr));
        comboExpirYear->setItemText(6, QCoreApplication::translate("Form", "2028", nullptr));
        comboExpirYear->setItemText(7, QCoreApplication::translate("Form", "2029", nullptr));

        lineEdit_CardholderName->setPlaceholderText(QString());
        lineEdit_CardNumber->setPlaceholderText(QString());
        comboExpirMonth->setItemText(0, QCoreApplication::translate("Form", "- Select -", nullptr));
        comboExpirMonth->setItemText(1, QCoreApplication::translate("Form", "01 - January", nullptr));
        comboExpirMonth->setItemText(2, QCoreApplication::translate("Form", "02 - February", nullptr));
        comboExpirMonth->setItemText(3, QCoreApplication::translate("Form", "03 - March", nullptr));
        comboExpirMonth->setItemText(4, QCoreApplication::translate("Form", "04 - April", nullptr));
        comboExpirMonth->setItemText(5, QCoreApplication::translate("Form", "05 - May", nullptr));
        comboExpirMonth->setItemText(6, QCoreApplication::translate("Form", "06 - June", nullptr));
        comboExpirMonth->setItemText(7, QCoreApplication::translate("Form", "07 - July", nullptr));
        comboExpirMonth->setItemText(8, QCoreApplication::translate("Form", "08 - August", nullptr));
        comboExpirMonth->setItemText(9, QCoreApplication::translate("Form", "09 - September", nullptr));
        comboExpirMonth->setItemText(10, QCoreApplication::translate("Form", "10 - October", nullptr));
        comboExpirMonth->setItemText(11, QCoreApplication::translate("Form", "11 - November", nullptr));
        comboExpirMonth->setItemText(12, QCoreApplication::translate("Form", "12 - December", nullptr));

        lineEdit_CVV->setPlaceholderText(QString());
        lblCardholderName->setText(QCoreApplication::translate("Form", "cardholder name", nullptr));
        lblBrand->setText(QCoreApplication::translate("Form", "brand", nullptr));
        lineEdit_Name->setPlaceholderText(QString());
        lblName->setText(QCoreApplication::translate("Form", "name", nullptr));
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

#endif // UI_NEW_CARD_SCREEN_H

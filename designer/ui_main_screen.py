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
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
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
    QToolButton *btnProfile;
    QSpacerItem *verticalSpacer_2;
    QPushButton *btnAll_Items;
    QPushButton *btnFavorites;
    QPushButton *btnGenerator;
    QFrame *line;
    QToolButton *btnTags;
    QPushButton *btnRecently_Deleted;
    QSpacerItem *verticalSpacer;
    QWidget *gridLayoutWidget;
    QGridLayout *gridLayout_4;
    QWidget *right_box;
    QGridLayout *gridLayout_2;
    QWidget *wItemBox;
    QWidget *middle_box;
    QVBoxLayout *verticalLayout_3;
    QComboBox *comboCategories;
    QListWidget *lvItems;
    QWidget *top_box;
    QHBoxLayout *horizontalLayout;
    QPushButton *btnNew;
    QFrame *line_2;
    QHBoxLayout *hSearch;
    QWidget *widget_2;
    QGridLayout *gridLayout_3;
    QLabel *label;
    QLineEdit *lineEdit_Search;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName("Form");
        Form->resize(194, 0);
        Form->setStyleSheet(QString::fromUtf8(""));
        gridLayout = new QGridLayout(Form);
        gridLayout->setObjectName("gridLayout");
        widget = new QWidget(Form);
        widget->setObjectName("widget");
        widget->setStyleSheet(QString::fromUtf8("QWidget#left_box{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, 		stop:0 rgba(0, 0, 0, 255), stop:1 rgba(92, 61, 88, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"QWidget#top_box{\n"
"	background-color: rgba(32, 32, 32, 255);\n"
"	border-top-right-radius: 10px\n"
"}\n"
"QWidget#middle_box{\n"
"	background-color: rgba(32, 32, 32, 255);\n"
"	border-color: rgb(0, 0, 0);\n"
"}\n"
"QWidget#right_box{\n"
"	background-color: rgba(32, 32, 32, 255);\n"
"	border-bottom-right-radius: 10px\n"
"}\n"
"QPushButton#btnNew{\n"
"	background-color:rgba(148, 105, 141, 255);\n"
"	color:rgba(255, 255, 255, 220);\n"
"	border-radius:5px;\n"
"}\n"
"QListView{\n"
"	border-radius:10px;\n"
"}\n"
"QToolButton#btnProfile{\n"
"	border:none;\n"
"	color:rgba(255, 255, 255, 220);\n"
"	border-radius:5px;\n"
"}\n"
"QToolButton#btnProfile:hover{\n"
"	background-color: rgba(152, 108, 144, 80)\n"
"}"));
        left_box = new QWidget(widget);
        left_box->setObjectName("left_box");
        left_box->setGeometry(QRect(10, 0, 261, 621));
        left_box->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	border:none;\n"
"	color: rgba(255, 255, 255, 200);\n"
"	padding: 10px;\n"
"	text-align: left;\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(152, 108, 144, 115)\n"
"}\n"
"QToolButton{\n"
"	text-align:left;\n"
"	border-radius:6px;\n"
"	color: rgba(255, 255, 255, 220);\n"
"	padding: 10px;\n"
"}\n"
"QToolButton:hover{\n"
"	background-color: rgba(152, 108, 144, 115)\n"
"}\n"
"QToolButton#btnTags{\n"
"	border:none;\n"
"	color:rgba(255, 255, 255, 220);\n"
"	border-radius:5px;\n"
"}\n"
"QToolButton#btnTags:hover{\n"
"	background-color: rgba(152, 108, 144, 80);\n"
"}\n"
""));
        verticalLayout_2 = new QVBoxLayout(left_box);
        verticalLayout_2->setObjectName("verticalLayout_2");
        btnProfile = new QToolButton(left_box);
        btnProfile->setObjectName("btnProfile");
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(btnProfile->sizePolicy().hasHeightForWidth());
        btnProfile->setSizePolicy(sizePolicy);
        btnProfile->setMaximumSize(QSize(16777215, 50));
        QFont font;
        font.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font.setPointSize(16);
        btnProfile->setFont(font);
        btnProfile->setLayoutDirection(Qt::LeftToRight);
        btnProfile->setStyleSheet(QString::fromUtf8("border-radius:6px;\n"
"color: rgba(255, 255, 255, 200);\n"
"padding: 10px;"));
        btnProfile->setPopupMode(QToolButton::InstantPopup);
        btnProfile->setToolButtonStyle(Qt::ToolButtonTextBesideIcon);
        btnProfile->setAutoRaise(false);
        btnProfile->setArrowType(Qt::NoArrow);

        verticalLayout_2->addWidget(btnProfile);

        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Preferred);

        verticalLayout_2->addItem(verticalSpacer_2);

        btnAll_Items = new QPushButton(left_box);
        btnAll_Items->setObjectName("btnAll_Items");
        QSizePolicy sizePolicy1(QSizePolicy::Expanding, QSizePolicy::Preferred);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(btnAll_Items->sizePolicy().hasHeightForWidth());
        btnAll_Items->setSizePolicy(sizePolicy1);
        btnAll_Items->setMinimumSize(QSize(0, 0));
        btnAll_Items->setMaximumSize(QSize(16777215, 40));
        QFont font1;
        font1.setPointSize(15);
        btnAll_Items->setFont(font1);
        btnAll_Items->setLayoutDirection(Qt::LeftToRight);
        btnAll_Items->setStyleSheet(QString::fromUtf8(""));
        btnAll_Items->setCheckable(false);
        btnAll_Items->setChecked(false);

        verticalLayout_2->addWidget(btnAll_Items);

        btnFavorites = new QPushButton(left_box);
        btnFavorites->setObjectName("btnFavorites");
        sizePolicy1.setHeightForWidth(btnFavorites->sizePolicy().hasHeightForWidth());
        btnFavorites->setSizePolicy(sizePolicy1);
        btnFavorites->setMinimumSize(QSize(0, 0));
        btnFavorites->setMaximumSize(QSize(16777215, 40));
        btnFavorites->setFont(font1);
        btnFavorites->setStyleSheet(QString::fromUtf8(""));

        verticalLayout_2->addWidget(btnFavorites);

        btnGenerator = new QPushButton(left_box);
        btnGenerator->setObjectName("btnGenerator");
        sizePolicy1.setHeightForWidth(btnGenerator->sizePolicy().hasHeightForWidth());
        btnGenerator->setSizePolicy(sizePolicy1);
        btnGenerator->setMaximumSize(QSize(16777215, 40));
        btnGenerator->setFont(font1);
        btnGenerator->setStyleSheet(QString::fromUtf8(""));

        verticalLayout_2->addWidget(btnGenerator);

        line = new QFrame(left_box);
        line->setObjectName("line");
        line->setFrameShape(QFrame::HLine);
        line->setFrameShadow(QFrame::Sunken);

        verticalLayout_2->addWidget(line);

        btnTags = new QToolButton(left_box);
        btnTags->setObjectName("btnTags");
        QSizePolicy sizePolicy2(QSizePolicy::Preferred, QSizePolicy::Expanding);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(btnTags->sizePolicy().hasHeightForWidth());
        btnTags->setSizePolicy(sizePolicy2);
        btnTags->setMaximumSize(QSize(16777215, 40));
        QFont font2;
        font2.setFamilies({QString::fromUtf8("Nexa-Trial")});
        font2.setPointSize(14);
        btnTags->setFont(font2);
        btnTags->setStyleSheet(QString::fromUtf8("color: rgba(255, 255, 255, 200);"));
        btnTags->setIconSize(QSize(7, 7));
        btnTags->setToolButtonStyle(Qt::ToolButtonTextBesideIcon);
        btnTags->setArrowType(Qt::DownArrow);

        verticalLayout_2->addWidget(btnTags);

        btnRecently_Deleted = new QPushButton(left_box);
        btnRecently_Deleted->setObjectName("btnRecently_Deleted");
        sizePolicy1.setHeightForWidth(btnRecently_Deleted->sizePolicy().hasHeightForWidth());
        btnRecently_Deleted->setSizePolicy(sizePolicy1);
        btnRecently_Deleted->setMinimumSize(QSize(0, 0));
        btnRecently_Deleted->setMaximumSize(QSize(16777215, 40));
        btnRecently_Deleted->setFont(font1);
        btnRecently_Deleted->setLayoutDirection(Qt::LeftToRight);
        btnRecently_Deleted->setStyleSheet(QString::fromUtf8(""));
        btnRecently_Deleted->setCheckable(false);
        btnRecently_Deleted->setChecked(false);

        verticalLayout_2->addWidget(btnRecently_Deleted);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_2->addItem(verticalSpacer);

        gridLayoutWidget = new QWidget(widget);
        gridLayoutWidget->setObjectName("gridLayoutWidget");
        gridLayoutWidget->setGeometry(QRect(270, 20, 671, 581));
        gridLayout_4 = new QGridLayout(gridLayoutWidget);
        gridLayout_4->setSpacing(0);
        gridLayout_4->setObjectName("gridLayout_4");
        gridLayout_4->setContentsMargins(0, 0, 0, 0);
        right_box = new QWidget(gridLayoutWidget);
        right_box->setObjectName("right_box");
        QSizePolicy sizePolicy3(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy3.setHorizontalStretch(1);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(right_box->sizePolicy().hasHeightForWidth());
        right_box->setSizePolicy(sizePolicy3);
        right_box->setMinimumSize(QSize(300, 0));
        right_box->setSizeIncrement(QSize(0, 0));
        right_box->setBaseSize(QSize(400, 0));
        right_box->setStyleSheet(QString::fromUtf8(""));
        gridLayout_2 = new QGridLayout(right_box);
        gridLayout_2->setObjectName("gridLayout_2");
        wItemBox = new QWidget(right_box);
        wItemBox->setObjectName("wItemBox");
        wItemBox->setMinimumSize(QSize(0, 0));
        wItemBox->setBaseSize(QSize(0, 0));
        wItemBox->setStyleSheet(QString::fromUtf8("background-color: rgba(35, 35, 35, 220);"));

        gridLayout_2->addWidget(wItemBox, 0, 0, 1, 1);


        gridLayout_4->addWidget(right_box, 1, 1, 1, 1);

        middle_box = new QWidget(gridLayoutWidget);
        middle_box->setObjectName("middle_box");
        QSizePolicy sizePolicy4(QSizePolicy::Minimum, QSizePolicy::Expanding);
        sizePolicy4.setHorizontalStretch(0);
        sizePolicy4.setVerticalStretch(0);
        sizePolicy4.setHeightForWidth(middle_box->sizePolicy().hasHeightForWidth());
        middle_box->setSizePolicy(sizePolicy4);
        middle_box->setMinimumSize(QSize(150, 0));
        middle_box->setMaximumSize(QSize(400, 16777215));
        middle_box->setBaseSize(QSize(150, 0));
        middle_box->setStyleSheet(QString::fromUtf8(""));
        verticalLayout_3 = new QVBoxLayout(middle_box);
        verticalLayout_3->setObjectName("verticalLayout_3");
        comboCategories = new QComboBox(middle_box);
        comboCategories->addItem(QString());
        comboCategories->addItem(QString());
        comboCategories->addItem(QString());
        comboCategories->addItem(QString());
        comboCategories->addItem(QString());
        comboCategories->addItem(QString());
        comboCategories->setObjectName("comboCategories");
        sizePolicy2.setHeightForWidth(comboCategories->sizePolicy().hasHeightForWidth());
        comboCategories->setSizePolicy(sizePolicy2);
        comboCategories->setMaximumSize(QSize(16777215, 30));
        QFont font3;
        font3.setFamilies({QString::fromUtf8("Nexa-Trial")});
        comboCategories->setFont(font3);
        comboCategories->setStyleSheet(QString::fromUtf8("border-radius:6px;\n"
"padding-bottom:1px;\n"
"padding-left:6px;\n"
"color: rgba(255, 255, 255, 200);"));

        verticalLayout_3->addWidget(comboCategories);

        lvItems = new QListWidget(middle_box);
        lvItems->setObjectName("lvItems");
        lvItems->setStyleSheet(QString::fromUtf8("background-color: rgba(35, 35, 35, 220);"));

        verticalLayout_3->addWidget(lvItems);


        gridLayout_4->addWidget(middle_box, 1, 0, 1, 1);

        top_box = new QWidget(gridLayoutWidget);
        top_box->setObjectName("top_box");
        top_box->setMaximumSize(QSize(16777215, 50));
        top_box->setStyleSheet(QString::fromUtf8("\n"
"border-bottom-color: rgb(0, 0, 0);"));
        horizontalLayout = new QHBoxLayout(top_box);
        horizontalLayout->setObjectName("horizontalLayout");
        btnNew = new QPushButton(top_box);
        btnNew->setObjectName("btnNew");
        QSizePolicy sizePolicy5(QSizePolicy::MinimumExpanding, QSizePolicy::Expanding);
        sizePolicy5.setHorizontalStretch(0);
        sizePolicy5.setVerticalStretch(0);
        sizePolicy5.setHeightForWidth(btnNew->sizePolicy().hasHeightForWidth());
        btnNew->setSizePolicy(sizePolicy5);
        btnNew->setMaximumSize(QSize(65, 25));
        QFont font4;
        font4.setFamilies({QString::fromUtf8("Arial")});
        font4.setPointSize(15);
        btnNew->setFont(font4);
        btnNew->setStyleSheet(QString::fromUtf8("background-color:rgba(148, 105, 141, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
""));

        horizontalLayout->addWidget(btnNew);

        line_2 = new QFrame(top_box);
        line_2->setObjectName("line_2");
        QSizePolicy sizePolicy6(QSizePolicy::Fixed, QSizePolicy::Expanding);
        sizePolicy6.setHorizontalStretch(0);
        sizePolicy6.setVerticalStretch(0);
        sizePolicy6.setHeightForWidth(line_2->sizePolicy().hasHeightForWidth());
        line_2->setSizePolicy(sizePolicy6);
        line_2->setMaximumSize(QSize(16777215, 25));
        line_2->setStyleSheet(QString::fromUtf8("color: rgb(0, 0, 0);"));
        line_2->setFrameShape(QFrame::VLine);
        line_2->setFrameShadow(QFrame::Sunken);

        horizontalLayout->addWidget(line_2);

        hSearch = new QHBoxLayout();
        hSearch->setSpacing(0);
        hSearch->setObjectName("hSearch");
        widget_2 = new QWidget(top_box);
        widget_2->setObjectName("widget_2");
        sizePolicy.setHeightForWidth(widget_2->sizePolicy().hasHeightForWidth());
        widget_2->setSizePolicy(sizePolicy);
        widget_2->setMaximumSize(QSize(26, 27));
        widget_2->setStyleSheet(QString::fromUtf8("\n"
"background-color: rgb(23, 23, 23);\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
""));
        gridLayout_3 = new QGridLayout(widget_2);
        gridLayout_3->setObjectName("gridLayout_3");
        gridLayout_3->setContentsMargins(0, 0, 0, 0);
        label = new QLabel(widget_2);
        label->setObjectName("label");
        sizePolicy.setHeightForWidth(label->sizePolicy().hasHeightForWidth());
        label->setSizePolicy(sizePolicy);
        label->setMinimumSize(QSize(10, 10));
        label->setMaximumSize(QSize(15, 15));
        label->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);\n"
""));
        label->setPixmap(QPixmap(QString::fromUtf8(":/search_icon/search_icon.png")));
        label->setScaledContents(true);
        label->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);
        label->setMargin(0);
        label->setIndent(-1);

        gridLayout_3->addWidget(label, 0, 0, 1, 1);


        hSearch->addWidget(widget_2);

        lineEdit_Search = new QLineEdit(top_box);
        lineEdit_Search->setObjectName("lineEdit_Search");
        lineEdit_Search->setEnabled(true);
        sizePolicy.setHeightForWidth(lineEdit_Search->sizePolicy().hasHeightForWidth());
        lineEdit_Search->setSizePolicy(sizePolicy);
        lineEdit_Search->setMaximumSize(QSize(100000, 27));
        lineEdit_Search->setStyleSheet(QString::fromUtf8("border-bottom-right-radius: 6px;\n"
"border-top-right-radius: 6px;\n"
"padding-bottom:1px;\n"
"padding-left:3px"));
        lineEdit_Search->setFrame(false);
        lineEdit_Search->setClearButtonEnabled(true);

        hSearch->addWidget(lineEdit_Search);


        horizontalLayout->addLayout(hSearch);


        gridLayout_4->addWidget(top_box, 0, 0, 1, 2);

        gridLayoutWidget->raise();
        left_box->raise();

        gridLayout->addWidget(widget, 0, 2, 1, 1);


        retranslateUi(Form);
        QObject::connect(btnProfile, &QToolButton::clicked, btnProfile, qOverload<>(&QToolButton::showMenu));
        QObject::connect(btnTags, &QToolButton::clicked, btnTags, qOverload<>(&QToolButton::showMenu));

        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QCoreApplication::translate("Form", "Form", nullptr));
        btnProfile->setText(QCoreApplication::translate("Form", "account", nullptr));
        btnAll_Items->setText(QCoreApplication::translate("Form", "all items", nullptr));
        btnFavorites->setText(QCoreApplication::translate("Form", "favorites", nullptr));
        btnGenerator->setText(QCoreApplication::translate("Form", "generator", nullptr));
        btnTags->setText(QCoreApplication::translate("Form", "    tags", nullptr));
        btnRecently_Deleted->setText(QCoreApplication::translate("Form", "recently deleted", nullptr));
        comboCategories->setItemText(0, QCoreApplication::translate("Form", "All Categories", nullptr));
        comboCategories->setItemText(1, QCoreApplication::translate("Form", "Logins", nullptr));
        comboCategories->setItemText(2, QCoreApplication::translate("Form", "Identities", nullptr));
        comboCategories->setItemText(3, QCoreApplication::translate("Form", "Bank cards", nullptr));
        comboCategories->setItemText(4, QCoreApplication::translate("Form", "Bank accounts", nullptr));
        comboCategories->setItemText(5, QCoreApplication::translate("Form", "Encrypted notes", nullptr));

        btnNew->setText(QCoreApplication::translate("Form", "+  New", nullptr));
        label->setText(QString());
        lineEdit_Search->setInputMask(QString());
        lineEdit_Search->setText(QString());
        lineEdit_Search->setPlaceholderText(QCoreApplication::translate("Form", "search", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAIN_SCREEN_H

/********************************************************************************
** Form generated from reading UI file 'item_in_list.ui'
**
** Created by: Qt User Interface Compiler version 6.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_ITEM_IN_LIST_H
#define UI_ITEM_IN_LIST_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Item_In_List
{
public:
    QGridLayout *gridLayout;
    QLabel *lbl_Item_Name;
    QSpacerItem *verticalSpacer;
    QLabel *lbl_Item_Details;
    QSpacerItem *verticalSpacer_2;
    QLabel *lbl_Item_Icon;

    void setupUi(QWidget *Item_In_List)
    {
        if (Item_In_List->objectName().isEmpty())
            Item_In_List->setObjectName("Item_In_List");
        Item_In_List->resize(150, 60);
        Item_In_List->setMaximumSize(QSize(200, 75));
        Item_In_List->setStyleSheet(QString::fromUtf8("border-radius:10px;\n"
"background-color: rgb(30, 30, 30);"));
        gridLayout = new QGridLayout(Item_In_List);
        gridLayout->setObjectName("gridLayout");
        gridLayout->setVerticalSpacing(5);
        gridLayout->setContentsMargins(0, 0, 0, 0);
        lbl_Item_Name = new QLabel(Item_In_List);
        lbl_Item_Name->setObjectName("lbl_Item_Name");
        QFont font;
        font.setBold(true);
        lbl_Item_Name->setFont(font);

        gridLayout->addWidget(lbl_Item_Name, 1, 1, 1, 1);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer, 0, 1, 1, 1);

        lbl_Item_Details = new QLabel(Item_In_List);
        lbl_Item_Details->setObjectName("lbl_Item_Details");
        QFont font1;
        font1.setPointSize(11);
        lbl_Item_Details->setFont(font1);
        lbl_Item_Details->setStyleSheet(QString::fromUtf8("color: rgba(255, 255, 255, 200);"));

        gridLayout->addWidget(lbl_Item_Details, 2, 1, 1, 1);

        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_2, 3, 1, 1, 1);

        lbl_Item_Icon = new QLabel(Item_In_List);
        lbl_Item_Icon->setObjectName("lbl_Item_Icon");
        lbl_Item_Icon->setMaximumSize(QSize(50, 50));

        gridLayout->addWidget(lbl_Item_Icon, 0, 0, 4, 1);


        retranslateUi(Item_In_List);

        QMetaObject::connectSlotsByName(Item_In_List);
    } // setupUi

    void retranslateUi(QWidget *Item_In_List)
    {
        Item_In_List->setWindowTitle(QCoreApplication::translate("Item_In_List", "Form", nullptr));
        lbl_Item_Name->setText(QCoreApplication::translate("Item_In_List", "TextLabel", nullptr));
        lbl_Item_Details->setText(QCoreApplication::translate("Item_In_List", "TextLabel", nullptr));
        lbl_Item_Icon->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class Item_In_List: public Ui_Item_In_List {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_ITEM_IN_LIST_H

#ifndef UI_WINDOW_H
#define UI_WINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Window
{
public:
    QListWidget *questionListWidget;
    QPushButton *addPushButton;
    QLabel *label;
    QLineEdit *addLineEdit;
    QLabel *label_2;
    QPushButton *removePushButton;
    QLineEdit *removeLineEdit;
    QLabel *label_3;
    QPushButton *resolvePushButton;

    void setupUi(QWidget *Window)
    {
        if (Window->objectName().isEmpty())
            Window->setObjectName(QString::fromUtf8("Window"));
        Window->resize(871, 362);
        questionListWidget = new QListWidget(Window);
        questionListWidget->setObjectName(QString::fromUtf8("questionListWidget"));
        questionListWidget->setGeometry(QRect(140, 20, 291, 291));
        addPushButton = new QPushButton(Window);
        addPushButton->setObjectName(QString::fromUtf8("addPushButton"));
        addPushButton->setGeometry(QRect(610, 70, 141, 29));
        label = new QLabel(Window);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(530, 30, 63, 20));
        addLineEdit = new QLineEdit(Window);
        addLineEdit->setObjectName(QString::fromUtf8("addLineEdit"));
        addLineEdit->setGeometry(QRect(630, 30, 221, 28));
        label_2 = new QLabel(Window);

        retranslateUi(Window);

        QMetaObject::connectSlotsByName(Window);
    } // setupUi

    void retranslateUi(QWidget *Window)
    {
        Window->setWindowTitle(QCoreApplication::translate("Window", "Window", nullptr));
        addPushButton->setText(QCoreApplication::translate("Window", "Add", nullptr));
        label->setText(QCoreApplication::translate("Window", "Add", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Window: public Ui_Window {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_WINDOW_H

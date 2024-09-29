# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName("Widget")
        Widget.resize(400, 184)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_file_dialog = QPushButton(Widget)
        self.btn_file_dialog.setObjectName("btn_file_dialog")

        self.verticalLayout.addWidget(self.btn_file_dialog)

        self.btn_font_dialog = QPushButton(Widget)
        self.btn_font_dialog.setObjectName("btn_font_dialog")

        self.verticalLayout.addWidget(self.btn_font_dialog)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_color = QPushButton(Widget)
        self.btn_color.setObjectName("btn_color")

        self.horizontalLayout.addWidget(self.btn_color)

        self.btn_background = QPushButton(Widget)
        self.btn_background.setObjectName("btn_background")

        self.horizontalLayout.addWidget(self.btn_background)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_str_input = QPushButton(Widget)
        self.btn_str_input.setObjectName("btn_str_input")

        self.horizontalLayout_2.addWidget(self.btn_str_input)

        self.btn_int_input = QPushButton(Widget)
        self.btn_int_input.setObjectName("btn_int_input")

        self.horizontalLayout_2.addWidget(self.btn_int_input)

        self.btn_item_input = QPushButton(Widget)
        self.btn_item_input.setObjectName("btn_item_input")

        self.horizontalLayout_2.addWidget(self.btn_item_input)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lbl_font = QLabel(Widget)
        self.lbl_font.setObjectName("lbl_font")

        self.verticalLayout.addWidget(self.lbl_font)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)

    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(
            QCoreApplication.translate(
                "Widget",
                "\uacf5\ud1b5 \ub2e4\uc774\uc5bc\ub85c\uadf8 \uc0ac\uc6a9\ud558\uae30",
                None,
            )
        )
        self.btn_file_dialog.setText(
            QCoreApplication.translate("Widget", "QFileDialog", None)
        )
        self.btn_font_dialog.setText(
            QCoreApplication.translate("Widget", "QFontDialog", None)
        )
        self.btn_color.setText(QCoreApplication.translate("Widget", "Text Color", None))
        self.btn_background.setText(
            QCoreApplication.translate("Widget", "Background Color", None)
        )
        self.btn_str_input.setText(
            QCoreApplication.translate("Widget", "String Input", None)
        )
        self.btn_int_input.setText(
            QCoreApplication.translate("Widget", "Int Input", None)
        )
        self.btn_item_input.setText(
            QCoreApplication.translate("Widget", "Item Input", None)
        )
        self.lbl_font.setText(QCoreApplication.translate("Widget", "Some Text", None))

    # retranslateUi

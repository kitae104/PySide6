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
        Widget.resize(576, 131)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_provide = QPushButton(Widget)
        self.btn_provide.setObjectName("btn_provide")

        self.verticalLayout.addWidget(self.btn_provide)

        self.lbl_info = QLabel(Widget)
        self.lbl_info.setObjectName("lbl_info")

        self.verticalLayout.addWidget(self.lbl_info)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)

    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", "Form", None))
        self.btn_provide.setText(
            QCoreApplication.translate("Widget", "Provide Info", None)
        )
        self.lbl_info.setText(QCoreApplication.translate("Widget", "Some text", None))

    # retranslateUi

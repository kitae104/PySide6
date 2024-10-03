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
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName("Widget")
        Widget.resize(464, 362)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(Widget)
        self.label.setObjectName("label")
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.btn_fetch = QPushButton(Widget)
        self.btn_fetch.setObjectName("btn_fetch")

        self.horizontalLayout.addWidget(self.btn_fetch)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.list_fetch = QListWidget(Widget)
        self.list_fetch.setObjectName("list_fetch")

        self.verticalLayout.addWidget(self.list_fetch)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)

    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", "Form", None))
        self.label.setText(QCoreApplication.translate("Widget", "Post Fetcher", None))
        self.btn_fetch.setText(QCoreApplication.translate("Widget", "Fetch", None))

    # retranslateUi

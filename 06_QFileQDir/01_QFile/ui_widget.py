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
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName("Widget")
        Widget.resize(612, 394)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ta_text = QTextEdit(Widget)
        self.ta_text.setObjectName("ta_text")

        self.horizontalLayout.addWidget(self.ta_text)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_write = QPushButton(Widget)
        self.btn_write.setObjectName("btn_write")

        self.verticalLayout.addWidget(self.btn_write)

        self.btn_read = QPushButton(Widget)
        self.btn_read.setObjectName("btn_read")

        self.verticalLayout.addWidget(self.btn_read)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tf_select_file = QLineEdit(Widget)
        self.tf_select_file.setObjectName("tf_select_file")

        self.horizontalLayout_2.addWidget(self.tf_select_file)

        self.btn_select = QPushButton(Widget)
        self.btn_select.setObjectName("btn_select")

        self.horizontalLayout_2.addWidget(self.btn_select)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tf_copy = QLineEdit(Widget)
        self.tf_copy.setObjectName("tf_copy")

        self.horizontalLayout_3.addWidget(self.tf_copy)

        self.btn_copy = QPushButton(Widget)
        self.btn_copy.setObjectName("btn_copy")

        self.horizontalLayout_3.addWidget(self.btn_copy)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)

    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", "Form", None))
        self.btn_write.setText(QCoreApplication.translate("Widget", "Write", None))
        self.btn_read.setText(QCoreApplication.translate("Widget", "Read", None))
        self.btn_select.setText(
            QCoreApplication.translate("Widget", "Select File", None)
        )
        self.btn_copy.setText(QCoreApplication.translate("Widget", "Copy", None))

    # retranslateUi

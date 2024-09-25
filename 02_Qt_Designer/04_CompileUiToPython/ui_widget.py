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
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_frmWidget(object):
    def setupUi(self, frmWidget):
        if not frmWidget.objectName():
            frmWidget.setObjectName("frmWidget")
        frmWidget.resize(503, 193)
        self.verticalLayout = QVBoxLayout(frmWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(frmWidget)
        self.label.setObjectName("label")

        self.horizontalLayout.addWidget(self.label)

        self.editFullName = QLineEdit(frmWidget)
        self.editFullName.setObjectName("editFullName")

        self.horizontalLayout.addWidget(self.editFullName)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QLabel(frmWidget)
        self.label_2.setObjectName("label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.editOccupation = QLineEdit(frmWidget)
        self.editOccupation.setObjectName("editOccupation")

        self.horizontalLayout_2.addWidget(self.editOccupation)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.btnSubmit = QPushButton(frmWidget)
        self.btnSubmit.setObjectName("btnSubmit")

        self.verticalLayout.addWidget(self.btnSubmit)

        self.retranslateUi(frmWidget)

        QMetaObject.connectSlotsByName(frmWidget)

    # setupUi

    def retranslateUi(self, frmWidget):
        frmWidget.setWindowTitle(QCoreApplication.translate("frmWidget", "Form", None))
        self.label.setText(QCoreApplication.translate("frmWidget", "Fullname :", None))
        self.label_2.setText(
            QCoreApplication.translate("frmWidget", "Occupation :", None)
        )
        self.btnSubmit.setText(QCoreApplication.translate("frmWidget", "Submit", None))

    # retranslateUi

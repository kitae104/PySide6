# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'infodialog.ui'
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
    QAbstractButton,
    QApplication,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_InfoDialog(object):
    def setupUi(self, InfoDialog):
        if not InfoDialog.objectName():
            InfoDialog.setObjectName("InfoDialog")
        InfoDialog.resize(473, 132)
        self.verticalLayout = QVBoxLayout(InfoDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(InfoDialog)
        self.label.setObjectName("label")

        self.horizontalLayout.addWidget(self.label)

        self.edit_position = QLineEdit(InfoDialog)
        self.edit_position.setObjectName("edit_position")

        self.horizontalLayout.addWidget(self.edit_position)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QLabel(InfoDialog)
        self.label_2.setObjectName("label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.cmb_favorite = QComboBox(InfoDialog)
        self.cmb_favorite.addItem("")
        self.cmb_favorite.addItem("")
        self.cmb_favorite.addItem("")
        self.cmb_favorite.setObjectName("cmb_favorite")

        self.horizontalLayout_2.addWidget(self.cmb_favorite)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.button_box = QDialogButtonBox(InfoDialog)
        self.button_box.setObjectName("button_box")
        self.button_box.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.Ok
            | QDialogButtonBox.StandardButton.Open
            | QDialogButtonBox.StandardButton.Save
            | QDialogButtonBox.StandardButton.Yes
        )

        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(InfoDialog)

        QMetaObject.connectSlotsByName(InfoDialog)

    # setupUi

    def retranslateUi(self, InfoDialog):
        InfoDialog.setWindowTitle(
            QCoreApplication.translate("InfoDialog", "Dialog", None)
        )
        self.label.setText(QCoreApplication.translate("InfoDialog", "Position :", None))
        self.label_2.setText(
            QCoreApplication.translate("InfoDialog", "Favorite :", None)
        )
        self.cmb_favorite.setItemText(
            0, QCoreApplication.translate("InfoDialog", "Windows", None)
        )
        self.cmb_favorite.setItemText(
            1, QCoreApplication.translate("InfoDialog", "Linux", None)
        )
        self.cmb_favorite.setItemText(
            2, QCoreApplication.translate("InfoDialog", "Mac", None)
        )

    # retranslateUi

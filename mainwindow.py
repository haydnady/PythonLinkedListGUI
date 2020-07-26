# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(540, 341)
        MainWindow.setStyleSheet(u"background-color: rgb(189, 189, 189);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(-1, 0, 0, -1)
        self.findPushButton = QPushButton(self.centralwidget)
        self.findPushButton.setObjectName(u"findPushButton")
        self.findPushButton.setStyleSheet(u"background-color: rgb(170, 255, 255);")

        self.gridLayout.addWidget(self.findPushButton, 1, 6, 1, 1)

        self.removePushButton = QPushButton(self.centralwidget)
        self.removePushButton.setObjectName(u"removePushButton")
        self.removePushButton.setStyleSheet(u"background-color: rgb(255, 170, 127);")

        self.gridLayout.addWidget(self.removePushButton, 1, 4, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 7, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 5, 1, 1)

        self.addPushButton = QPushButton(self.centralwidget)
        self.addPushButton.setObjectName(u"addPushButton")
        self.addPushButton.setStyleSheet(u"background-color: rgb(85, 255, 127);")

        self.gridLayout.addWidget(self.addPushButton, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.inputPlainTextEdit = QPlainTextEdit(self.centralwidget)
        self.inputPlainTextEdit.setObjectName(u"inputPlainTextEdit")
        font = QFont()
        font.setPointSize(37)
        font.setBold(False)
        font.setWeight(50)
        self.inputPlainTextEdit.setFont(font)
        self.inputPlainTextEdit.setLayoutDirection(Qt.LeftToRight)
        self.inputPlainTextEdit.setStyleSheet(u"background-color: rgb(223, 223, 223);")
        self.inputPlainTextEdit.setReadOnly(False)
        self.inputPlainTextEdit.setOverwriteMode(False)
        self.inputPlainTextEdit.setBackgroundVisible(False)

        self.gridLayout.addWidget(self.inputPlainTextEdit, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 9, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)

        self.currentTextEdit = QTextEdit(self.centralwidget)
        self.currentTextEdit.setObjectName(u"currentTextEdit")
        font1 = QFont()
        font1.setPointSize(20)
        self.currentTextEdit.setFont(font1)
        self.currentTextEdit.setStyleSheet(u"background-color: rgb(223, 223, 223);")
        self.currentTextEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.currentTextEdit, 5, 0, 1, 7)

        self.beforeTextEdit = QTextEdit(self.centralwidget)
        self.beforeTextEdit.setObjectName(u"beforeTextEdit")
        self.beforeTextEdit.setFont(font1)
        self.beforeTextEdit.setStyleSheet(u"background-color: rgb(223, 223, 223);")
        self.beforeTextEdit.setReadOnly(True)
        self.beforeTextEdit.setOverwriteMode(False)

        self.gridLayout.addWidget(self.beforeTextEdit, 8, 0, 1, 7)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_5, 2, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 540, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.findPushButton.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.removePushButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.addPushButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.inputPlainTextEdit.setPlaceholderText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Current List:", None))
        self.currentTextEdit.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"List Before Operation:", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPlainTextEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(598, 634)
        font = QFont()
        font.setFamilies([u"BM Dohyeon"])
        font.setBold(True)
        Form.setFont(font)
        self.login_btn = QPushButton(Form)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(200, 440, 191, 101))
        font1 = QFont()
        font1.setFamilies([u"BM Dohyeon"])
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setItalic(False)
        self.login_btn.setFont(font1)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 140, 111, 71))
        font2 = QFont()
        font2.setFamilies([u"BM Dohyeon"])
        font2.setPointSize(18)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 260, 111, 71))
        self.label_2.setFont(font2)
        self.id = QPlainTextEdit(Form)
        self.id.setObjectName(u"id")
        self.id.setGeometry(QRect(250, 160, 191, 31))
        self.pw = QPlainTextEdit(Form)
        self.pw.setObjectName(u"pw")
        self.pw.setGeometry(QRect(250, 280, 191, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.login_btn.setText(QCoreApplication.translate("Form", u"\ub85c\uadf8\uc778", None))
        self.label.setText(QCoreApplication.translate("Form", u"\uc544\uc774\ub514", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\ube44\ubc00\ubc88\ud638", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QLabel,
    QMainWindow, QPlainTextEdit, QSizePolicy, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(481, 738)
        self.actiong = QAction(MainWindow)
        self.actiong.setObjectName(u"actiong")
        self.action_O = QAction(MainWindow)
        self.action_O.setObjectName(u"action_O")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.rawPacketTextEdit = QPlainTextEdit(self.centralwidget)
        self.rawPacketTextEdit.setObjectName(u"rawPacketTextEdit")
        self.rawPacketTextEdit.setGeometry(QRect(20, 20, 441, 221))
        self.xorCheckBox = QCheckBox(self.centralwidget)
        self.xorCheckBox.setObjectName(u"xorCheckBox")
        self.xorCheckBox.setGeometry(QRect(30, 250, 91, 31))
        self.xorKeyTextEdit = QPlainTextEdit(self.centralwidget)
        self.xorKeyTextEdit.setObjectName(u"xorKeyTextEdit")
        self.xorKeyTextEdit.setEnabled(False)
        self.xorKeyTextEdit.setGeometry(QRect(120, 250, 341, 31))
        self.packetInfoGroupBox = QGroupBox(self.centralwidget)
        self.packetInfoGroupBox.setObjectName(u"packetInfoGroupBox")
        self.packetInfoGroupBox.setGeometry(QRect(20, 290, 441, 431))
        self.magicStartLabel = QLabel(self.packetInfoGroupBox)
        self.magicStartLabel.setObjectName(u"magicStartLabel")
        self.magicStartLabel.setGeometry(QRect(20, 30, 81, 31))
        self.magicStartTextEdit = QPlainTextEdit(self.packetInfoGroupBox)
        self.magicStartTextEdit.setObjectName(u"magicStartTextEdit")
        self.magicStartTextEdit.setGeometry(QRect(140, 30, 71, 31))
        self.magicStartTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.magicStartTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.magicStartTextEdit.setReadOnly(True)
        self.cmdIdHexTextEdit = QPlainTextEdit(self.packetInfoGroupBox)
        self.cmdIdHexTextEdit.setObjectName(u"cmdIdHexTextEdit")
        self.cmdIdHexTextEdit.setGeometry(QRect(140, 70, 71, 31))
        self.cmdIdHexTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.cmdIdHexTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.cmdIdHexTextEdit.setReadOnly(True)
        self.cmdIdLabel = QLabel(self.packetInfoGroupBox)
        self.cmdIdLabel.setObjectName(u"cmdIdLabel")
        self.cmdIdLabel.setGeometry(QRect(20, 70, 81, 31))
        self.cmdIdDecTextEdit = QPlainTextEdit(self.packetInfoGroupBox)
        self.cmdIdDecTextEdit.setObjectName(u"cmdIdDecTextEdit")
        self.cmdIdDecTextEdit.setGeometry(QRect(330, 70, 71, 31))
        self.cmdIdDecTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.cmdIdDecTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.cmdIdDecTextEdit.setReadOnly(True)
        self.cmdIdDirectLabel = QLabel(self.packetInfoGroupBox)
        self.cmdIdDirectLabel.setObjectName(u"cmdIdDirectLabel")
        self.cmdIdDirectLabel.setGeometry(QRect(240, 70, 81, 31))
        self.metadataLengthHexTextEdit = QPlainTextEdit(self.packetInfoGroupBox)
        self.metadataLengthHexTextEdit.setObjectName(u"metadataLengthHexTextEdit")
        self.metadataLengthHexTextEdit.setGeometry(QRect(140, 110, 71, 31))
        self.metadataLengthHexTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.metadataLengthHexTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.metadataLengthHexTextEdit.setReadOnly(True)
        self.metadataLengthLabel = QLabel(self.packetInfoGroupBox)
        self.metadataLengthLabel.setObjectName(u"metadataLengthLabel")
        self.metadataLengthLabel.setGeometry(QRect(20, 110, 111, 31))
        self.metadataLengthDecTextEdit = QPlainTextEdit(self.packetInfoGroupBox)
        self.metadataLengthDecTextEdit.setObjectName(u"metadataLengthDecTextEdit")
        self.metadataLengthDecTextEdit.setGeometry(QRect(330, 110, 71, 31))
        self.metadataLengthDecTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.metadataLengthDecTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.metadataLengthDecTextEdit.setReadOnly(True)
        self.metadataLengthDirectLabel = QLabel(self.packetInfoGroupBox)
        self.metadataLengthDirectLabel.setObjectName(u"metadataLengthDirectLabel")
        self.metadataLengthDirectLabel.setGeometry(QRect(240, 110, 81, 31))
        self.bodyLengthDecTextEdit = QPlainTextEdit(self.packetInfoGroupBox)
        self.bodyLengthDecTextEdit.setObjectName(u"bodyLengthDecTextEdit")
        self.bodyLengthDecTextEdit.setGeometry(QRect(330, 150, 71, 31))
        self.bodyLengthDecTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.bodyLengthDecTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.bodyLengthDecTextEdit.setReadOnly(True)
        self.bodyLengthHexTextEdit = QPlainTextEdit(self.packetInfoGroupBox)
        self.bodyLengthHexTextEdit.setObjectName(u"bodyLengthHexTextEdit")
        self.bodyLengthHexTextEdit.setGeometry(QRect(140, 150, 71, 31))
        self.bodyLengthHexTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.bodyLengthHexTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.bodyLengthHexTextEdit.setReadOnly(True)
        self.bodyLengthDirectLabel = QLabel(self.packetInfoGroupBox)
        self.bodyLengthDirectLabel.setObjectName(u"bodyLengthDirectLabel")
        self.bodyLengthDirectLabel.setGeometry(QRect(240, 150, 81, 31))
        self.bodyLengthLabel = QLabel(self.packetInfoGroupBox)
        self.bodyLengthLabel.setObjectName(u"bodyLengthLabel")
        self.bodyLengthLabel.setGeometry(QRect(20, 150, 111, 31))
        self.metadataLabel = QLabel(self.packetInfoGroupBox)
        self.metadataLabel.setObjectName(u"metadataLabel")
        self.metadataLabel.setGeometry(QRect(20, 190, 111, 31))
        self.metadataTextEdit = QPlainTextEdit(self.packetInfoGroupBox)
        self.metadataTextEdit.setObjectName(u"metadataTextEdit")
        self.metadataTextEdit.setGeometry(QRect(140, 190, 281, 31))
        self.metadataTextEdit.setReadOnly(True)
        self.bodyLabel = QLabel(self.packetInfoGroupBox)
        self.bodyLabel.setObjectName(u"bodyLabel")
        self.bodyLabel.setGeometry(QRect(20, 230, 111, 31))
        self.bodyTextEdit = QPlainTextEdit(self.packetInfoGroupBox)
        self.bodyTextEdit.setObjectName(u"bodyTextEdit")
        self.bodyTextEdit.setGeometry(QRect(140, 230, 281, 151))
        self.bodyTextEdit.setReadOnly(True)
        self.magicEndTextEdit = QPlainTextEdit(self.packetInfoGroupBox)
        self.magicEndTextEdit.setObjectName(u"magicEndTextEdit")
        self.magicEndTextEdit.setGeometry(QRect(140, 390, 71, 31))
        self.magicEndTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.magicEndTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.magicEndTextEdit.setReadOnly(True)
        self.magicEndLabel = QLabel(self.packetInfoGroupBox)
        self.magicEndLabel.setObjectName(u"magicEndLabel")
        self.magicEndLabel.setGeometry(QRect(20, 390, 81, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BocchiParser", None))
        self.actiong.setText(QCoreApplication.translate("MainWindow", u"g", None))
        self.action_O.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00(O)...", None))
        self.xorCheckBox.setText(QCoreApplication.translate("MainWindow", u"XOR Key :", None))
        self.packetInfoGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Packet Info", None))
        self.magicStartLabel.setText(QCoreApplication.translate("MainWindow", u"Magic Start :", None))
        self.magicStartTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"4567", None))
        self.cmdIdHexTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"HEX", None))
        self.cmdIdLabel.setText(QCoreApplication.translate("MainWindow", u"CmdId :", None))
        self.cmdIdDecTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DEC", None))
        self.cmdIdDirectLabel.setText(QCoreApplication.translate("MainWindow", u"\u2014\u2014\u2014\u2014>", None))
        self.metadataLengthHexTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"HEX", None))
        self.metadataLengthLabel.setText(QCoreApplication.translate("MainWindow", u"Metadata Length :", None))
        self.metadataLengthDecTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DEC", None))
        self.metadataLengthDirectLabel.setText(QCoreApplication.translate("MainWindow", u"\u2014\u2014\u2014\u2014>", None))
        self.bodyLengthDecTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DEC", None))
        self.bodyLengthHexTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"HEX", None))
        self.bodyLengthDirectLabel.setText(QCoreApplication.translate("MainWindow", u"\u2014\u2014\u2014\u2014>", None))
        self.bodyLengthLabel.setText(QCoreApplication.translate("MainWindow", u"Body Length :", None))
        self.metadataLabel.setText(QCoreApplication.translate("MainWindow", u"Metadata :", None))
        self.bodyLabel.setText(QCoreApplication.translate("MainWindow", u"Body :", None))
        self.magicEndTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"89ab", None))
        self.magicEndLabel.setText(QCoreApplication.translate("MainWindow", u"Magic End :", None))
    # retranslateUi


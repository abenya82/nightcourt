# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_one.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1118, 752)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(370, 10, 321, 61))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(24)
        self.title_label.setFont(font)
        self.select_player_combo_box = QComboBox(self.centralwidget)
        self.select_player_combo_box.setObjectName(u"select_player_combo_box")
        self.select_player_combo_box.setEnabled(False)
        self.select_player_combo_box.setGeometry(QRect(20, 110, 271, 31))
        font1 = QFont()
        font1.setFamilies([u"Batang"])
        font1.setPointSize(12)
        self.select_player_combo_box.setFont(font1)
        self.player_title_label = QLabel(self.centralwidget)
        self.player_title_label.setObjectName(u"player_title_label")
        self.player_title_label.setEnabled(False)
        self.player_title_label.setGeometry(QRect(130, 80, 131, 21))
        self.player_title_label.setTextFormat(Qt.RichText)
        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(400, 680, 281, 31))
        self.player_go_button = QPushButton(self.centralwidget)
        self.player_go_button.setObjectName(u"player_go_button")
        self.player_go_button.setEnabled(False)
        self.player_go_button.setGeometry(QRect(100, 170, 121, 31))
        self.playerCurrentStatTable = QTableWidget(self.centralwidget)
        self.playerCurrentStatTable.setObjectName(u"playerCurrentStatTable")
        self.playerCurrentStatTable.setEnabled(False)
        self.playerCurrentStatTable.setGeometry(QRect(30, 580, 1051, 91))
        font2 = QFont()
        font2.setFamilies([u"Sitka Display"])
        font2.setPointSize(12)
        self.playerCurrentStatTable.setFont(font2)
        self.playerCurrentStatTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.quitButton = QPushButton(self.centralwidget)
        self.quitButton.setObjectName(u"quitButton")
        self.quitButton.setGeometry(QRect(990, 680, 111, 31))
        self.quitButton.setIconSize(QSize(32, 32))
        self.seasonStatsLabel = QLabel(self.centralwidget)
        self.seasonStatsLabel.setObjectName(u"seasonStatsLabel")
        self.seasonStatsLabel.setEnabled(False)
        self.seasonStatsLabel.setGeometry(QRect(70, 520, 151, 31))
        self.last10gamestable = QTableWidget(self.centralwidget)
        self.last10gamestable.setObjectName(u"last10gamestable")
        self.last10gamestable.setEnabled(False)
        self.last10gamestable.setGeometry(QRect(410, 90, 681, 271))
        self.last10gamestable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.last10gamestable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.last10gamestable.verticalHeader().setVisible(False)
        self.last10GamesLabel = QLabel(self.centralwidget)
        self.last10GamesLabel.setObjectName(u"last10GamesLabel")
        self.last10GamesLabel.setEnabled(False)
        self.last10GamesLabel.setGeometry(QRect(870, 60, 141, 31))
        self.nextGameInfoTable = QTableWidget(self.centralwidget)
        self.nextGameInfoTable.setObjectName(u"nextGameInfoTable")
        self.nextGameInfoTable.setEnabled(False)
        self.nextGameInfoTable.setGeometry(QRect(460, 400, 541, 91))
        self.nextGameInfoTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.nextGameInfoTable.verticalHeader().setVisible(False)
        self.bookieSelectComboBox = QComboBox(self.centralwidget)
        self.bookieSelectComboBox.setObjectName(u"bookieSelectComboBox")
        self.bookieSelectComboBox.setGeometry(QRect(1010, 10, 91, 31))
        self.teamSelectComboBox = QComboBox(self.centralwidget)
        self.teamSelectComboBox.setObjectName(u"teamSelectComboBox")
        self.teamSelectComboBox.setEnabled(False)
        self.teamSelectComboBox.setGeometry(QRect(30, 280, 251, 31))
        font3 = QFont()
        font3.setFamilies([u"Batang"])
        font3.setPointSize(14)
        self.teamSelectComboBox.setFont(font3)
        self.playerFromTeamComboBox = QComboBox(self.centralwidget)
        self.playerFromTeamComboBox.setObjectName(u"playerFromTeamComboBox")
        self.playerFromTeamComboBox.setEnabled(False)
        self.playerFromTeamComboBox.setGeometry(QRect(40, 350, 231, 31))
        font4 = QFont()
        font4.setFamilies([u"Batang"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.playerFromTeamComboBox.setFont(font4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1118, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#a54525;\">Welcome to the App</span></p></body></html>", None))
        self.player_title_label.setText(QCoreApplication.translate("MainWindow", u"Select Player", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"GO!", None))
        self.player_go_button.setText(QCoreApplication.translate("MainWindow", u"Get Stats!", None))
        self.quitButton.setText(QCoreApplication.translate("MainWindow", u"QUIT", None))
        self.seasonStatsLabel.setText(QCoreApplication.translate("MainWindow", u"Total Season Stats:", None))
        self.last10GamesLabel.setText(QCoreApplication.translate("MainWindow", u"Last 10 Games", None))
    # retranslateUi


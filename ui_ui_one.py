# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\dev\nightcourt\ui_one.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1118, 752)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(370, 10, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.select_player_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.select_player_combo_box.setEnabled(False)
        self.select_player_combo_box.setGeometry(QtCore.QRect(20, 110, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Batang")
        font.setPointSize(12)
        self.select_player_combo_box.setFont(font)
        self.select_player_combo_box.setObjectName("select_player_combo_box")
        self.player_title_label = QtWidgets.QLabel(self.centralwidget)
        self.player_title_label.setEnabled(False)
        self.player_title_label.setGeometry(QtCore.QRect(130, 80, 131, 21))
        self.player_title_label.setTextFormat(QtCore.Qt.RichText)
        self.player_title_label.setObjectName("player_title_label")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(400, 680, 281, 31))
        self.start_button.setObjectName("start_button")
        self.player_go_button = QtWidgets.QPushButton(self.centralwidget)
        self.player_go_button.setEnabled(False)
        self.player_go_button.setGeometry(QtCore.QRect(100, 170, 121, 31))
        self.player_go_button.setObjectName("player_go_button")
        self.playerCurrentStatTable = QtWidgets.QTableWidget(self.centralwidget)
        self.playerCurrentStatTable.setEnabled(False)
        self.playerCurrentStatTable.setGeometry(QtCore.QRect(10, 580, 1091, 91))
        font = QtGui.QFont()
        font.setFamily("Sitka Display")
        font.setPointSize(12)
        self.playerCurrentStatTable.setFont(font)
        self.playerCurrentStatTable.setObjectName("playerCurrentStatTable")
        self.playerCurrentStatTable.setColumnCount(0)
        self.playerCurrentStatTable.setRowCount(0)
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(990, 680, 111, 31))
        self.quitButton.setIconSize(QtCore.QSize(32, 32))
        self.quitButton.setObjectName("quitButton")
        self.seasonStatsLabel = QtWidgets.QLabel(self.centralwidget)
        self.seasonStatsLabel.setEnabled(False)
        self.seasonStatsLabel.setGeometry(QtCore.QRect(70, 520, 151, 31))
        self.seasonStatsLabel.setObjectName("seasonStatsLabel")
        self.last10gamestable = QtWidgets.QTableWidget(self.centralwidget)
        self.last10gamestable.setEnabled(False)
        self.last10gamestable.setGeometry(QtCore.QRect(390, 90, 701, 271))
        self.last10gamestable.setObjectName("last10gamestable")
        self.last10gamestable.setColumnCount(0)
        self.last10gamestable.setRowCount(0)
        self.last10GamesLabel = QtWidgets.QLabel(self.centralwidget)
        self.last10GamesLabel.setEnabled(False)
        self.last10GamesLabel.setGeometry(QtCore.QRect(870, 60, 141, 31))
        self.last10GamesLabel.setObjectName("last10GamesLabel")
        self.nextGameInfoTable = QtWidgets.QTableWidget(self.centralwidget)
        self.nextGameInfoTable.setEnabled(False)
        self.nextGameInfoTable.setGeometry(QtCore.QRect(460, 400, 541, 91))
        self.nextGameInfoTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.nextGameInfoTable.setObjectName("nextGameInfoTable")
        self.nextGameInfoTable.setColumnCount(0)
        self.nextGameInfoTable.setRowCount(0)
        self.nextGameInfoTable.verticalHeader().setVisible(False)
        self.bookieSelectComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.bookieSelectComboBox.setGeometry(QtCore.QRect(1010, 10, 91, 31))
        self.bookieSelectComboBox.setObjectName("bookieSelectComboBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1118, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#a54525;\">Welcome to the App</span></p></body></html>"))
        self.player_title_label.setText(_translate("MainWindow", "Select Player"))
        self.start_button.setText(_translate("MainWindow", "GO!"))
        self.player_go_button.setText(_translate("MainWindow", "Get Stats!"))
        self.quitButton.setText(_translate("MainWindow", "QUIT"))
        self.seasonStatsLabel.setText(_translate("MainWindow", "Total Season Stats:"))
        self.last10GamesLabel.setText(_translate("MainWindow", "Last 10 Games"))

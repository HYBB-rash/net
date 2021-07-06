# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/Server.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ServerStatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.ServerStatusLabel.setGeometry(QtCore.QRect(40, 40, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ServerStatusLabel.setFont(font)
        self.ServerStatusLabel.setObjectName("ServerStatusLabel")
        self.StatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.StatusLabel.setGeometry(QtCore.QRect(190, 40, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.StatusLabel.setFont(font)
        self.StatusLabel.setObjectName("StatusLabel")
        self.ReportShower = QtWidgets.QTextBrowser(self.centralwidget)
        self.ReportShower.setGeometry(QtCore.QRect(410, 90, 341, 451))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ReportShower.setFont(font)
        self.ReportShower.setObjectName("ReportShower")
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(40, 210, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.StartButton.setFont(font)
        self.StartButton.setObjectName("StartButton")
        self.LinkShower = QtWidgets.QTextBrowser(self.centralwidget)
        self.LinkShower.setGeometry(QtCore.QRect(40, 310, 256, 241))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LinkShower.setFont(font)
        self.LinkShower.setObjectName("LinkShower")
        self.LinkLabel = QtWidgets.QLabel(self.centralwidget)
        self.LinkLabel.setGeometry(QtCore.QRect(40, 250, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LinkLabel.setFont(font)
        self.LinkLabel.setObjectName("LinkLabel")
        self.ReportLabel = QtWidgets.QLabel(self.centralwidget)
        self.ReportLabel.setGeometry(QtCore.QRect(410, 30, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ReportLabel.setFont(font)
        self.ReportLabel.setObjectName("ReportLabel")
        self.SocketInput = QtWidgets.QLineEdit(self.centralwidget)
        self.SocketInput.setGeometry(QtCore.QRect(40, 160, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SocketInput.setFont(font)
        self.SocketInput.setObjectName("SocketInput")
        self.SocketLabel = QtWidgets.QLabel(self.centralwidget)
        self.SocketLabel.setGeometry(QtCore.QRect(40, 100, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SocketLabel.setFont(font)
        self.SocketLabel.setObjectName("SocketLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 17))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Server"))
        self.ServerStatusLabel.setText(_translate("MainWindow", "Server Status:"))
        self.StatusLabel.setText(_translate("MainWindow", "Close"))
        self.StartButton.setText(_translate("MainWindow", "Start Server"))
        self.LinkLabel.setText(_translate("MainWindow", "Link List:"))
        self.ReportLabel.setText(_translate("MainWindow", "Report:"))
        self.SocketLabel.setText(_translate("MainWindow", "Server Listen Socket:"))

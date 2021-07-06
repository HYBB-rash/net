# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/Client.ui'
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
        self.ClientStatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.ClientStatusLabel.setGeometry(QtCore.QRect(70, 110, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ClientStatusLabel.setFont(font)
        self.ClientStatusLabel.setObjectName("ClientStatusLabel")
        self.ReportShower = QtWidgets.QTextBrowser(self.centralwidget)
        self.ReportShower.setGeometry(QtCore.QRect(430, 90, 281, 451))
        self.ReportShower.setObjectName("ReportShower")
        self.ClientStatusShow = QtWidgets.QLabel(self.centralwidget)
        self.ClientStatusShow.setGeometry(QtCore.QRect(210, 110, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ClientStatusShow.setFont(font)
        self.ClientStatusShow.setObjectName("ClientStatusShow")
        self.LinkButton = QtWidgets.QPushButton(self.centralwidget)
        self.LinkButton.setGeometry(QtCore.QRect(70, 250, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LinkButton.setFont(font)
        self.LinkButton.setObjectName("LinkButton")
        self.SocketIpout = QtWidgets.QLineEdit(self.centralwidget)
        self.SocketIpout.setGeometry(QtCore.QRect(70, 200, 251, 41))
        self.SocketIpout.setObjectName("SocketIpout")
        self.ScoketLabel = QtWidgets.QLabel(self.centralwidget)
        self.ScoketLabel.setGeometry(QtCore.QRect(70, 150, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ScoketLabel.setFont(font)
        self.ScoketLabel.setObjectName("ScoketLabel")
        self.ReportLabel = QtWidgets.QLabel(self.centralwidget)
        self.ReportLabel.setGeometry(QtCore.QRect(430, 30, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ReportLabel.setFont(font)
        self.ReportLabel.setObjectName("ReportLabel")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Client"))
        self.ClientStatusLabel.setText(_translate("MainWindow", "Client Status:"))
        self.ClientStatusShow.setText(_translate("MainWindow", "Close"))
        self.LinkButton.setText(_translate("MainWindow", "Start Tcp Link to Server"))
        self.ScoketLabel.setText(_translate("MainWindow", "Target Socket:"))
        self.ReportLabel.setText(_translate("MainWindow", "Report:"))

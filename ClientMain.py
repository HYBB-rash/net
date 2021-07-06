#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ClientMain.py
@Time    :   2021/07/06 13:55:41
@Author  :   hyong 
@Version :   1.0
@Contact :   hyong_cs@outlook.com
"""
# here put the import lib
from Client import Client
from ClientUI import Ui_MainWindow

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)


class ClientMain(Client, Ui_MainWindow):
    def __init__(self, interval: int, ip: str, socket: str) -> None:
        super().__init__(interval, ip, socket)
        self._translate = QtCore.QCoreApplication.translate

    def show_ui(self):
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        self.setupUi(MainWindow)
        MainWindow.show()
        self.LinkButton.clicked.connect(self.func_button_start)
        sys.exit(app.exec_())

    def func_button_start(self):
        self.start_tcp_link(self.tar_socket)

    def start_link_refresh(self):
        super().start_link_refresh()
        self.ClientStatusShow.setText(self._translate("MainWindow", "SYNSENT"))
        QApplication.processEvents()

    def ack_response_refresh(self):
        super().ack_response_refresh()
        self.ClientStatusShow.setText(self._translate("MainWindow", "ESTABLISH"))
        QApplication.processEvents()

    def start_link_tcp(self, socket: str) -> dict:
        tcp = super().start_link_tcp(socket)
        self.ReportShower.append("sent: \t" + str(tcp) + "\n")
        QApplication.processEvents()
        return tcp
    
    def ack_response_tcp(self, data: dict) -> dict:
        self.ReportShower.append("get: \t" + str(data) + "\n")
        tcp = super().ack_response_tcp(data)
        self.ReportShower.append("sent: \t" + str(tcp) + "\n")
        QApplication.processEvents()
        return tcp


if __name__ == "__main__":
    c = ClientMain(2, "192.168.196.169", "127.0.0.1:7890")
    c.show_ui()

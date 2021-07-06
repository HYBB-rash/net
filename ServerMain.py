# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ServerMain.py
@Time    :   2021/07/06 14:10:34
@Author  :   hyong 
@Version :   1.0
@Contact :   hyong_cs@outlook.com
"""
# here put the import lib
import json

from Server import Server
from ServerUI import Ui_MainWindow

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)


class ServerMain(Server, Ui_MainWindow):
    def __init__(self, socket: str, interval: int) -> None:
        super().__init__(socket, interval)
        self._translate = QtCore.QCoreApplication.translate

    def show_ui(self):
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        self.setupUi(MainWindow)
        MainWindow.show()
        self.StartButton.clicked.connect(self.func_button_start)
        sys.exit(app.exec_())

    def func_button_start(self):
        socket = self.SocketInput.text()
        self.ip, self.port = socket.split(":")[0], int(socket.split(":")[1])
        self.start_service()
    
    def link_status(self) -> str:
        res = ''
        keys = self.links.keys()
        for key in keys:
            value = self.links[key]
            res += key + "  " + ("SYNSENT" if value == 2 else "ESTABLISHED") + "\n"
        return res

    def return_ack_refresh(self, data: dict):
        super().return_ack_refresh(data)
        self.StatusLabel.setText(self._translate("MainWindow", "SYNRCVD"))
        self.LinkShower.setText(self._translate("MainWindow", self.link_status()))
        QApplication.processEvents()

        logging.debug(f"change server status to SYNRCVD")
        logging.debug(f"data: \n {str(self.links)}")

    def set_listen_status(self):
        super().set_listen_status()
        logging.debug(f"change server status to LISTEND")
        self.StatusLabel.setText(self._translate("MainWindow", "LISTEN"))
        QApplication.processEvents()

    def establish_link_refresh(self, data: dict):
        super().establish_link_refresh(data)
        logging.debug(f"change server status to ESTABLISH")
        self.StatusLabel.setText(self._translate("MainWindow", "ESTABLISH"))
        self.LinkShower.setText(self._translate("MainWindow", self.link_status()))
        QApplication.processEvents()

    def establish_link_end_refresh(self):
        super().establish_link_end_refresh()
        self.StatusLabel.setText(self._translate("MainWindows", "LISTEN"))

    def return_ack_tcp(self, data: dict) -> dict:
        self.ReportShower.append("get: \n" + str(data) + "\n")
        QApplication.processEvents()

        tcp = super().return_ack_tcp(data)
        self.ReportShower.append("sent: \n" + str(tcp) + "\n")
        QApplication.processEvents()
        return tcp

    def establish_link(self, data: dict):
        self.ReportShower.append("get: \n" + str(data) + "\n")
        QApplication.processEvents()
        return super().establish_link(data)
    
    def establish_link_end_refresh(self):
        self.StatusLabel.setText(self._translate("MainWindows", "LISTEN"))
        QApplication.processEvents()
        return super().establish_link_end_refresh()

if __name__ == "__main__":
    logging.info("clear tmp data")
    null_data = {}
    json.dump(null_data, open("line.json", "w", encoding="utf-8"), ensure_ascii=False)

    logging.info("start ui test")
    s = ServerMain("127.0.0.1:7890", 2)
    s.show_ui()

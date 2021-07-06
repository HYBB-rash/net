
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ClientMain.py
@Time    :   2021/07/06 13:55:41
@Author  :   hyong 
@Version :   1.0
@Contact :   hyong_cs@outlook.com
'''
# here put the import lib
from Client import Client
from ClientUI import Ui_MainWindow

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class ClientMain(Client, Ui_MainWindow):

    def show_ui(self):
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        self.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    c = ClientMain(2, '192.168.196.169', '127.0.0.1:7890')
    c.show_ui()

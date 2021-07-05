# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   Client.py
@Time    :   2021/07/05 13:40:47
@Author  :   hyong 
@Version :   1.0
@Contact :   hyong_cs@outlook.com
"""
# here put the import lib

import logging
from TcpPackage import get_tcp_package
from multiprocessing import Process
import random
from GlobalVar import recv, sent
import time

CLOSE = 0
SYNSENT = 2
ESTABLISHED = 3


class Client(Process):
    def __init__(self, interval: int, ip: str, socket: str) -> None:
        Process.__init__(self)
        self.interval = interval

        self.status = CLOSE

        self.ip = ip
        self.port = random.randint(1, 65535)

        self.seq = 1
        self.tar_socket = socket

    def run(self):
        self.start_tcp_link(self.tar_socket)

    def start_tcp_link(self, socket: str):
        """开始尝试  TCP 连接

        Args:
            socket (str): 服务器的  socket  套接字
        """
        logging.info("client start tcp link")

        data = self.start_link(socket)

        if data["SYN"] == 1 and data["ACK"] == 1:
            self.ack_response(data, socket)

    def get_socket(self):
        return self.ip + ":" + str(self.port)

    def start_link_tcp(self, socket: str) -> dict:
        """获取第一次握手的请求报文

        Args:
            socket (str): 服务器端的套接字

        Returns:
            dict: 打包好的  TCP  请求报文
        """
        tcp = get_tcp_package()
        tcp["SYN"], tcp["seq"] = 1, self.seq
        tcp["src_ip"], tcp["src_port"] = self.ip, self.port
        tcp["dest_port"] = socket.split(":")[1]
        return tcp

    def start_link(self, socket: str) -> dict:
        """开始第一次握手

        Args:
            socket (str): 服务器的套接字

        Returns:
            dict: 监听应答结果
        """

        tcp = self.start_link_tcp(socket)

        self.status, self.seq = SYNSENT, self.seq + 1
        logging.info(f"client status is synsent.")
        logging.debug(f"start_link tcp data package is \n {tcp}")

        sent(socket, tcp)

        resp = None
        while True:
            sleep_time = random.randint(0, 5)
            time.sleep(sleep_time)
            resp = recv(self.get_socket())
            if resp is None:
                continue
            else:
                logging.info(f"first syn response get res")
                break
        return resp

    def ack_response_tcp(self, data: dict) -> dict:
        """获取第三次握手的请求报文

        Args:
            data (dict): 第二次握手的请求报文

        Returns:
            dict: 第三次握手的请求报文
        """
        tcp = get_tcp_package()

        tcp["src_port"], tcp["dest_port"] = self.port, data["src_port"]
        tcp["ACK"], tcp["seq"], tcp["ack"] = 1, self.seq, data["seq"] + 1
        tcp["src_ip"] = self.ip

        return tcp

    def ack_response(self, data: dict, socket: str):
        """第三次握手

        Args:
            data (dict): 第二次握手的数据包
            socket (str): 服务器的  socket  套接字
        """

        tcp = self.ack_response_tcp(data)

        self.status, self.seq = ESTABLISHED, self.seq + 1
        logging.info(f"client status is established.")

        logging.debug(f"third link data is \n {tcp}")
        sent(socket, tcp)

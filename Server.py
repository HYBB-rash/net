# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   Server.py
@Time    :   2021/07/05 13:40:50
@Author  :   hyong 
@Version :   1.0
@Contact :   hyong_cs@outlook.com
"""
# here put the import lib

import logging
import time
import random
from multiprocessing import Process
from GlobalVar import recv, sent
from TcpPackage import get_tcp_package


CLOSE = 0
LISTEN = 1
SYNRCVD = 2
ESTABLISHED = 3


class Server(Process):
    def __init__(self, socket: str, interval: int) -> None:
        Process.__init__(self)
        self.interval = interval

        self.status = CLOSE
        try:
            ip, port = socket.split(":")[0], socket.split(":")[1]
        except Exception:
            logging.error("Split socket error!")
            ip, port = "0.0.0.0", "-1"

        self.ip = ip
        self.port = int(port)
        self.links = dict()

        self.seq = 1

    def get_socket(self) -> str:
        return self.ip + ":" + str(self.port)

    def run(self):
        self.start_service()

    def start_service(self):

        self.status = LISTEN

        while True:
            # // logging.debug('start get data from line')
            data = recv(self.get_socket())
            if data is None:
                sleep_time = random.randint(0, 5)
                time.sleep(sleep_time)
                continue
            else:
                sent(self.get_socket(), None)
                self.start_tcp_link(data)

    def start_tcp_link(self, data: dict):
        # // logging.info('start tcp link')
        if data["SYN"] == 1:
            self.return_ack(data)
        elif data["ACK"] == 1:
            self.establish_link(data)

    def return_ack_tcp(self, data: dict) -> dict:
        """获取第二次握手的报文

        Args:
            data (dict): 第一次握手的报文

        Returns:
            dict: 返回第二次握手的报文
        """
        tcp = get_tcp_package()

        x = data["seq"]
        tcp["SYN"], tcp["ACK"] = 1, 1
        tcp["seq"], tcp["ack"] = self.seq, x + 1
        tcp["src_port"], tcp["dest_port"] = self.port, data["src_port"]
        tcp["src_ip"] = self.ip

        return tcp

    def return_ack(self, data: dict):
        """第二次握手的报文

        Args:
            data (dict): 第一次握手的报文
        """
        logging.info("start first syn try")

        tcp = self.return_ack_tcp(data)

        logging.debug(f"return_ack tcp data is \n {tcp}")

        src_socket = data["src_ip"] + ":" + str(data["src_port"])

        self.seq, self.status = self.seq + 1, SYNRCVD
        self.links[data['src_ip'] + ":" + str(data['src_port'])] = SYNRCVD
        logging.info(f"server status is SYNRCVD.")
        logging.debug(f'link list: {self.links}')

        sent(src_socket, tcp)

    def establish_link(self, data: dict):
        """第三次握手

        Args:
            data (dict): 第三次握手的报文
        """
        self.status = ESTABLISHED
        self.links[data['src_ip'] + ":" + str(data['src_port'])] = ESTABLISHED
        logging.debug(f'link list: {self.links}')
        
        logging.info(f"server status is ESTABLISHED.")
        self.status = LISTEN


#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   TcpPackage.py
@Time    :   2021/07/05 10:57:28
@Author  :   hyong 
@Version :   1.0
@Contact :   hyong_cs@outlook.com
'''
# here put the import lib

def get_tcp_package():
    return {
        'src_port': 0, 'dest_port': 0, 'seq': 0,

        'ACK': 0, 'RST': 0, 'SYN': 0, 'ack': 0,

        'content': None, 'src_ip': None
    }

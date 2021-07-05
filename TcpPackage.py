
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
        'src_port': 0, 'dest_port': 0,

        'seq': 0,

        'check_num': 0,

        'data_bias': 0, 'not_use': 0, 'URG': 0,
        'ACK': 0, 'PSH': 0, 'RST': 0, 'SYN': 0,
        'FIN': 0, 'windows': 0, 'ack': 0,

        'check_sum': 0, 'urg_point': 0,

        'option': 0, 'space': 0,
        'content': None, 'src_ip': None
    }

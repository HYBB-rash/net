# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   global.py
@Time    :   2021/07/05 15:02:22
@Author  :   hyong 
@Version :   1.0
@Contact :   hyong_cs@outlook.com
'''
# here put the import lib

import logging
import json


def recv(socket: str):
    trans_data = json.load(open('line.json', 'r', encoding='utf-8'))
    # // logging.debug(f'my line is {mess_line}')
    return trans_data.get(socket, None)


def sent(socket: str, data: dict):
    trans_data = json.load(fp=open('line.json', 'r', encoding='utf-8'))
    logging.debug(f'set data {data}')
    trans_data[socket] = data
    json.dump(trans_data, open('line.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=4)
    logging.debug(f'trans data save')

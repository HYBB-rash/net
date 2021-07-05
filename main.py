
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2021/07/05 14:24:17
@Author  :   hyong 
@Version :   1.0
@Contact :   hyong_cs@outlook.com
'''
# here put the import lib

# import multiprocessing
import json
import time
from Client import Client
from Server import Server

import logging
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)



if __name__ == '__main__':
    logging.info('clear tmp data')
    null_data = {}
    json.dump(null_data, open('line.json', 'w', encoding='utf-8'), ensure_ascii=False)
    
    logging.info('start after 1 seconds ')
    time.sleep(1)
    s = Server('127.0.0.1:7890', 2)
    logging.info('start run server')
    s.start()
    logging.info('start run client')
    c = Client(2, '192.168.196.169', '127.0.0.1:7890')
    c.start()

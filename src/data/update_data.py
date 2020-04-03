#coding: utf8
'''
Created on 2020年1月30日
'''

import sys
sys.path.append('..')
sys.path.append('../..')
import time
import threading
import traceback
from src.libs.log import L
from src.data.dxy_record import *

    
def worker():
    try:
        request_data_province()
        request_rumor_data()
        request_news_data()
        L.info("Sleep now, worker will run after 30 minutes")
    except Exception as e:
        L.info("Someting went wrong because {}".format(str(e)))
        
def run():
    while True:
        t = threading.Thread(target=worker)
        t.start()
        time.sleep(18000)
    
if __name__ == '__main__':
    run()

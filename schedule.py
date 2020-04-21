# /usr/env/bin/python3
# -*-coding: utf-8 -*-
import time
from config import *
from database import Redis_conn
from pooladd import Pool_add
from tester import Valid_tester
from multiprocessing import Process


class Schedule(object):
    @staticmethod
    def valid_test(cycle=VALID_CHECK_CYCLE):
        database = Redis_conn()
        tester = Valid_tester()

        while True:
            print('****test valid proxy is work****')
            proxies_count = database.list_len
            if proxies_count == 0:
                print('>>>>>>wait for add>>>>>>')
                time.sleep(cycle)
                continue
            proxies = database.get_l(proxies_count // 2)
            tester.set_row(proxies)
            tester.test()
            time.sleep(cycle)

    @staticmethod
    def check_to_add(lower_threshold=POOL_LOWER_THRESHOLD,
                     upper_threshold=POOL_UPPER_THRESHOLD,
                     cycle=POOL_CHECK_ADD_CYCLE):
        database = Redis_conn()
        adder = Pool_add(upper_threshold)

        while True:
            if database.list_len < lower_threshold:
                print('>>>>>>pool is adding>>>>>>')
                adder.add_to_pool()
            time.sleep(cycle)

    def run(self):
        valid_process = Process(target=Schedule.valid_test)
        check_process = Process(target=Schedule.check_to_add)
        valid_process.start()
        check_process.start()


if __name__ == '__main__':
    s = Schedule()
    s.run()
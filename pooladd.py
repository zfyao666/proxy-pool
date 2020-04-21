# /usr/env/bin/python3
# -*-coding: utf-8 -*-

from crawl import crawl
from database import Redis_conn
from tester import Valid_tester


class Pool_add(object):
    def __init__(self, threshold):
        self._db = Redis_conn()
        self._tester = Valid_tester()
        self._crawl = crawl()
        self._threshold = threshold

    def is_full(self):
        if self._db.list_len < self._threshold:
            return True
        else:
            return False

    def add_to_pool(self):
        while self.is_full():
            try:
                for function_name in self._crawl.functions_name:
                    proxies = self._crawl.get_proxies(function_name)
                    self._tester.set_row(proxies)
                    self._tester.test()
                    if not self.is_full():
                        print('pool is full, wait for use')
                        break
            except (TypeError, ValueError) as error:
                print(error)
# /usr/env/bin/python3
# -*-coding: utf-8 -*-

from redis import StrictRedis
from config import *


class Redis_conn(object):

    def __init__(self, host=HOST, password=PASSWORD):
        if password:
            self.__db = StrictRedis(host=host, password=password)
        else:
            self.__db = StrictRedis(host=host)

    def get_l(self, count):
        proxies = self.__db.lrange('proxy-pool', 0, count-1)
        self.__db.ltrim('proxy-pool', count, -1)
        return proxies

    def put(self, proxy):
        self.__db.rpush('proxy-pool', proxy)

    def get_r(self):
        try:
            return self.__db.rpop('proxy-pool')
        except:
            print('proxy-pool is empty')

    @property
    def list_len(self):
        return self.__db.llen('proxy-pool')

    @property
    def pop(self):
        try:
            return self.__db.lindex('proxy-pool', -1)
        except:
            return ' '

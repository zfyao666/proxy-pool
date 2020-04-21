# /usr/env/bin/python3
# -*-coding: utf-8 -*-
from config import *
from fake_useragent import UserAgent
import asyncio
import aiohttp
from database import Redis_conn
# 从aiohttp调用错误处理的库
from aiohttp import ClientProxyConnectionError as ProxyConnectionError, \
                    ClientResponseError, ClientConnectionError, ServerConnectionError
# 从asyncio调用超时错误的库
from asyncio import TimeoutError


class Valid_tester(object):

    def __init__(self):
        self.__row = list()
        self.test_url = TEST_URL
        self._redis = Redis_conn()

    def set_row(self, proxies):
        self.__row = proxies

    async def proxy_test(self, proxy):
        try:
            async with aiohttp.ClientSession() as session:
                if isinstance(proxy, bytes):
                    proxy = proxy.decode()
                proxy_url = 'http://{}'.format(proxy)
                print('test:', proxy)
                try:
                    async with session.get(self.test_url, proxy=proxy_url, timeout=TIME_OUT) as response:
                        if response.status == 200:
                            self._redis.put(proxy)
                            print('valid proxy {}'.format(proxy))
                except (TimeoutError, ValueError, ProxyConnectionError):
                    print('Invalid proxy {}'.format(proxy))
                    pass
        except (ClientResponseError, ClientConnectionError, ServerConnectionError) as error:
            print(error)
            pass

    def test(self):
        loop = asyncio.get_event_loop()
        tasks = [self.proxy_test(proxy) for proxy in self.__row]
        loop.run_until_complete(asyncio.wait(tasks))

# /usr/env/bin/python3
# -*-coding: utf-8 -*-
import time

from fake_useragent import UserAgent

from tools import get_text
import re
from bs4 import BeautifulSoup
import requests


class CrawlMetaclass(type):
    def __new__(mcs, name, base, attrs):
        attrs['functions_name'] = []
        for key, value in attrs.items():
            if 'crawl_' in key:
                attrs['functions_name'].append(key)
        return type.__new__(mcs, name, base, attrs)


class crawl(object, metaclass=CrawlMetaclass):

    def get_proxies(self, name):
        proxies = []
        for proxy in eval('self.{}()'.format(name)):
            proxies.append(proxy)
        return proxies

    # def crawl_one(self):
    #     url_one = 'http://www.iphai.com/free/ng'
    #     text = get_text(url_one)
    #     pattern = re.compile('<td>\s*(.*?)\s*</td>.*?<td>\s*(.*?)\s*</td>.*?</tr>', re.S)
    #     result = re.findall(pattern, text)
    #     for ip, port in result:
    #             proxy = ip + ':' + port
    #             yield proxy
    #
    # def crawl_two(self):
    #     url_two = 'http://www.iphai.com/free/wg'
    #     text = get_text(url_two)
    #     pattern = re.compile('<td>\s*(.*?)\s*</td>.*?<td>\s*(.*?)\s*</td>.*?</tr>', re.S)
    #     result = re.findall(pattern, text)
    #     for ip, port in result:
    #             proxy = ip + ':' + port
    #             yield proxy

    def crawl_three(self):
        for i in range(1, 4):
            url_three = 'https://www.xicidaili.com/nn/{}'.format(i)
            text = get_text(url_three)
            pattern = re.compile('</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>.*?</tr>', re.S)
            result = re.findall(pattern, text)
            for ip, port in result:
                proxy = ip + ':' + port
                yield proxy

    def crawl_four(self):
        for i in range(1, 4):
            url_four = 'https://www.kuaidaili.com/free/inha/{}'.format(i)
            text = get_text(url_four)
            soup = BeautifulSoup(text, 'lxml')
            ip = soup.find_all(attrs={'data-title': 'IP'})
            port = soup.find_all(attrs={'data-title': 'PORT'})
            for j in range(len(ip)):
                proxy = ip[j].string + ':' + port[j].string
                yield proxy
            time.sleep(1)


    def crawl_five(self):
        for i in range(3, 6):
            url_five = 'http://www.66ip.cn/{}.html'.format(i)
            text = get_text(url_five)
            pattern = re.compile('<tr><td>(.*?)</td><td>(.*?)</td>.*?</tr>', re.S)
            result = re.findall(pattern, text)
            for ip, port in result:
                if not ip == 'ip':
                    proxy = ip + ':' + port
                    yield proxy

    def crawl_six(self):
        for i in range(1, 3):
            url_six = 'https://www.freeip.top/?page={}'.format(i)
            text = get_text(url_six)
            pattern = re.compile('<tr><td>(.*?)</td><td>(.*?)</td>')
            result = re.findall(pattern, text)
            for ip, port in result:
                proxy = ip + ':' + port
                yield proxy

    def crawl_seven(self):
        for i in range(1, 3):
            url_seven = 'http://www.ip3366.net/free/?stype=1&page={}'.format(i)
            text = get_text(url_seven)
            pattern = re.compile('<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
            result = re.findall(pattern, text)
            for ip, port in result:
                proxy = ip + ':' + port
                yield proxy

    def crawl_eight(self):
        for country in ['China-02', 'China-03', 'China-04', 'Taiwan-01']:
            url_eight = 'https://premproxy.com/proxy-by-country/{}.htm'.format(country)
            text = get_text(url_eight)
            soup = BeautifulSoup(text, 'lxml')
            result = soup.find_all(attrs={'data-label': 'IP:port '})
            for tag in result:
                yield tag.string


if __name__ == '__main__':
    c = crawl()
    print(list(c.crawl_three()))
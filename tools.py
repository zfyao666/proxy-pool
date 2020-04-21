# /usr/env/bin/python3
# -*-coding: utf-8 -*-

import requests
from requests.exceptions import RequestException, ConnectionError, ReadTimeout
# 从fake_useragent调用UserAgent类
from fake_useragent import UserAgent


def get_text(url):
    base_headers = {
        'User-Agent': UserAgent().random,
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN, zh;q = 0.9'
    }
    try:
        response = requests.get(url, headers=base_headers)
        if response.status_code == 200:
            return response.content.decode('utf-8', 'ignore')
    except ReadTimeout:
        print('Timeout error!')
    except ConnectionError:
        print('connect error!')
    except RequestException:
        print('error!')


# /usr/env/bin/python3
# -*-coding: utf-8 -*-

from flask import Flask
from database import Redis_conn


def get_proxy():
    db = Redis_conn()
    return db.get_r().decode()


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h2>Welcome to Proxy Pool System</h2>'

@app.route('/get', methods=['GET'])
def get():
    proxy = get_proxy()
    return '<h1>{}</h1>'.format(proxy)

if __name__ =='__main__':
    app.run()
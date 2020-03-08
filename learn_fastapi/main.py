# !/usr/bin/python3
# coding: utf-8 
# @Author  : wenbin
# @Time    : 2019/12/30 下午3:19
# @Software: PyCharm
# @File    : fastapi_example.py
# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get('/')
# def index_get():
#     return {"hello": "world!"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

cou = 0
for i in range(1, 11):
    cou += 1
    print('cou', cou)

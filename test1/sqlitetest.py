# -*- coding = utf-8 -*-
# @Time : 2021/6/28 21:38
# @Author : lqw
# @File : sqlitetest.py
# @software : PyCharm

import sqlite3

conn = sqlite3.connect("test.db")       #打开或创建数据库文件

print("Open database successfully")

c = conn.cursor()

sql = ""

c.execute(sql)



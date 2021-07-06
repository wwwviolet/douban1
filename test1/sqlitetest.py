# -*- coding = utf-8 -*-
# @Time : 2021/6/28 21:38
# @Author : lqw
# @File : sqlitetest.py
# @software : PyCharm

import sqlite3

#1.连接数据库

# conn = sqlite3.connect("test.db")       #打开或创建数据库文件
#
# print("Open database successfully")
#
# #2.数据库建表
#
# c = conn.cursor()          #获取游标
#
# sql = '''
#     create table company
#         (id int primary key not null ,
#         name text not null ,
#         age int not null ,
#         address char(50) ,
#         salary real);
# '''
# c.execute(sql)             #执行sql
# conn.commit()              #提交数据库操作
# conn.close()               #关闭数据链接
#
# print("成功建表")


#3.插入数据
conn = sqlite3.connect("test.db")       #打开或创建数据库文件

print("Open database successfully")

c = conn.cursor()          #获取游标
sql1 = '''
    insert into company (id,name,age,address,salary)
        values (1,'张三','32','成都','8000');
'''

sql2 = '''
    insert into company (id,name,age,address,salary)
        values (2,'李四','22','成都','7000');
'''

c.execute(sql1)         #执行sql
c.execute(sql2)         #执行sql
conn.commit()              #提交数据库操作
conn.close()               #关闭数据链接

print("成功建表")



#4.查询数据
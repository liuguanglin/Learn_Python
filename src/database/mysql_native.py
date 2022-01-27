#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql

db = pymysql.connect(host='localhost', user='user1', password='123456', database='py_test')
cursor = db.cursor()


def create_table():
    cursor.execute('DROP TABLE IF EXISTS `user`')
    create_sql = """
    CREATE TABLE `user`  (
      `uid` int NOT NULL AUTO_INCREMENT,
      `name` varchar(50) NOT NULL,
      `gender` enum('M','F') ,
      `age` int,
      `last_update` timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      PRIMARY KEY (`uid`) )
    """
    cursor.execute(create_sql)
    print('Table has been created.')


def insert_data():
    insert_sql = """
    INSERT INTO `user`(name, gender, age) VALUES ('Tom', 'F', 25), ('Alice', 'M', 24), ('Clark', 'F', 30)
    """
    try:
        cursor.execute(insert_sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    else:
        print('Data has been added.')


def update_data():
    update_sql = 'UPDATE `user` SET age=29 where uid=3'
    try:
        cursor.execute(update_sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    else:
        print('Data has been updated.')


def del_data():
    del_sql = 'DELETE FROM `user` where uid=2'
    try:
        cursor.execute(del_sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    else:
        print('Data has been deleted.')


def fetch_data():
    fetch_sql = 'SELECT * FROM `user` ORDER BY name'
    try:
        cursor.execute(fetch_sql)
        results = cursor.fetchall()
        print('\nQuery results:')
        for data in results:
            print(f'Name: {data[1]}, Age: {data[3]}.')
    except Exception as e:
        print(e)


create_table()
insert_data()
update_data()
del_data()
fetch_data()
db.close()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://user1:123456@localhost/py_test', echo=True)
Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    birth = Column(DateTime)
    vip = Column(Enum('0', '1'))


Base.metadata.create_all(engine)

db_session = sessionmaker(bind=engine)
session = db_session()


def add_data():
    data1 = Customer(name='Ford', birth='1963-7-30', vip='1')
    data2 = [Customer(name='Ellen', birth='1998-1-26', vip='1'), Customer(name='Zack', birth='1985-10-15', vip='0')]
    session.add(data1)
    session.add_all(data2)
    session.commit()


def update_data():
    session.query(Customer).filter_by(id=1).update({Customer.vip: '0'})
    # get_data = session.query(Customer).filter_by(id=1).first()
    # get_data.vip = '0'
    session.commit()


def del_data():
    del_count = session.query(Customer).filter_by(id=3).delete()
    session.commit()
    print(f'已删除{del_count}条数据')


def fetch_data():
    results = session.query(Customer.name, Customer.birth).filter(Customer.id < 10, Customer.vip == '1').all()
    # filter_by只接受键值对参数，只适用于单表查询
    # results = session.query(Customer.name, Customer.birth).filter_by(vip='1').all()
    # 可以直接执行SQL语句
    # results = session.execute("select name,birth from customer where id<10 and vip='1'")
    for row in results:
        print(row.name, row.birth.strftime('%Y-%m-%d'))


add_data()
update_data()
del_data()
fetch_data()
session.close()

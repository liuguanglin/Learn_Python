#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('mysql+pymysql://user1:123456@localhost/py_test')
Base = declarative_base()


class Husband(Base):
    __tablename__ = 'husband'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    # uselist=False 使用标量而非列表形式加载记录，实现一对一关系
    wife = relationship('Wife', backref='husband', uselist=False)
    # wife = relationship('Wife', back_populates='husband', uselist=False)


class Wife(Base):
    __tablename__ = 'wife'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    spouse_id = Column(Integer, ForeignKey('husband.id'))
    # husband = relationship('Husband', back_populates='wife')


Base.metadata.create_all(engine)

db_session = sessionmaker(bind=engine)
session = db_session()


def init_data():
    m1, m2 = Husband(name='Charley'), Husband(name='Sam')
    w1, w2 = Wife(name='Celina'), Wife(name='Susan')
    w1.spouse_id = 1
    session.add_all([m1, m2, w1, w2])
    w1.husband = m1
    m2.wife = w2
    session.commit()


def get_data():
    man_data = session.query(Husband).filter(Husband.name == 'Sam').first()
    print("{}'s wife is {}.".format(man_data.name, man_data.wife.name))


init_data()
get_data()

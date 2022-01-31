#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('mysql+pymysql://user1:123456@localhost/py_test', echo=True)
Base = declarative_base()


class Country(Base):
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    # cities = relationship('City')
    # backref 只能在关系的一侧使用，将自动在另一侧建立关系
    # cities = relationship('City', backref='cntry')
    # back_populates建立双向关系，关系两侧需显式定义相关属性
    # cities = relationship('City', back_populates='cntry')


class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    country_id = Column(Integer, ForeignKey('country.id'))
    cntry = relationship('Country', backref='cities')
    # cntry = relationship('Country', back_populates='cities')


Base.metadata.create_all(engine)

db_session = sessionmaker(bind=engine)
session = db_session()


def init_data():
    cntry1, cntry2 = Country(name='Brazil'), Country(name='Turkey')
    city1, city2, city3 = City(name='Sao Paulo'), City(name='Rio'), City(name='Ankara')
    city1.country_id = city2.country_id = 1
    session.add_all([cntry1, cntry2])
    session.add_all([city1, city2, city3])
    cntry2.cities.append(city3)
    session.commit()


def get_data():
    get_country = session.query(Country).filter(Country.name == 'Brazil').first()
    print('{} cities relate to {}.'.format(len(get_country.cities), get_country.name))
    for c in get_country.cities:
        print(c.name)


init_data()
get_data()

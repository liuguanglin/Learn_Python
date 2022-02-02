#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('mysql+pymysql://user1:123456@localhost/py_test')
Base = declarative_base()

assoc_table = Table('stu_tch', Base.metadata, Column('sid', Integer, ForeignKey('student.id')),
                    Column('tid', Integer, ForeignKey('teacher.id')))


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    teachers = relationship('Teacher', secondary=assoc_table, backref='students')
    # teachers = relationship('Teacher', secondary=assoc_table, back_populates='students')


class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    # students = relationship('Student', secondary=assoc_table, back_populates='teachers')


Base.metadata.create_all(engine)
db_session = sessionmaker(bind=engine)
session = db_session()


def init_data():
    s1, s2, s3 = Student(name='Alice'), Student(name='Bob'), Student(name='Colin')
    t1, t2 = Teacher(name='Einstein'), Teacher(name='Newton')
    session.add_all([s1, s2, s3])
    s1.teachers.extend([t1, t2])
    s2.teachers.extend([t1, t2])
    t2.students.append(s3)
    session.commit()


def get_data():
    data_stu = session.query(Student).filter(Student.name == 'Alice').first()
    print("{}'s teachers: {}".format(data_stu.name, [t.name for t in data_stu.teachers]))
    data_tch = session.query(Teacher).filter_by(name='Newton').first()
    print("{}'s students: {}".format(data_tch.name, [t.name for t in data_tch.students]))


init_data()
get_data()

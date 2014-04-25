#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Unicode, ForeignKey, Date, Time


Base = declarative_base()

engine = create_engine('sqlite:///../shedule.db', echo=False)

Session = scoped_session(sessionmaker(bind=engine))

metadata = Base.metadata


class Teacher(Base):
    """
    Таблица Преподаватель
    Модель Учитель
    """

    __tablename__ = 'Teacher'

    id = Column(Integer, primary_key=True)
    lastname = Column(Unicode)
    name = Column(Unicode)
    otch = Column(Unicode)
    abspara = relationship("AbstractPara", backref="teacher", viewonly=False)

    #teacher = relationship("AbstractPara")
    #Подразумевается primaryjoin="and_(Teacher.id==AbstractPara.teach_id)"

    def __init__(self, lastname, name, otch):
        self.lastname = lastname
        self.name = name
        self.otch = otch



''' Устарело
class Week(Base):
    """
    Не используется
    Модель Неделя
    """
    __tablename__ = 'Week'

    id = Column(Integer, primary_key=True)
    is_even = Column(Boolean)
    days = relationship("Day", backref="week")

    def __init__(self, is_even):
        self.is_even = is_even

    def __repr__(self):
        return session.query(Week).filter_by(id=Day.week_id).first()


class Day(Base):
    """
    Не используются
    Модель день
    """
    __tablename__ = 'Day'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode)
    week_id = Column(Integer, ForeignKey('week.id'))

    def __init__(self, name, week_id):
        self.name = name
        self.week_id = week_id

    def __repr__(self):
        return '%s' % self.name
'''


class Discipline(Base):
    """
    Таблица Дисциплина
    Модель Дисциплина
    """
    __tablename__ = 'Discipline'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode)
    abspara = relationship("AbstractPara", backref="discipline", viewonly=False)

    def __init__(self, name):
        self.name = name


class Gruppa(Base):
    """
    Таблица Группа
    Модель Группа
    """
    __tablename__ = 'Gruppa'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode)
    abspara = relationship("AbstractPara", backref="gruppa", viewonly=False)

    def __init__(self, name):
        self.name = name


class AbstractPara(Base):
    """
    Таблица Прообразы пар
    Модель Абстрактная Пара
    """
    __tablename__ = 'AbstractPara'

    id = Column(Integer, primary_key=True)

    disc_id = Column(Integer, ForeignKey('Discipline.id'))
    teach_id = Column(Integer, ForeignKey('Teacher.id'))
    gruppa_id = Column(Integer, ForeignKey('Gruppa.id'))
    numberpara = Column(Integer)
    dayofweek = Column(Unicode)
    para = relationship("Para", backref="abstractpara", viewonly=False)

    def __init__(self, teacher, discipline, gruppa, numberpara, dayofweek):
        self.teacher = teacher
        self.discipline = discipline
        self.gruppa = gruppa
        self.numberpara = numberpara
        self.dayofweek = dayofweek

    #def __repr__(self):
        #pass
        #TODO доделать правильный вывод


class Para(Base):
    """
    Таблица Пара
    Модель Текущая пара
    """
    __tablename__ = 'Para'

    id = Column(Integer, primary_key=True)

    abspara_id = Column(Integer, ForeignKey('AbstractPara.id'))

    date = Column(Date)
    timebegin = Column(Time)
    timeend = Column(Time)

    def __init__(self, abstractpara, date, timebegin, timeend):
        self.abstractpara = abstractpara
        self.date = date
        self.timebegin = timebegin
        self.timeend = timeend

if __name__ == '__main__':
    Base.metadata.create_all(engine)

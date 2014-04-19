# coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, backref, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Unicode, ForeignKey, Date, MetaData, Boolean


Base = declarative_base()

engine = create_engine('sqlite:///../shedule.db', echo=True)

Session = scoped_session(sessionmaker(bind=engine))


class Teacher(Base):
    """
    Таблица Преподаватель
    Модель Учитель
    """

    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode)
    lastname = Column(Unicode)
    otch = Column(Unicode)

    def __init__(self, lastname, name, otch):
        self.name = name
        self.lastname = lastname
        self.otch = otch

    def __repr__(self):
        return '%s %s %s' % (self.lastname, self.name, self.otch)


class Week(Base):
    """
    Не используется
    Модель Неделя
    """
    __tablename__ = 'week'

    id = Column(Integer, primary_key=True)
    is_even = Column(Boolean)
    days = relationship("Day", backref="week")

    def __init__(self, is_even):
        self.is_even = is_even

    def __repr__(self):
        if self.is_even:
            return u'Неделя числитель'
        else:
            return u'Неделя знаменатель'


class Day(Base):
    """
    Не используются
    Модель день
    """
    __tablename__ = 'day'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode)
    week_id = Column(Integer, ForeignKey('week.id'))

    def __init__(self, name, week_id):
        self.name = name
        self.week_id = week_id

    def __repr__(self):
        if True:
            return u'%s Неделя числитель' % self.name
        else:
            return u'%s Неделя знаменатель' % self.name


class Discipline(Base):
    """
    Таблица Дисциплина
    Модель Дисциплина
    """
    __tablename__ = 'discipline'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Gruppa(Base):
    """
    Таблица Группа
    Модель Группа
    """
    __tablename__ = 'gruppa'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


Base.metadata.create_all(engine)




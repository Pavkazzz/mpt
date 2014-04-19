# coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, backref, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Unicode, ForeignKey, Date, MetaData, Boolean


Base = declarative_base()

engine = create_engine('sqlite:///shedule.db', echo=True)

Session = scoped_session(sessionmaker(bind=engine))


class Teacher(Base):
    """
    Модель Учитель
    """

    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode)
    lastname = Column(Unicode)
    otch = Column(Unicode)

    def __init__(self, name, lastname, otch):
        self.name = name
        self.lastname = lastname
        self.otch = otch

    def __repr__(self):
        return '%s %s %s' % (self.lastname, self.name, self.otch)


class Week(Base):
    """
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
            return 'Неделя числитель'
        else:
            return 'Неделя знаменатель'


class Day(Base):
    """
    Модель день
    """
    __tablename__ = 'day'

    id = Column(Integer, primary_key=True)
    name = Column(Integer)
    week_id = Column(Integer, ForeignKey('week.id'))

    def __init__(self, name, week_id):
        self.name = name
        self.week_id = week_id


Base.metadata.create_all(engine)




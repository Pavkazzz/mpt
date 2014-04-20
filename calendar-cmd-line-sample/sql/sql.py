# coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, backref, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Unicode, ForeignKey, Date, Boolean


Base = declarative_base()

engine = create_engine('sqlite:///../shedule.db', echo=True)

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
    teacher = relationship("AbstractPara", backref="Teacher")

    def __init__(self, lastname, name, otch):
        self.lastname = lastname
        self.name = name
        self.otch = otch

    def __repr__(self):
        return '%s %s %s' % (self.lastname, self.name, self.otch)

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
    disc = relationship("AbstractPara", backref="Discipline")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Gruppa(Base):
    """
    Таблица Группа
    Модель Группа
    """
    __tablename__ = 'Gruppa'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode)
    gruppa = relationship("AbstractPara", backref="Gruppa")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


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


    def __init__(self, disc_id, teach_id, gruppa_id):
        self.disc_id = disc_id
        self.teach_id = teach_id
        self.gruppa_id = gruppa_id

    def __repr__(self):
        #tempteach = session.query(Teacher).filter_by(id=AbstractPara.teach_id).first()
        #tempdisc = session.query(Discipline).filter_by(id=AbstractPara.disc_id).first()
        #tempgruppa = session.query(Gruppa).filter_by(id=AbstractPara.gruppa_id).first()
        #yield '%s, %s, %s' % (tempgruppa.name, tempdisc.name, tempteach.lastname)
        return self.id


Base.metadata.create_all(engine)




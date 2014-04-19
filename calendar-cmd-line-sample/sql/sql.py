# coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Unicode, Date, MetaData, Boolean


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

Base.metadata.create_all(engine)




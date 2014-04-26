# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

def main():
    engine = create_engine('sqlite:///../shedule.db', echo=False)

    Session = scoped_session(sessionmaker(bind=engine))

    return Session

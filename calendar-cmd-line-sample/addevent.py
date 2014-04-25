# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sql.sql import Para, Session
import sample
import sys
import datetime

engine = create_engine('sqlite:///shedule.db', echo=False)

Session = scoped_session(sessionmaker(bind=engine))

session = Session()

sqlpara = session.query(Para).all()

service = sample.init(sys.argv)

for para in sqlpara:
    try:
        print("Success! Now add code here.")

        start = sample.time_to_atom(para.date.year, para.date.month, para.date.day, para.timebegin.hour, para.timebegin.minute)
        end = sample.time_to_atom(para.date.year, para.date.month, para.date.day, para.timeend.hour, para.timeend.minute)

        sample.add_event(service, start, end, para.abstractpara.discipline.name, trace=True)


        sample.print_events(service, trace=False)

    except sample.client.AccessTokenRefreshError:
        print("The credentials have been revoked or expired, please re-run"
              "the application to re-authorize")
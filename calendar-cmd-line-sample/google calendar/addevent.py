# -*- coding: utf-8 -*-
import sys

from sql.sql import Para
import sqlcalendar
import sample
import getcalendar
import datetime


Session = sqlcalendar.main()

session = Session()

sqlpara = session.query(Para).all()

service = sample.init(sys.argv)

gruppadict = getcalendar.getcalendar()

for para in sqlpara:
    try:

        start = sample.time_to_atom(para.date.year, para.date.month, para.date.day, para.timebegin.hour,
                                    para.timebegin.minute)
        end = sample.time_to_atom(para.date.year, para.date.month, para.date.day, para.timeend.hour,
                                  para.timeend.minute)

        for gruppa in gruppadict:
            if gruppa == para.abstractpara.gruppa.name and \
                            para.abstractpara.numberweek == \
                            (int(datetime.datetime.strftime(
                                    datetime.date(para.date.year, para.date.month, para.date.day), '%W')) % 2):
                print("Success! New event %s, %s") % (para.abstractpara.gruppa.name, para.abstractpara.discipline.name)

                sample.add_event(service, start, end, para.abstractpara.discipline.name, trace=True,
                                 from_who=gruppadict[gruppa])
                print para.abstractpara.numberweek, gruppadict[gruppa]
                #sample.print_events(service, trace=False)

    except sample.client.AccessTokenRefreshError:
        print("The credentials have been revoked or expired, please re-run"
              "the application to re-authorize")
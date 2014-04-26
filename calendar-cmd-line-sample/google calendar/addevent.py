# -*- coding: utf-8 -*-
import sys

from sql.sql import Para
import sqlcalendar
import sample
import getcalendar



Session = sqlcalendar.main()

session = Session()

sqlpara = session.query(Para).all()

service = sample.init(sys.argv)

for para in sqlpara:
    try:
        print("Success! Now add code here.")

        start = sample.time_to_atom(para.date.year, para.date.month, para.date.day, para.timebegin.hour, para.timebegin.minute)
        end = sample.time_to_atom(para.date.year, para.date.month, para.date.day, para.timeend.hour, para.timeend.minute)

        for gruppa, calendar_id in getcalendar.getcalendar():
            sample.add_event(service, start, end, para.abstractpara.discipline.name, trace=True, from_who=calendar_id)

        sample.print_events(service, trace=False)

    except sample.client.AccessTokenRefreshError:
        print("The credentials have been revoked or expired, please re-run"
              "the application to re-authorize")
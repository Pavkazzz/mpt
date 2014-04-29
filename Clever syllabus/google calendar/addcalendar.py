# -*- coding: utf-8 -*-
import sys

import sqlcalendar
import sample
from sql.sql import Gruppa


Session = sqlcalendar.main()
session = Session()
sqlgruppa = session.query(Gruppa).all()
service = sample.init(sys.argv)

for gruppa in sqlgruppa:
    calendar = {
        'summary': gruppa.name,
        'timeZone': 'Europe/Moscow'
    }

    created_calendar = service.calendars().insert(body=calendar).execute()

    print created_calendar['id']

# -*- coding: utf-8 -*-
import getcalendar
import sys
import sample

service = sample.init(sys.argv)
gruppalist = getcalendar.getcalendar()

for gruppa, calendarid in gruppalist:
    page_token = None
    while True:
        events = service.events().list(calendarId=calendarid, pageToken=page_token).execute()
        for event in events['items']:
            service.events().delete(calendarId=calendarid, eventId=event['id']).execute()
            print 'yes', gruppa
        page_token = events.get('nextPageToken')
        if not page_token:
            break
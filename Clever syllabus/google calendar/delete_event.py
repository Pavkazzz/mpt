# -*- coding: utf-8 -*-
import getcalendar
import sys
import sample

service = sample.init(sys.argv)
gruppadict = getcalendar.getcalendar()

for gruppa in gruppadict:
    page_token = None
    while True:
        events = service.events().list(calendarId=gruppadict[gruppa], pageToken=page_token).execute()
        for event in events['items']:
            service.events().delete(calendarId=gruppadict[gruppa], eventId=event['id']).execute()
            print 'yes', gruppa
        page_token = events.get('nextPageToken')
        if not page_token:
            break
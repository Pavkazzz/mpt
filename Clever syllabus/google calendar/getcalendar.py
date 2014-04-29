# -*- coding: utf-8 -*-
import sys
import sample

def getcalendar():

    service = sample.init(sys.argv)
    calendar_dict = {}
    page_token = None
    while True:
        calendar_list = service.calendarList().list(pageToken=page_token).execute()
        for calendar_list_entry in calendar_list['items']:

            if u'П-' in calendar_list_entry['summary']:
                calendar_dict[calendar_list_entry['summary']] = calendar_list_entry['id']

        page_token = calendar_list.get('nextPageToken')
        if not page_token:
            break

    return calendar_dict
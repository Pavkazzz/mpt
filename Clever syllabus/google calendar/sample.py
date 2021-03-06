# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Command-line skeleton application for Calendar API.
Usage:
  $ python sample.py

You can also get help on all the command-line flags the program understands
by running:

  $ python sample.py --help

"""

import argparse
import os
import sys
import datetime

import pytz
from apiclient import discovery

import my_rfc3339
import httplib2
from oauth2client import file
from oauth2client import client
from oauth2client import tools



# Parser for command-line arguments.
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[tools.argparser])


# CLIENT_SECRETS is name of a file containing the OAuth 2.0 information for this
# application, including client_id and client_secret. You can see the Client ID
# and Client secret on the APIs page in the Cloud Console:
# <https://cloud.google.com/console#/project/784493703292/apiui>
CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), 'client_secrets.json')

# Set up a Flow object to be used for authentication.
# Add one or more of the following scopes. PLEASE ONLY ADD THE SCOPES YOU
# NEED. For more information on using scopes please see
# <https://developers.google.com/+/best-practices>.
FLOW = client.flow_from_clientsecrets(CLIENT_SECRETS,
                                      scope=[
                                          'https://www.googleapis.com/auth/calendar',
                                          'https://www.googleapis.com/auth/calendar.readonly',
                                      ],
                                      message=tools.message_if_missing(CLIENT_SECRETS))


def print_events(service, trace=False):
    """
    Выводит все события из календаря
    :param service: Объект api календаря
    """
    page_token = None
    while True:
        events = service.events().list(calendarId='primary', pageToken=page_token).execute()
        for event in events['items']:
            if trace:
                print(event)
            try:
                print event['summary']
            except KeyError:
                print 'У события нет названия'
        page_token = events.get('nextPageToken')
        if not page_token:
            break


def add_event(service, start, end, summary, calendar_id='primary', from_who='Pavkairl@gmail.com', trace=False):
    """
    Добавляет событие в календарь
    :param service: Объект api календаря
    :param calendar_id: Имя календаря
    :param summary: Название события
    :param from_who: От кого (авторизация)
    :param start: Время АТОМ начало
    :param end: Время АТОМ конец
    """

    event = {
        'summary': summary,
        'start': {
            'dateTime': start,
            'timeZone': 'Europe/Moscow'
        },
        'end': {
            'dateTime': end,
            'timeZone': 'Europe/Moscow'
        },
        'maxAttendees': 0

    }

    if trace:
        print event
    try:
        created_event = service.events().insert(calendarId=from_who, body=event).execute()
    except:
        print 'Ошибка выполнения запроса'

    else:
        print 'Done:' + created_event['id']


def para_minute(para):
    pass


def time_to_atom(year, month, day, hour, minute):
    return my_rfc3339.rfc3339(datetime.datetime(year, month, day, hour, minute, tzinfo=pytz.timezone('Etc/GMT-4')))
    #2014-04-12T16:30:00.000+04:00
    #что-то типа такого


def init(argv):
    # Parse the command-line flags.
    flags = parser.parse_args(argv[1:])
    storage = file.Storage('sample.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = tools.run_flow(FLOW, storage, flags)
    # Create an httplib2.Http object to handle our HTTP requests and authorize it
    # with our good Credentials.
    http = httplib2.Http()
    http = credentials.authorize(http)
    # Construct the service object for the interacting with the Calendar API.
    service = discovery.build('calendar', 'v3', http=http)
    return service


def main(argv):
    service = init(argv)

    try:
        print("Success! Now add code here.")

        start = time_to_atom(2014, 4, 13, 18, 0)
        end = time_to_atom(2014, 4, 13, 19, 30)

        add_event(service, start, end, 'Проверка добавления', trace=True)

        print_events(service, trace=False)

    except client.AccessTokenRefreshError:
        print("The credentials have been revoked or expired, please re-run"
              "the application to re-authorize")


# For more information on the Calendar API you can visit:
#
#   https://developers.google.com/google-apps/calendar/firstapp
#
# For more information on the Calendar API Python library surface you
# can visit:
#
#   https://developers.google.com/resources/api-libraries/documentation/calendar/v3/python/latest/
#
# For information on the Python Client Library visit:
#
#   https://developers.google.com/api-client-library/python/start/get_started
if __name__ == '__main__':
    main(sys.argv)

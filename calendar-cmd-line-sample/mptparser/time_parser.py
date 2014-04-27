# -*- coding: utf-8 -*-

#from BeautifulSoup import BeautifulSoup
import urllib2
from mptparser import script_table
import datetime



html_doc = urllib2.urlopen('http://mpt.ru/education/allocation.php?otdel=3&group=6').read()
#Рассписание звонков


def timeparse(numberpara, weekday):
    if weekday == 5:
        res = script_table.parse_tables(html_doc, [2], 1)
    else:
        res = script_table.parse_tables(html_doc, [1], 1)

    time = res[1][0].replace('\n', ' ').replace(' ', '')
    newtime = time[(numberpara - 1) * 11:11 * numberpara].split('-')
    return datetime.time(hour=int(newtime[0][:2]), minute=int(newtime[0][3:])), datetime.time(hour=int(newtime[1][:2]),
                                                                                                  minute=int(
                                                                                                      newtime[1][3:]))


if __name__ == '__main__':
    start, end = timeparse(4, 5)
    res2 = script_table.parse_tables(html_doc, [2], 1)

    print start, end
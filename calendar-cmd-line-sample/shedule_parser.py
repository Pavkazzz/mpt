# -*- coding: utf-8 -*-

import urllib2
import script_table

html_doc = urllib2.urlopen('http://mpt.ru/education/allocation/alloc_2203_p329.htm').read()

#Рассписание занятий
res = script_table.parse_tables(html_doc, [0,1], 0)

for item in res:
    for item2 in item:
        item2 = item2.replace('\r\n','')
        print item2.encode('utf-8')





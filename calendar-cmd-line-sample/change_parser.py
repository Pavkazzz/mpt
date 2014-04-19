# -*- coding: utf-8 -*-

import urllib2
import script_table

html_doc = urllib2.urlopen('http://mpt.ru/education/changes.php?gr_name=%D0%9F%D0%9A-319').read()

#Рассписание изменить
res = script_table.parse_tables(html_doc, [1, 2, 3, 4, 5], 1)

for item in res:
    for item2 in item:
        print item2.encode('utf-8')




# -*- coding: utf-8 -*-

#from BeautifulSoup import BeautifulSoup
import urllib2
import script_table

html_doc = urllib2.urlopen('http://mpt.ru/education/allocation.php?otdel=3&group=6').read()


#Рассписание звонков
res = script_table.parse_tables(html_doc, [1, 2, 3, 4, 5], 1)

for item in res:
    for item2 in item:
        print item2.encode('utf-8')




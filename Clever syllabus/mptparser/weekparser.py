# -*- coding: utf-8 -*-
import urllib2

def weekparser():

    html_doc = urllib2.urlopen('http://mpt.ru/education/allocation.php?otdel=3&group=6')

    for item in html_doc:
        if '<font style="font-size: 18px" color=#ff0000>' in item:
            return item.split('<font style="font-size: 18px" color=#ff0000>')[1].split('</font>')[0]
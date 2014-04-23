# -*- coding: utf-8 -*-
from sql import AbstractPara, Para, Teacher, Discipline, Gruppa, Session
from excel_parser.teacherparser import createteacherlist
import xlrd

session = Session()


book = xlrd.open_workbook('../excel_parser/2203_Raspisanie.xls')
teacherlist = createteacherlist(book)

for person in teacherlist:
    print u'Имя: %s' % person[:2]
    print u'Отчество: %s' % person [2:4]
    print u'Фамилия: %s' % person [5:]

'''
teach = Teacher(u'Караваев', u'Сергей', u'Владимирович')
session.add(teach)

session.commit()
'''
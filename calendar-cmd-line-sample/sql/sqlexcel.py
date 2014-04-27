# -*- coding: utf-8 -*-
import sys
sys.path.append("../excel_parser")
from sql import Teacher, Discipline, Gruppa, Session
from excel_parser.teacherparser import createteacherlist
from excel_parser.disciplineparse import createdisciplinelist
from excel_parser.gruppaparser import creategrupplist
import xlrd



session = Session()


book = xlrd.open_workbook('2203_Raspisanie.xls')
teacherlist = createteacherlist(book)

for person in teacherlist:
    #print u'Имя: %s' % person[:2]
    #print u'Отчество: %s' % person [2:4]
    #print u'Фамилия: %s' % person [5:]

    sqlteach = Teacher(person[5:], person[:2], person[2:4])
    session.add(sqlteach)

disciplinelist = createdisciplinelist(book)
for disc in disciplinelist:
    #print u'Дисциплина: %s' % disc

    sqldisc = Discipline(disc)
    session.add(sqldisc)

grupplist = creategrupplist(book)

for gruppa in grupplist:
    #print u'Группа: %s' % gruppa

    sqlgruppa = Gruppa(gruppa)
    session.add(sqlgruppa)

session.commit()
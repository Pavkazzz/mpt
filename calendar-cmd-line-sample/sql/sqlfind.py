# -*- coding: utf-8 -*-
from sql import *
from excel_parser.excel import excellist
import xlrd

book = xlrd.open_workbook('../2203_Raspisanie.xls')
excel = excellist(book)

week = [u'понедельник', u'вторник', u'среда', u'четверг', u'пятница', u'суббота']

session = Session()
sqlteacher = session.query(Teacher).all()
sqldiscipline = session.query(Discipline).all()
sqlgruppa = session.query(Gruppa).all()

for para in excel:
    teacherid = 0
    disciplineid = 0
    gruppaid = 0
    for teacher in sqlteacher:
        if teacher.lastname in para:
            print '%s: %s' % (teacher.id, teacher.lastname)
            teacherstate = teacher

    for discipline in sqldiscipline:
        if discipline.name in para:
            print '%s: %s' % (discipline.id, discipline.name)
            disciplinestate = discipline

    for gruppa in sqlgruppa:
        if gruppa.name in para:
            print '%s: %s' % (gruppa.id, gruppa.name)
            gruppastate = gruppa

    for days in week:
        if days in para:
            print days
            daysofweek = days

    numberweek = int(para[-2])
    #print para[-2]
    #Узнаем номер пары
    numberpara = int(para[-1])

    sqlabspara = AbstractPara(teacherstate, disciplinestate, gruppastate, numberpara, daysofweek, numberweek)
    session.add(sqlabspara)

session.commit()
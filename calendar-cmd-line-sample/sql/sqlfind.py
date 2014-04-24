# -*- coding: utf-8 -*-
from sql import *
from excel_parser.excel import numerator, denominator
import xlrd

book = xlrd.open_workbook('../excel_parser/2203_Raspisanie.xls')
excel = numerator(book)  #Числитель
#excel = denominator(book) #Знаменатель


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

    sqlabspara = AbstractPara(teacherstate, disciplinestate, gruppastate)
    session.add(sqlabspara)

session.commit()
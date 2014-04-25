# -*- coding: utf-8 -*-
import xlrd

book = xlrd.open_workbook('2203_Raspisanie.xls')

#for teacher in teacherlist:
    #print teacher
array = []
sheet = book.sheet_by_index(2)
for row_index in range(9, sheet.nrows, 14):
     col_index = 0
     cells = sheet.cell(row_index, col_index)
     array.append((cells.value.replace('\n',''), row_index))

for item in array:
    print item
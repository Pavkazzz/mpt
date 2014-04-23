# -*- coding: utf-8 -*-
import xlrd
import re
#from sql import Teacher, Session


book = xlrd.open_workbook('2203_Raspisanie.xls')

disciplinelist = []

#for num in range(0, book._all_sheets_count):
sheet = book.sheet_by_index(2)

for row_index in xrange(11, sheet.nrows-3):

    for col_index in [2]: #5


        #col_index = 5  # 5 для 29 групп; 2 для 19 групп
        cells = sheet.cell(row_index, col_index)

        if isinstance(cells.value, float):
            continue

        teacher = re.split(ur'[А-я]\.\s*[А-я]\.\s*[-А-я]+', cells.value, flags=re.UNICODE)
        if not u'БИРЮЛЕВО' in teacher and not u'БИБЛИОТЕЧНЫЙ ДЕНЬ' in teacher:
            for item in teacher:
                if item not in disciplinelist and u',' not in item:
                    disciplinelist.append(item)

for discipline in disciplinelist:
    print discipline
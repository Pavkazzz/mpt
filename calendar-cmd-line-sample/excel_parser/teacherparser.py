# -*- coding: utf-8 -*-

import xlrd
import re
#from sql import Teacher, Session


book = xlrd.open_workbook('2203_Raspisanie.xls')

for num in range(0, book._all_sheets_count):
    sheet = book.sheet_by_index(num)

    for row_index in range(11, sheet.nrows):
    #for col_index in range(sheet.ncols):
        col_index = 5  # 5 для 29 групп; 2 для 19 групп
        cells = sheet.cell(row_index, col_index)

        if isinstance(cells.value, float):
            continue

        teacher = re.findall(ur'[А-я]\.\s*[А-я]\.\s*[-А-я]+', cells.value, flags=re.UNICODE)
        for item in teacher:
            print item.encode('utf-8')

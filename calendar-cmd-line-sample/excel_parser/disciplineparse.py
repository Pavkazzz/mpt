# -*- coding: utf-8 -*-
import xlrd
import re


def createdisciplinelist(book):
    disciplinelist = []

    for num in range(0, book._all_sheets_count):
        sheet = book.sheet_by_index(num)

        for row_index in xrange(11, sheet.nrows - 3):
            for col_index in [2, 5]:  # 5 для 29 групп; 2 для 19 групп
                cells = sheet.cell(row_index, col_index)

                if isinstance(cells.value, float):
                    continue

                disc = re.split(ur'[А-я]\.\s*[А-я]\.\s*[-А-яё]+', cells.value, flags=re.UNICODE)

                if not [u'БИРЮЛЕВО', u'БИБЛИОТЕЧНЫЙ ДЕНЬ'] in disc:
                    for item in disc:
                        newitem = item.rstrip(' ')
                        if newitem not in disciplinelist and newitem not in [u',', u'', u'ПРАКТИКА']:
                            disciplinelist.append(newitem)

    return disciplinelist

if __name__ == '__main__':

    book = xlrd.open_workbook('../2203_Raspisanie.xls')

    disciplinelist = createdisciplinelist(book)
    for discipline in disciplinelist:
        print discipline
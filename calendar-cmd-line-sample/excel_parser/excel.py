# -*- coding: utf-8 -*-

import xlrd
import re

book = xlrd.open_workbook('2203_Raspisanie.xls')

sheet = book.sheet_by_index(2)

#print sheet.name
#print sheet.nrows
#print sheet.ncols


def numerator(sheet):
    """
    неделя числитель
    Расхуяриваем таблицу для числителя
    :param sheet: excel таблица
    """
    array = []
    for row_index in range(11, sheet.nrows):
        #for col_index in range(sheet.ncols):
        col_index = 5  # 5 для 29 групп
        cells = sheet.cell(row_index, col_index)

        if isinstance(cells.value, float) or cells.value == '':
            continue

        if row_index % 2 == 1:
            #print sheet.cell(row_index, col_index - 1).value
            array.append(cells.value)


        #Фамилии и инициалы преподавателей: пример Т.В. Руденко
        if re.match(ur'^[А-я]\.\s*[А-я]\.\s*[-А-я]+', cells.value, re.UNICODE) is not None:
            array[len(array) - 1] += ' ' + cells.value
    for item in array:
        print item


def denominator(sheet):
    """
    Неделя знаменатель

    :param sheet: excel таблица
    """
    for row_index in range(11, sheet.nrows):
        #for col_index in range(sheet.ncols):
        col_index = 5
        cells = sheet.cell(row_index, col_index)

        if isinstance(cells.value, float):
            continue

        if row_index % 2 == 0:
            print cells.value
        else:
            if re.search(ur'[А-я]\.\s*[А-я]\.\s*[-А-я]+', cells.value, re.UNICODE) is None:
                print cells.value


if __name__ == '__main__':
    numerator(sheet)
    #denominator(sheet)

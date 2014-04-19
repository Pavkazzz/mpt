# -*- coding: utf-8 -*-

import xlrd
import re
from unicodedata import normalize

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
    for row_index in range(11, sheet.nrows):
        #for col_index in range(sheet.ncols):
        col_index = 5  # 5 для 29 групп
        cells = sheet.cell(row_index, col_index)

        if isinstance(cells.value, float):
            continue

        if row_index % 2 == 1:
            print cells.value
            print sheet.cell(row_index, col_index-1)


        #Фамилии и инициалы преподавателей: пример Т.В. Руденко
        if re.search(ur'^[А-я]\.\s*[А-я]\.\s*[-А-я]+', cells.value, re.UNICODE) is not None:
            print cells.value


def denominator(sheet):
    #TODO Сделать
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

        if row_index % 2 == 1:
            print cells.value

        if re.search(ur'^[А-я]\.\s*[А-я]\.\s*[-А-я]+', cells.value, re.UNICODE) is not None:
            print cells.value


if __name__ == '__main__':
    numerator(sheet)

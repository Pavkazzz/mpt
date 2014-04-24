# -*- coding: utf-8 -*-

import xlrd
import re

#print sheet.name
#print sheet.nrows
#print sheet.ncols


def valid(value):
    if isinstance(value, float) or value in ['', u'БИРЮЛЕВО', u'БИБЛИОТЕЧНЫЙ ДЕНЬ', u'ПРАКТИКА']:
        return False
    return True


def numerator(book):
    """
    неделя числитель
    Расхуяриваем таблицу для числителя
    :param book: excel таблица
    """
    array = []

    for num in range(0, book._all_sheets_count):
        sheet = book.sheet_by_index(num)

        for col_index in [2, 5]:  # 5 для 29 групп
            for row_index in range(11, sheet.nrows-3):
                cells = sheet.cell(row_index, col_index)

                if not valid(cells.value):
                    continue

                if row_index % 2 == 1:
                    #print sheet.cell(row_index, col_index - 1).value
                    array.append(cells.value + ' ' + sheet.cell(8, col_index).value)


                #Фамилии и инициалы преподавателей: пример Т.В. Руденко
                if re.match(ur'^[А-я]\.\s*[А-я]\.\s*[-А-яё]+', cells.value, re.UNICODE) is not None:
                    array[len(array) - 1] += ' ' + cells.value

    return array


def denominator(book):
    """
    Неделя знаменатель

    :param book: excel таблица
    """
    array = []

    for num in range(0, book._all_sheets_count):
        sheet = book.sheet_by_index(num)

        for col_index in [2, 5]:  # 5 для 29 групп
            for row_index in range(11, sheet.nrows-3):
                cells = sheet.cell(row_index, col_index)

                if not valid(cells.value):
                    continue

                if row_index % 2 == 0:
                    #Добавляем фамилии
                    if re.match(ur'[А-я]\.\s*[А-я]\.\s*[-А-яё]+', cells.value, flags=re.UNICODE):
                        array[len(array) - 1] += ' ' + cells.value + ' ' + sheet.cell(8, col_index).value

                    else:
                        #если пара уже из препода и предмета
                        array.append(cells.value + ' ' + sheet.cell(8, col_index).value) #TODO: Переделать нормально

                else:
                    #Добавляем предметы
                    if re.search(ur'[А-я]\.\s*[А-я]\.\s*[-А-я]+', cells.value, re.UNICODE) is None:
                        array.append(cells.value.lstrip(' '))

    return array

if __name__ == '__main__':
    book = xlrd.open_workbook('2203_Raspisanie.xls')
    excel = numerator(book)
    #excel = denominator(book)
    for item in excel:
        print item


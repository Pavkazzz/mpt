# -*- coding: utf-8 -*-

import xlrd


def creategrupplist(book):
    grupplist = []

    for num in range(0, book._all_sheets_count):
        sheet = book.sheet_by_index(num)
        row_index = 8

        for col_index in [2, 5]:  #col_index = 5  # 5 для 29 групп; 2 для 19 групп

            cells = sheet.cell(row_index, col_index)
            grupplist.append(cells.value)

    return grupplist

if __name__ == '__main__':

    book = xlrd.open_workbook('2203_Raspisanie.xls')
    grupplist = creategrupplist(book)
    for gruppa in grupplist:
        print gruppa
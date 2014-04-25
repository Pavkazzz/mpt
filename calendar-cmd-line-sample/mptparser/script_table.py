# -*- coding: utf-8 -*-

#Извлечение данных из заданных столбцов html-таблицы

#Данные: html-исходник любого сайта
#Аргументы: список заголовков или номера столбцов (начиная с нулевого)
#Результат: список данных по рядам

import libxml2dom


def parse_tables(source, headers, table_index):
    """headers может быть списком строк, если таблица содержит заголовки или
           headers может быть списком целых чисел, если заголовки не заданы. 
     
           Этот метод возвращает вложенные списки. 
        """

    #Determine if the headers list is strings or ints and make sure they
    #are all the same type
    j = 0

    #print 'Printing headers: ',headers

    #route to the correct function
    #if the header type is int
    if type(headers[0]) == type(1):

        #run no_header function
        return no_header(source, headers, table_index)

        #if the header type is string  
    elif type(headers[0]) == type('a'):

        #run the header_given function
        return header_given(source, headers, table_index)

    else:
        #return none if the headers aren't correct
        return None


        #This function takes in the source code of the whole page a string list of
    #headers and the index number of the table on the page. It returns a list of  
    #lists with the scraped information

def header_given(source, headers, table_index):
    #initiate a list to hole the return list
    return_list = []

    #initiate a list to hold the index numbers of the data in the rows
    header_index = []

    #get a document object out of the source code
    doc = libxml2dom.parseString(source, html=1)

    #get the tables from the document
    tables = doc.getElementsByTagName('table')

    try:
        #try to get focue on the desired table
        main_table = tables[table_index]
    except:
        #if the table doesn't exits then return an error
        return ['The table index was not found']

        #get a list of headers in the table  
    table_headers = main_table.getElementsByTagName('th')


    #need a sentry value for the header loop
    loop_sentry = 0

    #loop through each header looking for matches
    for header in table_headers:

        #if the header is in the desired headers list
        if header.textContent in headers:
            #add it to the header_index
            header_index.append(loop_sentry)

            #add one to the loop_sentry  
        loop_sentry += 1

        #get the rows from the table  
    rows = main_table.getElementsByTagName('tr')

    #sentry value detecting if the first row is being viewed
    row_sentry = 0

    #loop through the rows in the table, skipping the first row
    for row in rows:

        #if row_sentry is 0 this is our first row
        if row_sentry == 0:
            #make the row_sentry not 0
            row_sentry = 1337
            continue
            #get all cells from the current row  
        cells = row.getElementsByTagName('td')

        #initiate a list to append into the return_list
        cell_list = []

        #iterate through all of the header index's
        for i in header_index:
            #append the cells text content to the cell_list
            cell_list.append(cells[i].textContent)

            #append the cell_list to the return_list  
        return_list.append(cell_list)

        #return the return_list  
    return return_list

    #This function takes in the source code of the whole page an int list of  
    #headers indicating the index number of the needed item and the index number  
    #of the table on the page. It returns a list of lists with the scraped info  


def no_header(source, headers, table_index):
    #initiate a list to hold the return list
    return_list = []

    #get a document object out of the source code
    doc = libxml2dom.parseString(source, html=1)

    #get the tables from document
    tables = doc.getElementsByTagName('table')

    try:
        #Try to get focus on the desired table
        main_table = tables[table_index]
    except:
        #if the table doesn't exits then return an error
        return ['The table index was not found']

        #get all of the rows out of the main_table  
    rows = main_table.getElementsByTagName('tr')

    #loop through each row
    for row in rows:

        #get all cells from the current row
        cells = row.getElementsByTagName('td')

        #initiate a list to append into the return_list
        cell_list = []

        #loop through the list of desired headers
        for i in headers:
            try:
                #try to add text from the cell into the cell_list
                cell_list.append(cells[i].textContent)
            except:
                #if there is an error usually an index error just continue
                continue
                #append the data scraped into the return_list
        return_list.append(cell_list)

        #return the return list  
    return return_list
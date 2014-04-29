#!/bin/sh
# -*- coding: utf-8 -*-

export PYTHONPATH=${PYTHONPATH}:./excel_parser
export PYTHONPATH=${PYTHONPATH}:./sql
python ./sql/sql.py
python ./sql/sqlexcel.py
python ./sql/sqlfind.py
python ./sql/sqlPara.py
python ./google\ calendar/addevent.py  --noauth_local_webserver
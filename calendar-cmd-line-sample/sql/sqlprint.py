# -*- coding: utf-8 -*-
from sql.sql import *
session = Session()
teacher = session.query(Teacher).all()
for item in teacher:
    print unicode(item)
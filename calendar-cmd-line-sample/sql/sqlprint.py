# -*- coding: utf-8 -*-
from sql import *
session = Session()
teacher = session.query(Teacher).all()
for item in teacher:
    print unicode(item)
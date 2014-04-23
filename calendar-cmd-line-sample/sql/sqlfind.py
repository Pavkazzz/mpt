# -*- coding: utf-8 -*-
from sql import *

session = Session()

para = session.query(Para).all()

for item in para:
    print item.abstractpara.gruppa.id
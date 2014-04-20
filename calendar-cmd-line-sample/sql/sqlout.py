# -*- coding: utf-8 -*-

from sql import *

session = Session()

para = session.query(AbstractPara).all()

print para

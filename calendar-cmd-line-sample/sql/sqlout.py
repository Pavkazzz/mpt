# -*- coding: utf-8 -*-

from sql import *

session = Session()
abspar = session.query(AbstractPara).all()
print abspar
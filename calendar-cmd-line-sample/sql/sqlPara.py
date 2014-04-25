# -*- coding: utf-8 -*-
from sql import Para, AbstractPara, Session
import datetime
session = Session()

sqlabspara = session.query(AbstractPara).all()

for para in sqlabspara:
    print para
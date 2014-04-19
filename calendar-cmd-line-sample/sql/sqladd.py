# -*- coding: utf-8 -*-
from sql import *

session = Session()
teacher = Teacher(u'Караваев', u'Сергей', u'Владимирович')
session.add(teacher)
session.commit()


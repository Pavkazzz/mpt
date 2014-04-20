# -*- coding: utf-8 -*-
from sql import *

session = Session()


abspara = AbstractPara(1, 1, 1)
session.add(abspara)

teach = Teacher(u'Караваев', u'Сергей', u'Владимирович')
session.add(teach)

disc = Discipline(u'ТРПО')
session.add(disc)

grupp = Gruppa(u'П-329')
session.add(grupp)

session.commit()


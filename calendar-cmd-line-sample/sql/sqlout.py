#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sql import *

session = Session()

para = session.query(Para).all()

for abspara in para:
    absparaid = session.query(AbstractPara).all()
    for item in absparaid:
        #tempteach = session.query(Teacher).filter_by(id=AbstractPara.teach_id).first()
        tempteach = session.query(Teacher).first()
        tempdisc = session.query(Discipline).first()
        tempgruppa = session.query(Gruppa).first()
        print '%s, %s, %s. %s. %s' % (tempgruppa.name, tempdisc.name, tempteach.name[0], tempteach.otch[0], tempteach.lastname)
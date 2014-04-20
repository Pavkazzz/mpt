# -*- coding: utf-8 -*-

from sql import *

session = Session()

para = session.query(AbstractPara).all()

for item in para:
    tempteach = session.query(Teacher).filter_by(id=AbstractPara.teach_id).first()
    tempdisc = session.query(Discipline).filter_by(id=AbstractPara.disc_id).first()
    tempgruppa = session.query(Gruppa).filter_by(id=AbstractPara.gruppa_id).first()
    print '%s, %s, %s' % (tempgruppa.name, tempdisc.name, tempteach.lastname)
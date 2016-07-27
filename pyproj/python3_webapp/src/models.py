import time, uuid

from orm import Model,IntegerField,StringField, TextField

def next_id():
    return '%010d' % (int(time.time() * 1000))
def next_index():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)	

class QrTable(Model):
    __table__ = 'qrtable'
	
    qrid = IntegerField(primary_key=True, default=next_id, ddl='varchar(50)')
    qrindex = StringField(default=next_index,ddl='varchar(45)',)
    qrcontent = TextField(ddl='longtext')
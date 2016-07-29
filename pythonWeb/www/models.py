import time, uuid

from orm import Model,IntegerField,StringField, TextField

def next_id():
    return '%06d' % (int(time.time()))
def next_index():
    return '%08d%s' % (int(time.time() * 10), uuid.uuid4().hex)	

class QrTable(Model):
    __table__ = 'qrtable'
	
    qrid = IntegerField(primary_key=True, default=next_id, ddl='int')
    objectid = IntegerField(primary_key=False,ddl='int')
    qrindex = StringField(ddl='varchar(45)')
    qrcontent = TextField(ddl='longtext')

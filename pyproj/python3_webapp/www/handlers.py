from coroweb import get, post
from models import QrTable,next_id
import logging; logging.basicConfig(level=logging.INFO)
from config import configs
@post('/createQrCode')
def test(*,objectid,qrcontent):
    nextId=next_id()
    arr=yield from queryQrObjectId(objectid)
    rows=0
    if len(arr)>0:
       ##update
       logging.info("update objectid() %s" % objectid) 
       q=arr[0]
       q["qrcontent"]=qrcontent
       rows=yield from q.update()
    else:
       ##insert
       q=QrTable(objectid=objectid,qrindex=nextId,qrcontent=qrcontent)
       logging.info("insert qrindex() %s" % nextId)
       rows= yield from q.save()
       
    if rows!=1:
       return dict(errCode=False,content="")
    else:
       arr=yield from queryQrObjectId(objectid)
       qOBJ=arr[0]
       return dict(errCode=True,content=qrindexUrl(qOBJ))
def queryQrIndex(qrindex):
    arr=yield from QrTable.findAll("qrindex=?",[qrindex])
    return arr
def queryQrObjectId(objectid):
    arr=yield from QrTable.findAll("objectid=?",[objectid])
    return arr
def qrindexUrl(qOBJ):
    ip=configs.server['ip']
    port=configs.server['port']
       
    return "http://"+ip+":"+str(port)+"/myQR/"+qOBJ["qrindex"]

@get('/linkHtmlByObjectId')
def linkhtml(*,objectid):
     arr=yield from queryQrObjectId(objectid)
     if len(arr)>0:
        qOBJ=arr[0]
        return qrindexUrl(qOBJ)
     else:
        return ""
	 
@get('/api/myQR/{qrindex}')
def queryQR(qrindex):
    arr=yield from queryQrIndex(qrindex)
    if len(arr)==1:
       return dict(errCode=True,content=arr[0]["qrcontent"])
    return  dict(errCode=False,content="")

@get('/')
def main():
    return { '__template__': 'index.html'}

@get('/json')
def jsonTest():
    return dict(name='yuyang',age=27)
	   

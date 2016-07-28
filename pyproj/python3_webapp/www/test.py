import orm,dbconn,asyncio
from models import QrTable
import sys
def test(loop):
     yield from orm.create_pool(loop=loop,user='root',password='root',db='qrcode')
     q = QrTable(qrindex="3453453",qrcontent="<A><h>0F02</h><p><n>5开关状态</n><r>13Y000送风机状态</r><r>24Y001抽风机状态</r><r>35Y002冷却风机状态</r><r>46Y003冷却风泵状态</r><r>57Y004循环水泵状态</r></p><p><n>5实时数据</n><r>11D212顺序启动延时</r><r>22D1FE变频器频率</r><r>31D212顺序启动延时</r><r>42D1FE变频器频率</r><r>51D212顺序启动延时</r></p></A>")
     val=yield from q.findAll()
     print(val)

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
if loop.is_closed():
    sys.exit(0)

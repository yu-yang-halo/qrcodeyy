import coroweb,models

@get('/save')
def get_blog(id):
    QrTable q=QrTable(objectid=100,qrindex=next_id(),qrcontent="test;;;;")
	q.save()
    return {
    '__template__': 'index.html',
}
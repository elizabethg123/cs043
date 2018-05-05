import wsgiref.simple_server
import urllib.parse
from lesson2_2.database import Simpledb #my database is stored in lesson2_2 instead, so I changed the template


def application(environ, start_response):
    headers = [('Content-Type', 'text/plain; charset=utf-8')]

    path = environ['PATH_INFO'].split('/')
    params = urllib.parse.parse_qs(environ['QUERY_STRING'])

    print(path[1])

    db = Simpledb('db.txt')
    if path[1] == 'insert':
        db.insert(params['key'][0], params['value'][0])
        start_response('200 OK', headers)
        return ['Inserted'.encode()]
    elif path[1] == 'select':
        s = db.select_one(params['key'][0])
        start_response('200 OK', headers)
        if s:
            return [s.encode()]
        else:
            return ['NULL'.encode()]
    elif path[1] == 'delete':
        s = db.select_one(params['key'][0])
        start_response('200 OK', headers)
        if s:
            db.delete(params['key'][0])
            return ['Deleted'.encode()]
        else:
            return ['NULL'.encode()]

    elif path[1] == 'update':
        s = db.select_one(params['key'][0])
        start_response('200 OK', headers)
        if s:
            db.modify(params['key'][0], params['value'][0])
            return ['Updated'.encode()]
        else:
            return ['NULL'.encode()]

    else:
        start_response('404 Not Found', headers)
        return ['Status 404: Resource not found'.encode()]

httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()
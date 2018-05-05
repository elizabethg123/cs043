import wsgiref.simple_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    page = '''<!DOCTYPE html>
          <html>
          <head><title>Page Title</title> </head>
          <body>
          <h1 style="color:blue;">Lemonade</h1>
          <p>My first paragraph.</p>
          <a href="/check?a=1&b=2">Check A and B</a>
          <a href="https://www.w3schools.com">This is a link</a>
          <img src="w3schools.jpg" alt="W3Schools.com" width="104" height="142">
          </body>
          </html>'''

    return [page.encode()]

httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()
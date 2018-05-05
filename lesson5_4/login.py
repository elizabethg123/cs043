import wsgiref.simple_server
import urllib.parse
import sqlite3
import http.cookies
import emails

#checks to see if database is created and table created
connection = sqlite3.connect('users.db')
stmt = "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
cursor = connection.cursor()
result = cursor.execute(stmt)
r = result.fetchall()
if (r == []):
    exp = 'CREATE TABLE users (username,password)'
    connection.execute(exp)

def application(environ, start_response):
    headers = [('Content-Type', 'text/html; charset=utf-8')]

    path = environ['PATH_INFO']
    params = urllib.parse.parse_qs(environ['QUERY_STRING'])
    un = params['username'][0] if 'username' in params else None
    pw = params['password'][0] if 'password' in params else None

    if path == '/register' and un and pw:
        user = cursor.execute('SELECT * FROM users WHERE username = ?', [un]).fetchall()
        if user:
            start_response('200 OK', headers)
            return ['Sorry, username {} is taken'.format(un).encode()]
        else:  # Start code student should have entered
            connection.execute('INSERT INTO users VALUES (?, ?)', [un, pw])
            connection.commit()
            headers.append(('Set-Cookie', 'session={}:{}'.format(un, pw)))
            start_response('200 OK', headers)
            return ['Congratulations, username {} been successfully registered. <a href="/account">Account</a>'.format(
                un).encode()]
    # End code student should have entered

    elif path == '/login' and un and pw:
        user = cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', [un, pw]).fetchall()
        if user:
            headers.append(('Set-Cookie', 'session={}:{}'.format(un, pw)))
            start_response('200 OK', headers)
            return ['User {} successfully logged in. <a href="/account">Account</a>'.format(un).encode()]
        else:
            start_response('200 OK', headers)
            return ['Incorrect username or password'.encode()]

    elif path == '/logout':
        headers.append(('Set-Cookie', 'session=0; expires=Thu, 01 Jan 1970 00:00:00 GMT'))
        start_response('200 OK', headers)
        return ['Logged out. <a href="/">Login</a>'.encode()]

    elif path == '/account':
        start_response('200 OK', headers)

        if 'HTTP_COOKIE' not in environ:
            return ['Not logged in <a href="/">Login</a>'.encode()]

        cookies = http.cookies.SimpleCookie()
        cookies.load(environ['HTTP_COOKIE'])
        if 'session' not in cookies:
            return ['Not logged in <a href="/">Login</a>'.encode()]

        [un, pw] = cookies['session'].value.split(':')
        user = cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', [un, pw]).fetchall()
        if user:
            return ['Logged in: {}. <a href="/logout">Logout</a>'.format(un).encode()]
        else:
            return ['Not logged in. <a href="/">Login</a>'.encode()]

    elif path == '/tregister': #Start of code student should have entered
        login_form = '''
            <form>
                <h1>Register</h1>
                Username <input type="text" name=" username"><br>
                Password <input type="password" name=" password"><br>
                <br><input type="submit" formaction="/register" value="Create Account"> 
            </form>
            <head>
            <style>
            body {
                background-color: white;
                font-family: "Lucida", Monospace;
            }
            h1 {
                color: white;
            } 
            form {
                background-color:green;
                color: white;
                width: 100%;
                padding-left: 5px;
                padding-bottom: 5px;
                font-family: "Lucida", Monospace;
            }
            input {
                background-color: white;
                border-color: white;
                color: green;
            }
            </style>
            </head>
            '''
        start_response('200 OK', headers)
        return [login_form.encode()]


    elif path == '/forgotpassword':
        login_form = '''
            <form>
                <h1>Forgot Password</h1>
                Username <input type="text" name=" username"><br>
                <br><input type="submit" formaction="/forgotpasswordsent" value="Forgot Password"> 
            </form>
            <head>
            <style>
            body {
                background-color: white;
                font-family: "Lucida", Monospace;
            }
            h1 {
                color: white;
            } 
            form {
                background-color:green;
                color: white;
                width: 100%;
                padding-left: 5px;
                padding-bottom: 5px;
                font-family: "Lucida", Monospace;
            }
            input {
                background-color: white;
                border-color: white;
                color: green;
            }
            </style>
            </head>
            '''
        start_response('200 OK', headers)
        return [login_form.encode()]

    elif path == '/forgotpasswordsent' and un and pw:
        emails.send(un, pw)
        login_form = '''
        <body>Your password was sent to your email.</body>
        body {
                background-color: green;
                font-family: "Lucida", Monospace;
            }'''
        start_response('200 OK', headers)
        return [login_form.encode()]

    elif path == '/':  # Start of code student should have entered
        login_form = '''
    <form>
    <h1>Login</h1>
    Username <input type="text" name=" username"><br>
    Password <input type="password" name=" password"><br>
    <br><input type="submit" formaction="/login" value="Log in"> <input type="submit" formaction="/forgotpassword" value="Forgot Password"> <input type="submit" formaction="/tregister" value="Register">
</form>
<style>
body {
    background-color: white;
    font-family: "Lucida", Monospace;
}


h1 {
    color: white;
} 

form {
    background-color:green;
    color: white;
    width: 100%;
    padding-left: 5px;
    padding-bottom: 5px;
    font-family: "Lucida", Monospace;
}

input {
    background-color: white;
    border-color: white;
    color: green;
}

</style>
'''
        start_response('200 OK', headers)
        return [login_form.encode()]


    else:
        print(path)
        start_response('404 Not Found', headers)
        return ['Status 404: Resource not found'.encode()]

httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()

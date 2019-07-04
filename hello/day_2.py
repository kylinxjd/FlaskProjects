# _*_ coding: utf-8 _*_

from flask import Flask, request, make_response, render_template, session

app = Flask(__name__)
app.secret_key = 'asjdaksjnfsjdanfoiwfijiweojfskmdknaks,m'


# @app.before_first_request
# def before_first_request():
#     print("第一次请求之前")
#
#
# @app.before_request
# def before_request():
#     print("每一次请求之前执行")
#
#
# @app.after_request
# def after_request(response):
#     print("after_response")
#     return response
#
#
# @app.teardown_request
# def teardown_request(e):
#     print("teardown_request")
#     print(e)


@app.route('/setcookie')
def setcookie():
    mkres = make_response(render_template('index.html'))
    mkres.set_cookie('username', 'laowang')
    return mkres


@app.route('/getcookie')
def getCookie():
    print(request.cookies.get('username'))
    return request.cookies.get('username')


@app.route('/delcookie')
def delCookie():
    mkres = make_response(render_template('index.html'))
    mkres.delete_cookie('username')
    return mkres


@app.route('/setsession', methods=['GET', 'POST'])
def setsession():
    session['username'] = 'xiaowang'
    return "session"


@app.route('/getsession')
def getsession():
    return session.get('username')


@app.route('/jinjia')
def html_test():
    return render_template('jinjiatest.html', name='xiaowang', list1=[1, 2, 3])


if __name__ == '__main__':
    app.run(debug=True)

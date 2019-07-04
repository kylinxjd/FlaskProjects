# _*_ coding: utf-8 _*_

from flask import Flask, make_response, request

app = Flask(__name__)


@app.before_first_request
def before_first_request():
    print("before_first_request")


@app.before_request
def before_request():
    print("before request")


@app.after_request
def after_request(response):
    print("after request")
    return response


@app.teardown_request
def teardown(e):
    print("tear down request")
    print(e)


@app.route('/gouzi')
def gouzi():
    return "gouzi"


@app.route('/setcookie')
def setcookie():
    mkres = make_response("setcookie")
    mkres.set_cookie(key="height", value='122', max_age=90)
    return mkres


@app.route('/getcookie')
def getcookie():
    c = request.cookies.get('height')
    return c


if __name__ == '__main__':
    app.run(debug=True)

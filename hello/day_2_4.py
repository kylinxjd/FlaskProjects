# _*_ coding: utf-8 _*_
from flask import Flask, make_response, request

app = Flask(__name__)


@app.before_first_request
def before_first():
    print("before_first")


@app.before_request
def before():
    print("before")


@app.after_request
def after(response):
    print("after")
    return response


@app.teardown_request
def teardown(e):
    print("tear down")
    print(e)


@app.route('/test4')
def test4():
    return "4"


@app.route('/setcookie')
def setcookie():
    mkr = make_response("ok")
    mkr.set_cookie(key='4', value='4', max_age=22)
    return mkr


@app.route('/getcookie')
def getcookie():
    coo = request.cookies.get('4')
    return coo


if __name__ == '__main__':
    app.run(debug=True)

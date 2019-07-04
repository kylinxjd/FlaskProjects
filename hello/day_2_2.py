# _*_ coding: utf-8 _*_

from flask import Flask, make_response, request

app = Flask(__name__)


@app.before_first_request
def before_first_request():
    print("before first request，第一次请求前的操作")


@app.before_request
def before_request():
    print("before request， 每一次请求前都会执行")


@app.after_request
def after_request(response):
    print("after request，加工响应对象")
    return response


@app.teardown_request
def teardown_request(e):
    print("teardown_request, 请求之后一定执行")



@app.route('/index')
def index():
    return "index"


@app.route('/getcookie')
def getcookie():
    cook = request.cookies.get('age')
    return cook + "   cookies"


@app.route('/setcookie')
def setcookie():
    mkres = make_response("nihao")
    mkres.set_cookie(key="age", value='13', max_age=30)
    return mkres


if __name__ == '__main__':
    app.run(debug=True)

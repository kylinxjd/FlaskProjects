from flask import Flask, abort
from flask import jsonify
from flask import request
from flask import render_template
from werkzeug.routing import BaseConverter
from werkzeug.utils import secure_filename

app = Flask(__name__)


class Config(object):
    DEBUG = True


app.config.from_pyfile('config.ini')


# 自定义转换器
class MyConverter(BaseConverter):
    def __init__(self, param, *args):
        # args接受url传递的变量规则
        super().__init__(param)
        self.regex = args[0]


# 使用自定义的转换器
app.url_map.converters['re'] = MyConverter


@app.route('/')
def index():
    # data = {
    #     "name": "小王",
    #     "age": 16
    # }
    # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    print(request.args)
    print(request.args.get('ko'))
    print(request.args['ko'])
    # return jsonify(data)
    return "hello flask"


@app.route('/index', methods=['POST'])
def index_post():
    print(request.data)
    print(request.form)
    return "post url"


@app.route('/variable/<params>')
def variable(params):
    return params


@app.route('/converter/<re("[\d]{3}"):params>')
def myconvert(params):
    print(params)
    print(type(params))
    return params


@app.route('/project/')
def projects():
    abort(404)
    return 'The project page'


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404/404.html', error='bad'), 404


@app.route('/uploadfile')
def uploadfile():
    return render_template('upload_file.html')


@app.route('/uploadfilehandler', methods=['POST'])
def uploadfilehandler():
    f = request.files['file']
    # f = request.files.get('file')
    print(f)
    f.save('./static/img/' + f.filename)
    return "ok"


@app.route('/user/<int:userid>')
def user(userid):
    print(userid)
    print(type(userid))
    return str(userid)


if __name__ == '__main__':
    app.run()

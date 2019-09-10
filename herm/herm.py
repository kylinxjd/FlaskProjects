from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'asdadafdgfhfghfjgkhgjgk,lkl'

app.config['SECRET_KEY'] = 'asdakdmfkl/;cvbf;g,fkfg'

# 数据库配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/flask01'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate

manager = Manager(app, db)
# 添加命令，取名为db_command
manager.add_command('db_command', MigrateCommand)
# 创建migrate，将app应用和数据库操作句柄联系在一起
migrate = Migrate(app, db)




class Role(db.Model):
    __tablename__ = 'roles'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)

    #     在主表添加关系，与用户表产生关系，代表整个角色下的所有用户

    users = db.relationship('User', backref='role', lazy='dynamic')
    # backref='role'反向作用
    # lazy='dynamic'用到是时候关联加载
    # lazy='subquery'加载完对象后立即加载



    def __repr__(self):
        return self.name


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(30), nullable=True)
    is_delete = db.Column(db.Boolean, default=False)
    # 添加外键
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return self.name



class Register(FlaskForm):
    username = StringField(label='username',
                           validators=[DataRequired()],
                           render_kw={
                               'placeholder': 'username',
                               'class': 'input_text'
                           })
    password = PasswordField(label='password',
                             validators=[DataRequired(),
                                         Length(3, 8, '密码长度必须在3-8之间')])
    cpassword = PasswordField(label='cpassword',
                              validators=[DataRequired(),
                                          EqualTo('password', '两次密码不一致')])
    submit = SubmitField('提交')


# @app.route('/', methods=['post', 'get'])
# def index():
#     if request.method == 'GET':
#         return render_template('temp041.html')
#     if request.method == 'POST':
#         # todo 获取表单数据
#         form_data = request.form
#         print(form_data)
#         username = form_data.get('username')
#         password = form_data.get('password')
#         cpassword = form_data.get('cpassword')
#         # todo 校验表单
#         if not all([username, password, cpassword]):
#             return "数据不完整"
#         if password != cpassword:
#             return "两次密码不一致"
#         # TODO 保存数据
#         return "success"
#
#
# @app.route('/testform', methods=['get', 'post'])
# def testform():
#     form = Register()
#     if request.method == 'GET':
#         return render_template('form.html', form=form)
#     if request.method == 'POST':
#         if form.validate_on_submit():
#             username = form.username.data
#             password = form.password.data
#             print("11111111111111111111111111111")
#             print(username)
#             print(password)
#             print("22222222222222222222222")
#             print(type(form.data))
#             print(form.data)
#             return "success"
#         else:
#             print(form.errors)
#             error_msg = form.errors
#             for k, v in error_msg.items():
#                 print(k, v[0])
#             return "failed"exit

@app.route('/index')
def index():
    return "index"


@app.route('/index2')
def index2():
   return "index2"


if __name__ == '__main__':
    # db.create_all()

    # obj1 = User(name='老铁')
    # obj2 = User(name='小王', email='123@qq.com')
    # obj3 = User(name='老王', email='1653@qq.com')

    # db.session.add(obj1)
    # db.session.add_all([obj3])
    #
    # db.session.commit()

    # app.run(debug=True)
    manager.run()

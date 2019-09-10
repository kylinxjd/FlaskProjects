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


db = SQLAlchemy(app)


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(30), nullable=True)
    is_delete = db.Column(db.Boolean, default=False)

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


@app.route('/', methods=['post', 'get'])
def index():
    if request.method == 'GET':
        return render_template('temp041.html')
    if request.method == 'POST':
        # todo 获取表单数据
        form_data = request.form
        print(form_data)
        username = form_data.get('username')
        password = form_data.get('password')
        cpassword = form_data.get('cpassword')
        # todo 校验表单
        if not all([username, password, cpassword]):
            return "数据不完整"
        if password != cpassword:
            return "两次密码不一致"
        # TODO 保存数据
        return "success"


@app.route('/testform', methods=['get', 'post'])
def testform():
    form = Register()
    if request.method == 'GET':
        return render_template('form.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            print("11111111111111111111111111111")
            print(username)
            print(password)
            print("22222222222222222222222")
            print(type(form.data))
            print(form.data)
            return "success"
        else:
            print(form.errors)
            error_msg = form.errors
            for k, v in error_msg.items():
                print(k, v[0])
            return "failed"


if __name__ == '__main__':

    # db.create_all()

    obj1 = User(name='老铁')
    obj2 = User(name='小王', email='123@qq.com')
    obj3 = User(name='老王', email='1653@qq.com')

    # db.session.add(obj1)
    # db.session.add_all([obj3])
    #
    # db.session.commit()

    app.run(debug=True)

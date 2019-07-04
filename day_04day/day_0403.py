# _*_ coding: utf-8 _*_


from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

app = Flask(__name__)


class Register(FlaskForm):
    username = StringField(label='username',
                           validators=[DataRequired()],
                           render_kw={
                               'placeholder': 'username'
                           })
    pwd = StringField(label='mima',
                      validators=[DataRequired(),
                                  Length(min=3, max=12, message='length error')])
    cpwd = StringField(label='cpwd',
                       validators=[DataRequired(),
                                   Length(min=3, max=12, message='length error'),
                                   EqualTo(fieldname='pwd', message='not equal')])
    submit = SubmitField('提交')


@app.route('/index', methods=['GET', 'POST'])
def index():
    form = Register()
    if request.method == 'GET':
        return render_template('form.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            data = form.data
            print(data)
            return "success"
        else:
            error = form.errors
            print(error)
            return "error"


if __name__ == '__main__':
    app.run(debug=True)

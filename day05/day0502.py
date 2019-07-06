# _*_ coding: utf-8 _*_
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/flask01'
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app=app)

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

migrate = Migrate(app=app, db=db)

class Role(db.Model):

    __tablename__ = 'role02'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(length=21), unique=True)

    users = db.relationship('User', backref='role')



class User(db.Model):
    __tablename__ = 'user02'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(length=21), unique=True)

    role_id = db.Column(db.Integer, db.ForeignKey('role02.id'))



@app.route('/index')
def index():
    return "index"



if __name__ == '__main__':
    manager.run()
# _*_ coding: utf-8 _*_

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql://root:123456@127.0.0.1:3306/flask'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app=app)

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

migrate = Migrate(app=app, db=db)


class Role(db.Model):
    __tablename__ = 'role03'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(21), unique=True)

    users = db.relationship('User', backref='role')


class User(db.Model):
    __tablename__ = 'user03'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(21), unique=True)

    role_id = db.Column(db.Integer, db.ForeignKey('role03.id'))


if __name__ == '__main__':
    manager.run()

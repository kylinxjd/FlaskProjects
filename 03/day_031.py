# _*_ coding: utf-8 _*_
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def index():
    str1 = '<h1>flask</h1>'
    list1 = ['sad', 'sadasdada', 'ssdsdsdfgg', 'sdsa', 's']
    list2 = [1, 2, 3, 4]
    dict1 = {
        'name': 'xiaowang',
        'age': 23
    }
    dict_list = [
        {
            'name': 'xiaowang',
            'age': 23
        },
        {
            'name': 'laowang',
            'age': 33
        }
    ]
    data = {
        'str1': str1,
        'list1': list1,
        'dict1': dict1,
        'dictlist': dict_list
    }
    return render_template('31.html', str1=str1, list1=list1, dict1=dict1, dict_list=dict_list, list2=list2)


@app.route('/index2')
def index2():
    str1 = "hello"
    return render_template('temp1.html', str1=str1)


if __name__ == '__main__':
    app.run(debug=True)

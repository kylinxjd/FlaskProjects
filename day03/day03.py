from flask import Flask, current_app, make_response, render_template, flash

app = Flask(__name__)

app.secret_key = 'sjadhkjfjisjfiewirjwem, cm,csd./z;'


@app.route('/')
def hello_world():
    print("应用上下文------------------------------------")
    print(current_app)
    print(current_app.name)
    return 'Hello World!'


@app.route('/tempjinja')
def tempjinjia():
    res = make_response(render_template('temp1.html'))
    res.set_cookie(key='name', value='cookie', max_age=60)
    return res


@app.route('/data')
def data():
    str1 = "asas"
    list1 = [1, 2, 3, 4, 5]
    dict1 = {
        'name': 'xiaowang',
        'age': 23
    }
    newlist = ['asda', 'fdjkf']
    data1 = {
        'str1': str1,
        'list1': list1,
        'dict1': dict1,
        'newlist': newlist
    }
    # return render_template('temp2.html', **dict1)
    return render_template('temp2.html', str1=str1, list1=list1, dict1=dict1, newlist=newlist)


@app.route('/filter')
def filter():
    list1 = [1, 4, 3, 5, 1, 2]
    return render_template('temp3.html', list1=list1)


@app.template_filter('lireverse')
def list_reverse(li: list):
    li.reverse()
    return li


# app.add_template_filter(list_reverse, 'lireverse')


@app.route('/summary')
def summary():
    str1 = '<h1>flask</h1>'
    list1 = ['sadsds', 'sadasdada', 'ssdsdsdfgg', 'sdsa', 's']
    list2 = [1, 2, 3, 4]
    list3 = []
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
    # return render_template('temp4.html', **data)
    return render_template('temp4.html', str1=str1, list1=list1, dict1=dict1, dict_list=dict_list, list2=list2,
                           list3=list3)


@app.template_filter('dictsum')
def dictsum(diclist, param):
    sums = 0
    for item in diclist:
        sums += item[param]
    return sums


@app.route('/test')
def test():
    list1 = ['sadsds', 'sadasdada', 'ssdsdsdfgg', 'sdsa', 's']
    return render_template('temp1.html', list1=list1)


@app.errorhandler(404)
def not_found(error):
    print(error)
    return "asassssssssssssssssss"


@app.route('/macro')
def macro():
    return render_template('temp5.html')


@app.route('/extends')
def extends():
    return render_template('temp6.html')


@app.route('/include')
def include():
    return render_template('temp7.html')


@app.route('/info')
def info():
    flash('asdf')
    return "添加消息"

@app.route('/getmessage')
def getmessage():
    return render_template('temp8.html')

if __name__ == '__main__':
    app.run(debug=True)

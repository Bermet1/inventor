from flask import Flask, render_template, request
from flask.wrappers import Request

app = Flask(__name__)

@app.route('/')
def homepage():
    f = open('goods.txt', 'r', encoding='utf-8')
    goods = f.readlines()
    return render_template('index.html', goods = goods)

@app.route('/add/', methods=['POST'])
def add():
    good = request.form['good']
    f = open('goods.txt', 'a+', encoding='utf-8')
    f.write(good + '\n')
    f.close()
    return """
        <h2>Инвентарь пополнен</h2>
        <a href='/'>Домой</a>
        
        """
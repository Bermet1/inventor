from os import name
from flask import Flask, render_template, request
from databse import Good, engine
from sqlalchemy.orm import session, sessionmaker

app = Flask(__name__)
Session =sessionmaker(engine)

@app.route('/')
def homepage():
    session = Session()
    goods = session.query(Good)
    session.commit()
    return render_template('index.html', goods = goods)

@app.route('/add/', methods=['POST'])
def add():
    good = request.form['good']
    session = Session()
    good_object = Good(name=good)
    session.add(good_object)
    session.commit()
    return """
        <h2>Инвентарь пополнен</h2>
        <a href='/'>Домой</a>
        
        """
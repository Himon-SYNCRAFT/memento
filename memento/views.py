from memento import app, db
from flask import render_template, request
from datetime import datetime
from memento.models import MementoItem


@app.route('/get')
@app.route('/')
def get_memento_list():
    items = ['matma', 'programowanie']
    return render_template('memento_list.html', items=enumerate(items, start=1))


@app.route('/add', methods=['GET', 'POST'])
def new_memento():
    if request.method == 'POST':
        name = request.form['name']
        exercise = request.form['exercise']
        theory = request.form['theory']
        item = MementoItem(name=name, theory=theory, exercise=exercise)
        db.session.add(item)
        db.session.commit()

    return render_template('new_memento.html')


@app.route('/get/<int:memento_id>')
def get_memento(memento_id):
    name = "matma"
    exercise = "Suma kątów w trójkącie"
    theory = "http://wikipedia.com/234"

    return render_template(
        'get_memento.html',
        name=name,
        exercise=exercise,
        theory=theory
    )

@app.route('/test')
def test():
    now = datetime.now()
    return render_template("hello.html", date=now)

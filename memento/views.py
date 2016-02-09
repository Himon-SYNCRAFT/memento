from memento import app, db
from flask import render_template, request
from datetime import date
from memento.models import MementoItem


@app.route('/list')
@app.route('/')
def get_memento_list():
    items = MementoItem.query.filter(MementoItem.next_repetition_date <= date.today())
    return render_template('memento_list.html', items=enumerate(items, start=1))


@app.route('/list/<int:year>/<int:month>/<int:day>')
def get_memento_list_by_date(year, month=None, day=None):
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
    item = MementoItem.query.get_or_404(memento_id)
    item.generate_next_repetition_date()

    return render_template(
        'get_memento.html',
        item=item
    )

@app.route('/update/<int:memento_id>', methods=['POST'])
def accept_memento(memento_id):
    if request.method == 'POST':
        item = MementoItem.query.get_or_404(memento_id)
        item.number_of_repetitions += 1
        item.next_repetition_date = request.form['date']

        db.session.add(item)
        db.session.commit()

    return render_template(
        'update_memento.html',
        item=item
    )


@app.route('/test')
def test():
    return "poszlo"

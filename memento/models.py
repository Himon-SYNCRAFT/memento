from memento import db
from datetime import date, timedelta


class MementoItem(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    exercise = db.Column(db.String(4096))
    theory = db.Column(db.String(4096))
    number_of_repetitions = db.Column(db.Integer, nullable=False)
    next_repetition_date = db.Column(db.Date, nullable=False)

    def __init__(self, name, exercise=None, theory=None):
        self.name = name
        self.exercise = exercise
        self.theory = theory
        self.number_of_repetitions = 0
        self.generate_next_repetition_date()

    def generate_next_repetition_date(self):
        if(self.number_of_repetitions == 0):
            days = 1
        else:
            days = 2 ** (self.number_of_repetitions - 1)

        days = min(days, 30)
        self.next_repetition_date = date.today() + timedelta(days=days)

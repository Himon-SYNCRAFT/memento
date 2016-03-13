from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import memento.jinja_filters

app = Flask(__name__)
app.config.from_pyfile('settings.cfg')

db = SQLAlchemy(app)

app.jinja_env.filters['nl2br'] = jinja_filters.nl2br

import memento.views

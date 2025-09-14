# server/app.py
#!/usr/bin/env python3

from flask import Flask
from flask_migrate import Migrate
from models import db

app = Flask(__name__)

# Configuration for SQLite DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return 'Server is running!'

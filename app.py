from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "username"
app.config.from_object('config')
db = SQLAlchemy(app)
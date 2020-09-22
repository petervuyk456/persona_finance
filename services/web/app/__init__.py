from flask import Flask, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("app.config.Config")
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)

    def __init__(self, username):
        self.username = username


@app.route('/')
def hello_world():
    return jsonify(hello='world')


@app.route('/static/<path:filename>')
def staticfiles(filename):
    return send_from_directory(app.config["STATIC FOLDER"], filename)

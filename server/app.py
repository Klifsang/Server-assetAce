
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy()
@app.route('/')
def home():
    return '<h1>Asset inventory management</h1>'


if __name__ == '__main__':
    app.run(debug=True)
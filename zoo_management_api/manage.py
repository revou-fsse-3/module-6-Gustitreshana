from flask import Flask
from flask_migrate import Migrate
from app import db

app = Flask(__name__)

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()

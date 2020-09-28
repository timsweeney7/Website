from flask import Flask
from config import DefaultConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(DefaultConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

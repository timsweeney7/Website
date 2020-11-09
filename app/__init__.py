from flask import Flask
from flask_bootstrap import Bootstrap
from config import DefaultConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(DefaultConfig)
Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

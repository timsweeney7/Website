from flask import Flask
from flask_bootstrap import Bootstrap
from config import DefaultConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


application = Flask(__name__)
application.config.from_object(DefaultConfig)
Bootstrap(application)
db = SQLAlchemy(application)
migrate = Migrate(application, db)
login_manager = LoginManager()
login_manager.init_app(application)

from application import routes, models

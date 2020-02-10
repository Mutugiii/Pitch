from flask import Flask
from config import config_options

db = SQLAlchemy()

def create_app(config_name):
     app = Flask(__name__)
    
     # Creating configurations
     app.config.from_object(config_options[config_name])

     # Initialize flask extensions
     db.init_app(app)

     return app



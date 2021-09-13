from flask import Flask

from .config import DevConfig

from flask_bootstrap import Bootstrap

# Initializing application
app = Flask(__name__,template_folder='template',instance_relative_config = True)

#Initialize extensions
bootstrap = Bootstrap(app)

#Initializing configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


from app import views
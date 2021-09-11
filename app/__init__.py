from flask import Flask
from .config import DevConfig


# Initializing application
app = Flask(__name__,template_folder='template',instance_relative_config = True)

#Initializing configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


from app import views
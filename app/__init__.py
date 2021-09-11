from flask import Flask

# Initializing application
app = Flask(__name__,template_folder='template')

from app import views
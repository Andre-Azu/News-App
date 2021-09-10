from app import app
from flask import render_template


@app.route('/')
def index():
    '''
    root page that displays the index page
    '''

    title="Azu's News"
    return render_template('index.html',title=title)
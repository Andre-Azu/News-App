from flask import render_template
from app import app


# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title= 'New News'
    return render_template('index.html', title=title)

@app.route('/news/<news_id>')
def news(news_id):
    '''
    this is the funcion that returns the news articles data
    '''
    return render_template('news.html',id=news_id)
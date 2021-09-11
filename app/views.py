from flask import render_template
from app import app



# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title= ''
    return render_template('index.html', title=title)


#Route that enables search of every article published by over 80,000 different sources large and small in the last 3 years.   
@app.route('/v2/everything')    
def get_article(news_article):
   
    '''
    Route:This route that enables search of every article published by over 80,000 different sources large and small in the last 3 years.
    Function: Gets the articles
    '''
    aricle=news_article
    return render_template('news.html',article=news_article)

# #route that shows top headlines
# @app.route('/v2/top-headlines')
# def news(news_id):
#     '''
#     function
#     '''

# #route that returns info on the selected headlines
# @app.route('/v2/top-headlines/sources')
# def news(news_id):
#     '''
#     function
#     '''
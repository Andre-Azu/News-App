from flask import render_template
from app import app
from .request import get_news



# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    news= get_news('sports')
    
    title='Top Headlines'
    return render_template('index.html', title = title , news=news)

@app.route('/v2/sport')
def news():

    news=get_news('sports')
    wows='Today'
    title='News Details'
    return render_template('news.html', title = title, news=news)

#Route that enables search of every article published by over 80,000 different sources large and small in the last 3 years.   
# @app.route('')    
# def get_article():
   
#     '''
#     Route:This route that enables search of every article published by over 80,000 different sources large and small in the last 3 years.
#     Function: Gets the articles
#     '''
#     wow="kaikai"
#     return render_template('news.html',wow=wow)

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
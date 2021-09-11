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

#route that shows top headlines
@app.route('/v2/top-headlines')


#route that returns info on the selected headlines
@app.route('/v2/top-headlines/sources')

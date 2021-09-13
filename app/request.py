from app import app
import urllib.request,json
from .models import news

News=news.News

#Getting an API key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(category):
    '''
    this function enables us to read the json view
    '''
    get_news_url=base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data=url.read()
        get_news_response=json.loads(get_news_data)

        news_results=None

        if get_news_response['articles']:
            news_list = get_news_response['articles']
            news_results=process_results(news_list)
    return news_results

def process_results(news_list):
    '''
    this function proccesses the data that has been extracted from the get news function

    it's objective is tor return news objects.
    '''

    news_results=[]
    for news_item in news_list:
        source=news_item.get('source')
        author=news_item.get('author')
        websiteUrl=news_item.get('url')
        newsDescription=news_item.get('description')
        image=news_item.get('urlToImage')
        datePublished=news_item.get('publishedAt')
        article=news_item.get('content')
        if author: 
            news_zamz=News(author,websiteUrl,newsDescription,image,datePublished,article,source)
            news_results.append(news_zamz)
    return news_results       
    




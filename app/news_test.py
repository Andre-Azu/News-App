import unittest
from models import news

News=news.News

class NewsTest(unittest.Testcase):
    '''
    Test that test the beavior of the news class
    '''
    def setUp(self):
        self.new_news(self, )
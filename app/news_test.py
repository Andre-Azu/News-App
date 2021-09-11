import unittest
from models import news
News=news.News

class NewsTest(unittest.TestCase):
    '''
    Test that test the beavior of the news class
    '''
    def setUp(self):
        '''
        setup method tha rusns before every test
        '''
        self.new_news=News('Blake Brittain','Fitness band market share is undoubtedly contracting, thanks in no small part to the massive popularity of smartwatches. But 13.1 million overall shipments in Q1 2021 is nothing to sneeze at. People … [+3302 chars]','http://techcrunch.com/2021/08/25/fitbit-adds-ecg-and-stress-level-scanning-to-its-charger-fitness-tracker/','Warby Parker was hit with a lawsuit by 1-800 Contacts in Manhattan federal court accusing it of infringing its trademarks by buying search-engine keywords for "1-800 Contacts" to misdirect customers to its competing online contact-lens store.','https://www.reuters.com/legal/transactional/1-800-contacts-sues-warby-parker-trademark-infringement-over-keyword-ads-2021-08-19/","https://www.reuters.com/resizer/y8f--5BrKrGK9CqQJHPqZWC1FkA=/1200x628/smart/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/5EJ2XAMVHRLD3OZL46BXCWTCXA.jpg','2021-08-19T16:08:00Z' )

  
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()

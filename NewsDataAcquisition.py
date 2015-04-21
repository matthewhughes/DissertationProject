import requests
from lxml import etree
import feedparser
import DataStore
import ProcessNewsTitles

class AcquireNews(object):

    def __init__(self):
        self.read_timeout = 1.0
        self.error_count = 0

    def GetBBCNewsFeed(self):
        try:
            feed = requests.get('http://feeds.bbci.co.uk/news/uk/rss.xml', timeout=(10.0, self.read_timeout))
            print 'Succesfully Downloaded BBC UK RSS Feed'
            self.error_count = 0
        except requests.exceptions.ConnectionError as error:
            print error
            print 'DNS error prevented script from downloading feed'
            RetryConnectingToBeeb()
        except requests.exceptions.ReadTimeout as error:
            print error
            print "Connecting To The BBC Timed Out"
            RetryConnectingtoBeeb()
        return feed.text

    def RetryConnectingToBeeb(self):
        if(self.error_count < 3):
            self.error_count = self.error_count + 1
            print 'Retrying: Attempt Number ' + self.error_count
            GetBBCNewsFeed()
        else:
            print "Unable to connect to the BBC"
            print "Try Again Later"
            exit()

    def GetBBCNewsTitles(self, BeebXML):
        Titles = ProcessNewsTitles.ProcessTitles()
        db = DataStore.MongoDBStore()
        db.Setup()
        Titles = ProcessNewsTitles.ProcessTitles()

        feed = feedparser.parse(BeebXML)
        for x in range(0, len(feed['entries'])):
            entry = feed['entries'][x]['title']
            print entry

            Titles.title = entry
            Titles.tokenize_title()
            Titles.position_tags()
            Titles.find_noun()
            Titles.find_verb()

            db.SaveRecord(entry)

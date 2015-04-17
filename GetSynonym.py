import requests
import json

class Synonym(object):

    def __init__(self):
        self.api_key = '3f88fca1612e497544a1417875a87db5'
        self.verb = 'hide'
        self.synonyms = {}
        self.results = ''

    def get_synonyms(self):
        self.results = requests.get('http://words.bighugelabs.com/api/2/3f88fca1612e497544a1417875a87db5/' + self.verb +'/json').text
        self.synonyms = json.loads(self.results)
        self.synonyms = self.synonyms['verb']['syn']
        return self.synonyms

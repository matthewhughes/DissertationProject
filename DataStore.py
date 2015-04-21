import pymongo

class MongoDBStore(object):

    def __init__(self):
        self.server = ''
        self.database = ''
        self.collection = ''
        self.document = ''

    def Setup(self):
        self.server = pymongo.MongoClient()
        self.database = self.server.socialmediadata
        self.collection = self.database.posts

    def SaveRecord(self, title='title'):
        self.document = self.collection.insert({"title":title})

import pycouchdb

class CouchDBStore(object):

    def __init__(self):
        self.server = ''
        self.database = ''
        self.document = ''

    def Setup(self):
        self.server = pycouchdb.Server("http://127.0.0.1:5984/")

    def CreateDB(self):
        self.server.create("socialnewsdata")

    def UseDB(self):
        self.database = self.server.database('socialnewsdata')

    def SaveRecord(self, title='hello'):
        self.document = self.database.save({"title":title})
        print self.document

    def QueryDB(self):
        map_func = "function(document) { emit(document.title, 1); }"
        self.database.temporary_query(map_func)
        list(self.database.temporary_query(map_func))

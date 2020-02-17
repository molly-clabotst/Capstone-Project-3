class ViewModel():

    def __init__(self, db):
        self.db = db

    def insert(self, name, email):
        self.db.insert(name,email)

    def search_artist(self,name):
        data = self.db.search_artist(name)
        return data
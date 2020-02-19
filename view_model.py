class ViewModel():

    def __init__(self, db):
        self.db = db

    def insert(self, name, email):
        self.db.insert(name,email)

    def search_artist(self,name):
        data = self.db.search_artist(name)
        return data

    def insert_art(self, name, artist, price, available):
        self.db.insert_art(name, artist, price, available)

    def search_art_one(self, artist):
        data = self.db.search_art_one(artist)
        return data

    def search_art_all(self):
        data = self.db.search_art_all()
        return data

    def update(self, name, available):
        rows_updated = self.db.update(name, available)
        return rows_updated

    def search_art_name(self, name):
        data = self.db.search_art_name(name)
        return data
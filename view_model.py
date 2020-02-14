class ViewModel:

    def __init__(self, db):
        self.db = db

    def insert(self, art_s):
        self.db.insert(art_s)

    def get_all(self):
        return self.db.get_all()
import peewee

db = SqliteDatabase('artInfo.sqlite')

class Artist(Model):
    name = CharField()
    email = CharField()

    class Meta:
        database = db
    def __str__(self):
        return f'{self.name} is an artist and their email is {self.email}.'

class Art:
    artist= CharField()
    name = CharField()
    price = FloatField()
    availability = CharField()

    class Meta:
        database = db
    def __str__(self):
        return f'{self.artist} made this, they named it {self.name}. They are asking for ${self.price} for it and it is {self.availability}.'

class ArtStore:
    'Singleton'
    instance = None
    class __ArtStore:
        def __init__(self):
            db.connect()
            db.create_tables([Artist, Art])
        # def _add_art(self, art):

        # def _add_artist(self, artist):

        # def _update_art(self, art):

        # def _update_artist(self, artist):

        # def _delete_art(self, art):

        # def _delete_artist(self, artist):

        # def delete_all_art(self):

        # def delete_all_artists(self):

        # def exact_match(self, search):

        # def get_art_by_id(self, id):

        # def get_artist_by_id(self, id):

        # def search(self, term):

        # def get_art_by_availabliltiy(self, available):

        # def get_all_art(self):

        # def art_count(self):

        # def artist_count(self):

        def __new__(cls):
            if not ArtStore.instance:
                ArtStore.instance = ArtStore.__ArtStore()
            return ArtStore.instance

        def __getattr__(self, name):

        def __setattr__(self, name, value,):

class ArtError(Exception):
    pass
from model import Artist

class SQLArtDB():

    def insert(self, name, email):
        artist = Artist(name=name, email=email)
        artist.save()
        
    def search_artist(self, name):
        # ORM 
        data = Artist.select().where(Artist.name==name).limit(1)
        
        return data
    
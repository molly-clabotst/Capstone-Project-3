from model import Artist, Art

class SQLArtDB():

    def insert(self, name, email):
        artist = Artist(name=name, email=email)
        artist.save()
        
    def search_artist(self, name):
        # ORM 
        data = Artist.select().where(Artist.name==name).limit(1)
        return data

    def insert_art(self, name, artist, price, available):
        art = Art(name=name, artist=artist, price=price, available=available)
        art.save()

    def search_art_one(self, artist):
        data = Art.select().where(Art.artist==artist)
        return data
    
    def search_art_all(self):
        data = Art.select()
        return data
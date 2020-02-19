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
        if available.lower() == 'yes':
            available = 'sold'
        else:
            available = 'available'
        art = Art(name=name, artist=artist, price=price, available=available)
        art.save()

    def search_art_one(self, artist):
        # ORM
        data = Art.select().where(Art.artist==artist)
        return data
    
    def search_art_all(self):
        # ORM
        data = Art.select()
        return data

    def update(self, name):
        rows_updated = Art.update(available='sold').where(Art.name==name)
        return rows_updated

    def search_art_name(self, name):
        # ORM
        data = Art.select().where(Art.name==name)
        return data
from back.model import Artist, Art

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
        art = Art(art_name=name, artist=artist, price=price, available=available)
        art.save()

    def search_art_one(self, artist):
        # ORM
        data = Art.select().where(Art.artist==artist)
        return data
    
    def search_art_all(self):
        # ORM
        data = Art.select()
        return data

    def update(self, name, available):
        if available == 'sold':
            rows_updated = Art.update(available='available').where(Art.art_name==name).execute()
        elif available == 'available':
            rows_updated = Art.update(available='sold').where(Art.art_name==name).execute()
        else:
            rows_updated = 0
            
        return rows_updated

    def search_art_name(self, name):
        # ORM
        data = Art.select().where(Art.art_name==name)
        return data
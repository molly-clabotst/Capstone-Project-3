import peewee
from database_abc import ArtDB
from model import Art, Artist

class SQLArtDB(ArtDB):

    db = SqliteDatabase('art.db')

    def __init__(self):
        db.connect()
        db.create_tables([Art, Artist])

    def insert(self, art_s):

    def get_all(self, art_s):
        
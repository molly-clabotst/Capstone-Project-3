from peewee import *


# Database
db = SqliteDatabase('art.sqlite')

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Artist(BaseModel):
    name = CharField()
    email = CharField()

    def __str__(self):
        return f"{self.name}"

class Art(BaseModel):
    art_name = CharField()
    artist = ForeignKeyField(model=Artist, field=Artist.name)
    price = CharField()
    available = CharField()

    def __str__(self):
        return f"\nThis pieces name is {self.art_name} is it was created by {self.artist}. The pieces price is {self.price} and it is {self.available}.\n"

db.create_tables([Artist, Art])
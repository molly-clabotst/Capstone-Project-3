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
        return f"The artist {self.name} is contactable at {self.email}."

class Art(BaseModel):
    name = CharField()
    artist = ForeignKeyField(model=Artist, field=name)
    price = CharField()
    available = CharField()

    def __str__(self):
        return f"This pieces name is it was created by {self.artist}. The pieces price is {self.price} and it is {self.availabile}."

db.create_tables([Artist, Art])
class Art():
    def __init__(self, name, artist, price, availability=True):
        self.name = name
        self.artist = artist
        self.price = price
        self.availability = availability

    def __str__(self):
        return f"This piece of art is called {self.name} and it was created by {self.artist}. It's selling price is {self.price} and it is {self.availability}."

class Artist():
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address

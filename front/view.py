from back.model import Artist
from front.view_util import display
from validate import validate_Artist_name, validate_Art, validate_Email

import re


class View():

    def __init__(self, view_model):
        self.view_model = view_model

    def make_menu(self):
        while True:
            choice = input('Would you like to...\n1.Add A New Artist\n2.Add A New Piece\n3.Search For Art From A Specific Artist\n4.Search For All Art From All Artists\n5.Update The Availability Of A Peice\n6.Delete A Peice\nQ.Quit\n')
            print()
            if choice == '1':
                add_new_artist(self)
            elif choice == '2':
                add_new_art(self)
            elif choice == '3':
                srch_art_one_artist(self)
            elif choice == '4':
                srch_art_all_artist(self)
            elif choice == '5':
                update_available(self)
            # elif choice == 6:
            #     delete_art(self)
            elif choice.upper() == 'Q':
                print('\nThanks for using the Art Database\n')
                break
            else:
                print('Please choose a valid menu option, numbers 1-6 or Q for Quit.\n')

# ADD ARTIST
def add_new_artist(self, name=''):
    # Input Validation
    
    isFound = ''
    if name=='':
        name = input('What is the name of the artist? ')
        name = validate_Artist_name(name)
        isFound = search_artist(self, name, first=True)

    if isFound == None:
        email = input(f"What is {name}'s email? ")
        email = validate_Email(email)
        self.view_model.insert(name, email)
        data = self.view_model.search_artist(name)
        display(data, first=True)
    else:
        print(f"{name} is already in the system.\n")

# ADD NEW ART
def add_new_art(self):
    artist = input('What is the name of the artist? ')
    name = validate_Artist_name(artist)
    isFound = search_artist(self, artist, first=True)

    # Verifying that the artist exists in the database before adding art to their name
    if isFound==None:
        print(f"{artist} isn't in the system yet please add them first.")
        add_new_artist(self, artist)

    name = input('What is the name of the piece? ')
    price = input('What is the price of the piece? ')
    available = input('Is this piece sold? ')

    name, price, available = validate_Art(name, price, available)

    self.view_model.insert_art(name, artist, price, available)
    data = self.view_model.search_art_name(name)
    display(data)

# SEARCH ART FROM ONE ARTIST
def srch_art_one_artist(self):
    name = input('What is the name of the artist? ')
    name = validate_Artist_name(name)
    # data = search_artist(self, name)
    data = self.view_model.search_art_one(name)
    display(data)

# SEARCH ALL ART
def srch_art_all_artist(self):
    data = self.view_model.search_art_all()
    display(data)

# UPDATE
def update_available(self):
    name = input('What is the name of the artwork whos availability has changed? ')
    data = self.view_model.search_art_name(name)

    if data.exists() == False:
        print('Sorry that artwork does not exist')
        return
    for dat in data:
        available = dat.available

    rows_updated = self.view_model.update(name, available)

    if rows_updated == 0:
        print('There was an error.')
        return

    data = self.view_model.search_art_name(name) 
    display(data)   

# SEARCH ARTIST
def search_artist(self, name, first=False):
    data = self.view_model.search_artist(name)
    
    # Displaying search results
    if data.exists() == False:
        return None
    for dPoint in data:
        return dPoint
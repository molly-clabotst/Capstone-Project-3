from model import Artist
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
            # elif choice == 5:
            #     update_available(self)
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
        name = validate_artist_name(name)
        isFound = search_artist(self, name)

    if isFound == None:
        email = input(f"What is {name}'s email? ")
        self.view_model.insert(name, email)
        display(self, name)
    else:
        print(f"{name} is already in the system.\n")

# ADD NEW ART
def add_new_art(self):
    artist = input('What is the name of the artist? ')
    name = validate_artist_name(artist)
    isFound = search_artist(self, artist)

    # Verifying that the artist exists in the database before adding art to their name
    if isFound==None:
        print(f"{artist} isn't in the system yet please add them first.")
        add_new_artist(self, artist)

    name = input('What is the name of the piece? ')
    price = input('What is the price of the piece? ')
    available = input('Is this piece sold? ')

    self.view_model.insert_art(name, artist, price, available)

def srch_art_one_artist(self):
    name = input('What is the name of the artist? ')
    name = validate_artist_name(name)
    # data = search_artist(self, name)
    data = self.view_model.search_art_one(name)
    print(data)

def srch_art_all_artist(self):
    data = self.view_model.search_art_all()
    print(data)

# SEARCH ARTIST
def search_artist(self, name):
    data = self.view_model.search_artist(name)
    
    # Displaying search results
    if data.exists() == False:
        return None
    for dPoint in data:
        return dPoint

# DISPLAY DATA
def display(self, name):
    isFound = search_artist(self, name)

    # Alerting user as to whether the artist exists
    if isFound==None:
        print(f'\nSorry there was no entry for {name}.\n')
    else:
        print('\n'+str(isFound)+'\n')

def validate_artist_name(name):
    while True:
        chars = name.replace(" ", "")
        if len(chars)<2:
            name = input('Please enter a valid name. ')
        else:
            break

    return name
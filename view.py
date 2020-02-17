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
            # elif choice == 2:
            #     add_new_art(self)
            # elif choice == 3:
            #     srch_art_one_artist(self)
            # elif choice == 4:
            #     srch_art_all_artist(self)
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
def add_new_artist(self):
    # Input Validation
    while True:
        name = input('What is the name of the artist? ')
        email = input(f"What is {name}'s email? ")
        
        # srchObj = re.search("[a-zA-Z0-9].[@][a-zA-Z0-9].[.][a-zA-z0-9].", email)
        # or srchObj==None
        if len(name)<2 or len(email)<5 :
            print('\nPlease enter a valid Name and Email Address\n')
            # print(srchObj)
        else:
            # print(srchObj)
            break
    
    self.view_model.insert(name, email)
    display(self, name)

# DISPLAY DATA
def display(self, name):
    data = self.view_model.search_artist(name)
    
    # Displaying search results
    if data.exists() == False:
        print(f'\nSorry there was no entry for {name}.\n')
    for dPoint in data:
        print('\n'+str(dPoint)+'\n')

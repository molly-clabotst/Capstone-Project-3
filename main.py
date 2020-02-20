from front.view import View
from front.view_model import ViewModel
from back.database import SQLArtDB

def main():
    db_art = SQLArtDB()
    art_vm = ViewModel(db_art)
    view_art = View(art_vm)
    view_art.make_menu()

if __name__ == '__main__':
    main()
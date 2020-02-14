from view import *
from view_model import ViewModel
from database import SQLArtDB

def main():

    art_db = SQLArtDB()

    art_view_model = ViewModel(art_db)

    art_view = View(art_view_model)

    
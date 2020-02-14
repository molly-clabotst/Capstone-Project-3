from view import *
import view_model
from database import SQLArtDB

def main():

    art_db = SQLArtDB()

    art_view_model = view_model.ViewModel(art_db):

    art_view = View
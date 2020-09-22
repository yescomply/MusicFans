# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from db import *
from add_fan_account import *
from add_artist import *
from add_fan import *
from show_fan import *
from search_artist_fans import *
from menu import *

db = FansDb("ArtistsFans.db")

'''for genre in db.genres():
    print(genre['label'])
'''

show_menu(db)

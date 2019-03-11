from detail_item import *
from colored import fg, bg, attr

class Logbook(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.takeable = True
        self.description = """
The ink on most of the pages is faded beyond legibility, but there's one entry
towards the end that you can read:

%s%sWed. 11/9 – 11:43 AM. Culloden was late for this morning's lesson. Unacceptable. Reminded
him of my policy: if you are not five minutes early, you are late. He responded in foul
language. Assumed it was due to the issue of his wife, but apparently his flick knife fell from
his back pocket and he is unable to locate it.

Target shooting held only thirty per cent accuracy. Moods worsened on both our parts. Would
not be surprised to learn of my impending termination, despite my years of service to this
house. Should Culloden refuse to return my goods I may have to enter his safe myself. His
cards hold some key to the numerical code.%s""" % (fg('white'), attr('bold'), attr('reset'))

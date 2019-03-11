from detail_item import *

class Card_Table(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.takeable = False
        self.description = """
Cards are set about the surface of the table as if midway through a game
whose rules you can't quite identify. Some cards are in stacks in the middle, others face
up or face down in front of the players' places. You don't see any markings or distinct
patterns in what cards are where, but they all seem to be part of a single, standard deck."""
        
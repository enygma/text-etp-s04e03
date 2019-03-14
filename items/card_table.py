from detail_item import *
import inventory

class Card_Table(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.takeable = False
        self.fingerprints_found = False
        self.description = """
Cards are set about the surface of the table as if midway through a game
whose rules you can't quite identify. Some cards are in stacks in the middle, others face
up or face down in front of the players' places. You don't see any markings or distinct
patterns in what cards are where, but they all seem to be part of a single, standard deck."""

    def look(self):
        # check their inventory for both the power and brush
        if "powder" in inventory.inv and "brush" in inventory.inv:
            print("""You grab a handful of the white powdery ash from the fireplace and scatter 
it over the playing cards. Then you take your little brush and start dusting. And... fingerprints 
start to become visible. Any given card only has one set of prints on it, but there are loads 
of different prints on all the cards together.""")

            if not "rifle":
                print("You try to think of other places around you where you could also find fingerprints")
            else:
                print("""
You re-examine the rifle, using the powder and brush on it and find additional fingerprints. 
You compare the prints you found there to the cards. The exact same fingerprints are on four of 
the cards: the 7 of hearts, 2 of diamonds, 9 of clubs and 3 of spades.""")
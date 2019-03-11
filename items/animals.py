from detail_item import *

class Animals(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.takeable = False
        self.description = """
There are four animals mounted on the wall, staring out at you with
glassy, frozen eyes. You take a moment to count your blessings that no ghosts are
inhabiting them, because that would probably be more creepiness than you could handle.

Each animal has a label underneath it for identification: you're looking at a red deer, a
diamondback shark, a club-footed pheasant, and a black bear."""

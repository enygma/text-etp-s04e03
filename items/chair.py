from detail_item import *
import room_list
from items.logbook import Logbook

class Chair(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.takeable = False
        self.locked = True
        self.description = """
It's a large, well-cushioned chair. There's something very regal and
patriarchal about it, especially the fact that it's the only one like it, the only nice one by
the fire.”"""

    def look(self):
        print("There's also a glossy, black book resting on it. You turn the cover to the first page"
            +" and see in fading black ink, \“Logbook of Philip Ho.\"")

        logbook = Logbook('a logbook', 'logbook')
        room_list.game_room.items.add(logbook)

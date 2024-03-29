from detail_item import *
import room_list
from items.logbook import Logbook
from items.knife import Knife
import formatting

class Chair(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.takeable = False
        self.locked = True
        self.description = """
It's a large, well-cushioned chair. There's something very regal and patriarchal about it, 
especially the fact that it's the only one like it, the only nice one by the fire.”"""

    def look(self):
        print("""There a glossy, black %s%sbook%s resting on it. You turn the cover to the first page"
and see in fading black ink, \"Logbook of Philip Ho.\")""" % formatting.highlight)
        print("""
You also notice a small steel %s%stube%s-looking something wedged behind the cushion.""" % formatting.highlight)

        logbook = Logbook('a logbook', 'logbook')
        room_list.game_room.items.add(logbook)

        knife = Knife('a tube-shaped item', 'tube')
        room_list.game_room.items.add(knife)

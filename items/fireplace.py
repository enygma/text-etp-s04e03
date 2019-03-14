from detail_item import *
from items.white_powder import WhitePowder
import room_list

class Fireplace(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.takeable = False
        self.description = """
The fire is unlit and the area around it cold. You don't think it's been lit in
many, many years. It still has some ancient sooty powder on the bottom, some of which is
black, but most of which has aged so much it's turned grey or even white."""

    def look(self):
        powder = WhitePowder('white powder', 'powder')
        room_list.game_room.items.add(powder)

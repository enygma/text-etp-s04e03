from detail_item import *
import room_list

class Knife(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.takeable = True
        self.description = """
It's... um... a something. You have no idea. It looks like a solid, steel tube about the 
length of your palm. But there aren't any clues on it about what it actually does."""


    def look(self):
        print("""You give the weird tube an experimental thrust outward, and you feel 
something. You try it again, and a narrow blade comes flicking out from the top side. 
So this is Mr Culloden's lost knife. No wonder he was so annoyed about losing it; it's pretty fancy.""")

        self.description = "A fancy knife"
        self.name = 'knife'
        self.aliases = ['knife']

        curtains = room_list.game_room.items.find('curtains')
        curtains.actions.append({
            "match": "cut ropes",
            "method": "action_cutropes"
        })
        curtains.load_actions()

    def take(self):
        print("""It's... um... a something. You have no idea. It looks like a solid, steel tube about the
length of your palm. But there aren't any clues on it about what it actually does. Maybe looking closer will help.""")

        return True
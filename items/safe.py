from detail_item import *
import room_list
from items.traps import Traps

class Safe(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.takeable = False
        self.locked = True
        self.unlock_code = '7932'

        self.description = """
The safe is, of course, locked, and requires some combination of numbers to open.

You look around for any clues, but don't see anything. You do notice that there's an awful
lot of dust; no one's been anywhere near this safe for ages. And while you look at the dusty
top surface, you suddenly see movement. Some of the dust is peeling away, like a person
is pushing it aside with their finger – only, you don't see a finger. Or a person. The
movement continues, and it becomes clear that the invisible somebody is writing you a
message. H... A... N...G."""

        self.actions.append({
            "match": "unlock safe with CODE", 
            "method": "action_unlock"
        })

    def action_unlock(self, code):
        if code == self.unlock_code:
            print("""The door to the safe swings open! From inside it you pull out three objects: three traps.
They look like bear traps. Lucky for you they're all shut safely at the moment.""")

            traps = Traps('bear traps', 'traps')
            room_list.game_room.items.add(traps)
        else:
            print("That code doesn't seem to be correct - the safe stays firmly locked.")

        return False
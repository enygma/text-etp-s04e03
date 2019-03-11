from detail_item import *
from inventory import inv
from items.pipe import Pipe
import room_list

class PipeCase(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.takeable = True
        self.locked = True
        self.description = """
The name M. Culloden is engraved on the top, and there's a space for a tiny key
to unlock it."""

        self.actions.append({
            "match": "unlock pipe case", 
            "method": "action_unlock"
        })
        self.load_actions()

    def action_unlock(self):
        if self.locked:
            # see if they have the key in their inventory
            if "key" in inv:
                print("It unlocks! And... there is a pipe inside. It's long and incredibly thin. "
                    +"Looks like it's made of ivory or something.")

                # Add the pipe to the room
                pipe = Pipe('pipe', 'pipe')
                room_list.game_room.items.add(pipe)

            else:
                print("You don't have anything to unlock it with!")

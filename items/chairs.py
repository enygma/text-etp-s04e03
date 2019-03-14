from detail_item import *
import room_list
import formatting

from items.key import Key

class Chairs(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)

        self.arranged = False
        self.description = "They're four standard chairs, all tucked in neatly where players would sit at the table."

    def action_arrange(self):
        if not self.arranged:
            print("""
You start swivelling the appropriate chairs around and getting them into place. Funnily enough, when you turn
the first one, you swear you can see tiny grooves along the edge of the table where the back of the chair could 
touch it. And when you go around to the chair that needs tilting, there's a definite dent on the upper part of 
the table edge. You push the chair onto its back legs, and it falls right into the dent. 

And when it does, you hear a small thump come from under the table. You look down, and sitting on the carpet, 
having fallen from a hidden compartment on the table's underside, is a tiny %s%skey%s.""" % formatting.highlight)
            self.arranged = True

            key = Key('a small key', 'key')
            room_list.game_room.items.add(key)
        else:
            print('Rearranging the chairs has no additonal effect.')
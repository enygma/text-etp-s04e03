from detail_item import *
import room_list
from items.brush import Brush

class Rug(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.takeable = False
        self.hanging = False
        self.description = """
The rug is large, grey and rectangular, with loopy tassels in all the corners. The
pattern on it isn't very interesting: it's just a grid of squares, not even different colours.
Just grey squares."""

    def look(self):
        # Once they look at the rug specifically, they'll be able to hang it
        if not self.hanging:
            print('The loopy tassels on the corners look like they might be useful.')

            rug = room_list.game_room.items.find('rug')
            rug.actions.append({
                "match": "hang rug", 
                "method": "action_hang"
            })
            rug.load_actions()
        else:
            print("The rug is currently hanging from the hooks above the door, blocking it.")

    def action_hang(self):
        self.hanging = True
        print("""The rug is heavy and it takes a lot of effort to pull it out from under the table 
and lift it up against the doors, but the corner tassels loop around the hooks and they hold. The rug 
hangs flat against the doors, except for one single square of its pattern, which bulges out because 
of the door handles.""")

        # Add the "trace pattern" command but be sure they've watched the painting
        rug = room_list.game_room.items.find('rug')
        rug.actions.append({
            "match": "trace pattern", 
            "method": "action_trace"
        })
        rug.load_actions()

    def action_trace(self):
        
        painting = room_list.game_room.items.find('painting')
        if painting.seen_pattern:
            print("""You start at the square that's being pushed forward by the door handles,
then move up, left, up, right, up, right, down. The square you've finished on is exactly the 
same as the others. You lift up the rug and examine the door behind the square, and it's got 
the same 3D wooden pattern as everywhere else on the door.
""")
            print("""
You press a hand up to the wooden patterning and, well, shake it. And it  comes loose! A small 
piece of the wood drops off in your hand, and sitting behind it is a very small, very fine 
%s%sbrush%s. Like a make-up brush – or a police fingerprinting brush.""" % formatting.highlight)

            brush = Brush('a small brush', 'brush')
            room_list.game_room.items.add(brush)
        else:
            print("""You're not sure what pattern to trace. You feel drawn to further inspect 
the painting, just to be sure nothing was missed.""")
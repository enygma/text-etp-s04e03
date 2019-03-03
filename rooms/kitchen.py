from adventurelib import *
from detail_room import *

from rooms.game_room import *

kitchen = Detail_Room("""
The room you walk into is a kitchen, and a very messy one at that. Discarded food,
shattered glass. Definitely suits the haunted house atmosphere. But there's no Bill, so you
move through it into a dusty hallway. A fair way down on the right, you see a pair of wide
double doors, also open. Cool. If Bill's anywhere, in here seems likely. You step inside and
survey your surroundings.

You can enter the game room to the east.
""")

kitchen.name = 'kitchen'
kitchen.title = "The Kitchen"
kitchen.east = game_room
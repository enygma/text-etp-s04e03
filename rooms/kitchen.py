from adventurelib import *
from detail_room import *

# from rooms.game_room import GameRoom_Room
import room_list

class Kitchen_Room(Detail_Room):

    def __init__(self):
        description = """
The room you walk into is a kitchen, and a very messy one at that. Discarded food,
shattered glass. Definitely suits the haunted house atmosphere. But there's no Bill, so you
move through it into a dusty hallway. A fair way down on the right, you see a pair of wide
double doors, also open. Cool. If Bill's anywhere, in here seems likely. You step inside and
survey your surroundings.

You can enter the game room to the east."""

        Detail_Room.__init__(self, description)

        self.title = 'The Kitchen'
        self.name = 'kitchen'

        # import rooms.game_room 
        # self.east = rooms.game_room.GameRoom_Room()

        # self.east = room_list.game_room
        self.east = room_list.game_room

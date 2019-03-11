from adventurelib import *
from detail_room import *
from detail_item import *

from colored import fg, bg, attr

from items.chairs import Chairs
from items.card_table import Card_Table
from items.clock import Clock
from items.rifle import Rifle
from items.painting import Painting
from items.rug import Rug
from items.doors import Doors
from items.fireplace import Fireplace
from items.logbook import Logbook
from items.pipe_case import PipeCase
from items.animals import Animals
from items.curtains import Curtains
from items.trophies import Trophies
from items.chair import Chair

from items.safe import Safe
from items.side_table import SideTable

class GameRoom_Room(Detail_Room):

    def __init__(self):
        description = """
The first thing that enters your head is that this is like an old-fashioned man cave. It's a
lounge, it's a game room, it's a hunting lodge, all in one. From where you are by the doors,
a beautiful clock stands in the corner to your left. The left wall is decorated with stuffed
and mounted animal heads, and in the upper left corner is a hefty safe. The centre of the
room has a card table with four chairs, sitting on a beautiful old rug. 

On the far wall are two curtains, drawn back to reveal not a window, but an enormous artwork. 
The right wall is made up of a fireplace and shelves; these shelves are lined with various 
trophies, and perched right above the fire is a remarkable antique rifle. In front of the 
fire is a single chair with a small side table next to it."""

        Detail_Room.__init__(self, description)

        self.title = 'The Game Room'
        self.name = 'game_room'

        chairs = Chairs('a few chairs', 'chairs')
        card_table = Card_Table('a card table', 'card_table')
        clock = Clock('a clock', 'clock')
        rifle = Rifle('an old rifle', 'rifle')
        painting = Painting('a large painting', 'painting')
        self.doors = Doors('large ornate doors', 'doors')
        rug = Rug('a large rug', 'rug')
        fireplace = Fireplace('a fireplace', 'fireplace')
        # logbook = Logbook('a logbook', 'logbook')
        # pipe_case = PipeCase('a pipe case', 'pipe_case')
        animals = Animals('mounted animals', 'animals')
        curtains = Curtains('curtains', 'curtains')
        side_table = SideTable('a side table', 'side_table')
        trophies = Trophies('trophies', 'trophies')
        chair = Chair('a chair', 'chair')
        safe = Safe('a safe', 'safe')

        self.items = Bag([
            rifle, painting, card_table, clock,
            curtains, self.doors, fireplace, animals,
            rug, side_table, safe,
            chairs, trophies, chair
        ])

    def enter(self):
        self.doors.locked = True
        print("""
        %s%sAfter entering the room, the doors swing closed behind you and lock!%s""" % (fg('white'), attr('bold'), attr('reset')))

    def exit(self, direction):
        if (direction == 'west' and self.doors.locked == True):
            print("%s%sThe doors are locked tight! You can't get out!%s" % (fg('white'), attr('bold'), attr('reset')))
            return False
        else:
            print('The doors are unlocked and you can exit the room freely')
            return True
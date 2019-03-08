from adventurelib import *
from detail_room import *

import rooms.kitchen

class BackOfHouse_Room(Detail_Room):

    def __init__(self):
        description = """
You do a quick circle around the house. Just as you reach what looks like an open back
door, your phone gives a shrill ring – just one, before cutting out again. You must have
gotten a bar of reception for a second there! You look at the screen: Bill the historian. He
must be trying to find you. Which means he's probably around here somewhere. Well, this
back door is open... and even if Bill isn't inside, your phone might have a better chance of
working on the upper floors. It feels a bit weird entering without permission, but hey, this
might be your house soon, so it's not like you're trespassing. It's more of an open house
inspection.

You can enter the house through the back door to the north."""

        Detail_Room.__init__(self, description)

        self.title = 'Back of the House'
        self.name = 'back_of_house'

        # Links to other rooms
        self.north = rooms.kitchen.Kitchen_Room()
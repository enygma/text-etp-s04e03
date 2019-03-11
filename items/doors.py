from detail_item import *

class Doors(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.locked = False
        self.takeable = False
        self.description = """
The huge double doors are locked and not budging no matter how much pressure
you put on them. They're ornately decorated with three-dimensional patterned wood, and
when you look up at the very top corners, you see two little hooks, almost as if a curtain
used to hang here. To your dismay, you don't see a keyhole anywhere."""

    def open(self):
        if self.locked:
            print("You try to open the doors but they won't budge. You're locked in!")
            return False
        else:
            print('The doors are open!')
            return True
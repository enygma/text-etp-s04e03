from detail_item import *
from colored import fg, bg, attr

class Rifle(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.take_count = 0
        self.takeable = True
        self.description = """
From afar, it looks like a really valuable piece that any museum would want.
Whether it still works after all this time, you couldn't say."""

    def take(self):
        if self.take_count == 0:
            self.take_count += 1
            print("""
    %s%sYou stand on your toes to reach it, but as soon as you stretch out one arm, you feel a frigid wind envelope you. 
    And then there's a voice in your ear...

    “Nobody touches the master's weapon but the master,” it snarls. “You touch it, I'll shoot you myself.”

    And then it's gone. You move your arm; nothing stops you. But maybe you shouldn't play
    with guns unless you know what you're doing.%s
    """ % (fg('white'), attr('bold'), attr('reset')))
            return False
        else:
            print("%s%sNo ghostly voices talk to you this time.%s" % (fg('white'), attr('bold'), attr('reset')))
            return True

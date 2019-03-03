from detail_item import *
from colored import fg, bg, attr

rifle = Detail_Item('an old rifle', 'rifle')
rifle.takeable = True
rifle.description = """
From afar, it looks like a really valuable piece that any museum would want.
Whether it still works after all this time, you couldn't say."""

take_count = 0

def check_take():
    global take_count

    if take_count == 0:
        take_count += 1
        print("""
%s%s“Nobody touches the master's weapon but the master,” it snarls. “You touch it, I'll shoot
you myself.”

And then it's gone. You move your arm; nothing stops you. But maybe you shouldn't play
with guns unless you know what you're doing.%s
""" % (fg('white'), attr('bold'), attr('reset')))
        return False
    else:
        print("%s%sNo ghostly voices talk to you this time.%s" % (fg('white'), attr('bold'), attr('reset')))
        return True

rifle.take = check_take
from detail_item import *
import inventory
import complete

class Clock(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.match_time = '6:55:59'
        self.takeable = False
        self.description = """
It isn't a grandfather clock, but it isn't much smaller than one. It's working, and is
at least close to the correct time, but it may have slowed down over the years. Unlike most
old clocks you know, this one has three hands rather than just two: an hour hand, a
minute hand and a second hand. As far as you can tell it doesn't have any fancy internal
workings you can pry at, but on the back, right behind the face, you do find three holes,
as narrow as a coat hanger wire."""

        self.actions.append({
            "match": "set time to TIME",
            "method": "action_settime"
        })
        self.load_actions()

    def action_settime(self, time):
        # Make sure they have the pipe and the traps
        if "pipe" in inventory.inv: and "traps" in inventory.inv:
            if time == self.match_time:
                print("""Inserting the thin pipe into the holes on the back of the clock, you 
spin the hands one by one until they match the noises made by the traps – until you reach 
the time 6:55 and 59 seconds. Then you let go, and it starts ticking by itself again. The 
second hand slides up one spot: 6:56.""")

                complete.finish()

            else:
                print("""You use the thin pipe in the holes on the back of the clock to set 
the time to {} but not much seems to happen.""".format(time))

        else:
            print("You can't reach the clock hands so you'll need something else to change the time.")
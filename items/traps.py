from detail_item import *

class Traps(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.takeable = False
        self.description = """
The traps are a bit old and rusty. They take a lot of effort to prise open. 

The first one you try is a nightmare; every time you pull it a little bit it makes a bunch of 
high, quick  ticking noises that remind you of a bomb about to go off. It takes so many pulls 
you start  counting them. 59. 59 times you have to pull on it and hear that noise before the 
thing finally opens and stays open. 

You move on to the second trap. This one's almost exactly as bad: the  noise it makes is a bit slower, 
less frantic and bomb-like, but it still takes 55 pulls before  you can get it open. 

The final trap is much better, though: it only takes 6 tries, and the noise  it makes is slow and 
low-pitched, so it sounds much less alarming. Now you have three active  bear traps. Er... maybe you 
shouldn't mess around with those."""

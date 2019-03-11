from detail_item import *

class Rug(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.takeable = False
        self.description = """
The rug is large, grey and rectangular, with loopy tassels in all the corners. The
pattern on it isn't very interesting: it's just a grid of squares, not even different colours.
Just grey squares."""
from detail_item import *

class Curtains(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.takeable = False
        self.rope_cut = False
        self.description = """
From what you can see, the curtains are thick and velvety and cream-coloured.
They're tied up in two bunches on either side of the artwork, and the ropes keeping them
there are hopelessly knotted."""

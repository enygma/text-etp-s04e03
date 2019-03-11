from detail_item import *

class Pipe(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.takeable = True
        self.description = """
A long thin white pipe, seemingly made from ivory."""

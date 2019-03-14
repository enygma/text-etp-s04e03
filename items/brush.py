from detail_item import *

class Brush(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.takeable = True
        self.description = """
A very small, very fine brush. Like a make-up brush – or a police fingerprinting brush."""

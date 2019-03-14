from detail_item import *

class WhitePowder(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.takeable = True
        self.description = """
Sooty powder on the bottom of the fireplace"""

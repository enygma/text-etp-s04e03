from detail_item import *

class Key(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.takeable = True
        self.description = """
A small key that looks the perfect size to open something small"""

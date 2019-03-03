from adventurelib import *

class Detail_Item(Item):
    description = "It doesn't seem to be anything special."
    takeable = True
    
    def __init__(self, name, *aliases, takeable=True):
        self.takeable = takeable
        Item.__init__(self, name, *aliases)


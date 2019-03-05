from adventurelib import *

class Detail_Item(Item):
    description = "It doesn't seem to be anything special."
    takeable = True

    actions = []
    
    def __init__(self, name, *aliases, takeable=True):
        self.actions = []
        self.takeable = takeable
        Item.__init__(self, name, *aliases)


    def load_actions(self):
        return True

    def unload_actions(self):
        return True
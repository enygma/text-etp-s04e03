from adventurelib import *

class Detail_Room(Room):
    description = "There's not much here to look at"
    
    def __init__(self, description=None):
        if description:
            self.description = description

        self.title = "Nowhere"
        self.items = Bag()
        self.name = "just_a_place"

        Room.__init__(self, self.description)


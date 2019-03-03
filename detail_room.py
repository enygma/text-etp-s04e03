from adventurelib import *

class Detail_Room(Room):
    description = "There's not much here to look at"
    title = 'Nowhere'
    items = Bag()
    
    def __init__(self, description):
        Room.__init__(self, description)


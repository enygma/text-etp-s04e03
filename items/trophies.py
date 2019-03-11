from detail_item import *

class Trophies(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.takeable = False
        self.description = """
There's a collection of miscellaneous small trophies, no names, no placements,
just your generic old awards. But evenly spaced between them are four very impressive
trophies, at least twice the size of the others. You read the engravings on them:

- Smithfield's Experimental Solar Energy Corporation award: bird category.
- Elias Johnson Automotive Industries award: predator category.
- Anderson Bank honorary award: pest hunting category.
- Julia Jones' Jeweller sponsorship award for fishing."""

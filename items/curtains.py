from detail_item import *
import inventory

class Curtains(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.takeable = False
        self.rope_cut = False

        self.description = """
From what you can see, the curtains are thick and velvety and cream-coloured.
They're tied up in two bunches on either side of the artwork, and the ropes keeping them
there are hopelessly knotted."""

    def action_cutropes(self):
        # be sure they have the knife
        if "knife" in inventory.inv:
            self.rope_cut = True

            print("""The knife cuts through the knots easily and
the curtains come loose. Now that they are, you can see a small pattern of pictures sewn
into the fabric. The left curtain has a dollar sign and a sun, and the right curtain has a
wheel and a bright red ruby. If you draw the curtains, these pictures form a neat, straight line.""")

            self.description = """From what you can see, the curtains are thick and velvety and cream-coloured.
The left curtain has a dollar sign and a sun, and the right curtain has a
wheel and a bright red ruby. If you draw the curtains, these pictures form a neat, straight line."""

        else:
            print("You don't seem to have anything to cut the ropes with! Maybe look around for something sharp.")

        
        return True
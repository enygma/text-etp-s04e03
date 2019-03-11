from detail_item import *

class Test_Item(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)

        self.description = "My test item"
        self.actions.append({
            "match": "throw test", 
            "method": "action_throw"
        })

    def action_throw(self):
        print('throwing the chairs')
        
from adventurelib import *
from adventurelib import _register
from adventurelib import commands

class Detail_Item(Item):
    description = "It doesn't seem to be anything special."
    takeable = True

    actions = []
    
    def __init__(self, *args, **kwargs):
        self.actions = []
        if "takeable" in kwargs:
            self.takeable = takeable

        name = args[0]
        Item.__init__(self, name, *args)


    def load_actions(self):
        actions = self.actions
        if len(actions) > 0:
            for action in actions:
                # See if the command already exists
                found = False
                for command in commands:
                    if command[0].orig_pattern == action['match']:
                        found = True

                if found == False:
                    func = getattr(self, action['method'])
                    _register(action['match'], func)

        return True

    def unload_actions(self):
        return True
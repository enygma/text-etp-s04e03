from detail_item import *
from colored import fg, bg, attr
import adventurelib

chairs = Detail_Item('a few chairs', 'chairs')
chairs.takeable = False
chairs.description = """
They're four standard chairs, all tucked in neatly where players would sit at the table."""
chairs.actions.append('arrange chairs')

def action_arrage():
    print('arrange the chairs')
    return True

def load_actions():
    adventurelib._register('arrange chairs', action_arrage)

    return False

def unload_actions():
    for command in list(adventurelib.commands):
        
        # Unload our "arrange chairs" action
        if command[0].orig_pattern == 'arrange chairs':
            print('>> deleting')
            adventurelib.commands.remove(command)
    
    return False

chairs.load_actions = load_actions
chairs.unload_actions = unload_actions
from adventurelib import *
import os
from colored import fg, bg, attr
import json

## Import all of our rooms
from rooms.outside import *
from rooms.back_of_house import *

# Print welcome banner
f = open('./welcome.md', 'r')
print(f.read())

inventory = Bag()

def save_progress(current_room, inventory):
    data = {
        'current_room': current_room.name
    }
    f = open('./save.json', 'w')
    f.write(json.dumps(data))
    f.close()
    return True

def load_save():
    if (os.path.isfile('./save.json')):
        print('Loading save file...')

        f = open('./save.json', 'r')
        contents = json.loads(f.read())
        exec('set_current_room('+contents['current_room']+')')
    return True

def set_current_room(room):
    global current_room
    current_room = room

## Commands
@when('look')
@when('l')
def look():
    print ("\n%s%s > %s %s\n" % (fg('white'), attr('bold'), current_room.title, attr(0)))
    print("{}\n".format(str(current_room)))

    # Output the items
    if current_room.items:
        item_names = ', '.join(str(x) for x in current_room.items)
        print(f'There is {item_names} here.')

    # display the exits
    if current_room.exits():
        exit_directions = ', '.join(current_room.exits())

        print(f"You can go {exit_directions} from here.")
    else:
        print(f"There's no way out - you're stuck!")


@when('look at ITEM')
def look_item(item):
    obj = inventory.find(item)
    if not item:
        print(f"You do not have {item}.")
    else:
        print(f"It's a sort of {obj.color}-ish color.")

@when('take ITEM')
def take(item):
    obj = inventory.take(item)
    if not obj:
        print(f"Tou do not have a {item}.")
    else:
        print(f"You take the {obj}.")
        inventory.add(item)

@when('inventory')
def show_inventory():
    print("You have:")
    if not inventory:
        print('nothing')
        return
    
    for item in inventory:
        print(f"* {item}")


@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
@when('n', direction='north')
@when('s', direction='south')
@when('e', direction='east')
@when('w', direction='west')
def go(direction):
    global current_room
    room = current_room.exit(direction)
    if room:
        set_current_room(room)
        print(f"You go {direction}")
        save_progress(current_room, inventory)
        look()
    else:
        print("You can't go that way.")

## @todo implement restart command to remove the save file

## Boot the game
current_room = outside
load_save()

save_progress(current_room, inventory)
look()

start()
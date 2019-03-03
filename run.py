from adventurelib import *
import os
from colored import fg, bg, attr
import json
import sys

## Import the initial room
from rooms.outside import *

# Print welcome banner
f = open('./welcome.md', 'r')
print(f.read())

inventory = Bag()
default_room = outside

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
        print('%s%s%s Loading save file... %s' % (fg('white'), attr('bold'), bg(28), attr(0)))

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
    print ("\n%s%s == %s == %s\n" % (fg('white'), attr('bold'), current_room.title, attr(0)))
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
    i = globals()[item]
    print(i.description)

@when('take ITEM')
def take(item):
    # Try and get it from the current room's items
    if current_room.items.find(item) == None:
        print(f"You don't see {item} here.")
    else:
        obj = None

        for i in list(current_room.items):
            if item in i.aliases:
                obj = current_room.items.take(item)

        if not obj:
            print(f"You can't find {item}.")
        elif obj and not obj.takeable:
            print(f"You don't seem to be able to take that.")
            current_room.items.add(obj)
        else:
            print(f"You take the {obj}.")
            inventory.add(obj)

@when('drop ITEM')
def drop(item):
    if item in inventory:
        for i in list(inventory):
            if item in i.aliases:
                obj = inventory.take(item)
                current_room.items.add(obj)
    else:
        print("You don't have {item}")

@when('inventory')
def show_inventory():
    print("You have:")
    if not inventory:
        print('nothing')
        return
    
    for item in inventory:
        print(f"* {item}")

@when('reset')
def reset():
    if (os.path.isfile('./save.json')):
        os.remove('./save.json')
        print('%s%s Resetting! Sending you back to the start! %s' %
            (fg('white'), attr('bold'), attr('reset')))
        set_current_room(default_room)
        look()

@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
# @when('n', direction='north')
# @when('s', direction='south')
# @when('e', direction='east')
# @when('w', direction='west')
def go(direction):
    global current_room
    room = current_room.exit(direction)
    if room:
        set_current_room(room)
        print(f"%s%s%s>> You go {direction}  > %s" % (fg('white'), bg(56), attr('bold'), attr('reset')))
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

try:
    start()
except Exception as e:
    if '--debug' in sys.argv:
        print('%s%s%s **** DEBUG ****%s' % (fg(232), attr('bold'), bg(197), attr('reset')))
        print(e)
        print('')
    else:
        print("Oops, something isn't quite right...")
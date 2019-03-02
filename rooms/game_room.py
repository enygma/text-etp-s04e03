from adventurelib import *

game_room = Room("""
The first thing that enters your head is that this is like an old-fashioned man cave. It's a
lounge, it's a game room, it's a hunting lodge, all in one. From where you are by the doors,
a beautiful clock stands in the corner to your left. The left wall is decorated with stuffed
and mounted animal heads, and in the upper left corner is a hefty safe. The centre of the
room has a card table with four chairs, sitting on a beautiful old rug. 

On the far wall are two curtains, drawn back to reveal not a window, but an enormous artwork. 
The right wall is made up of a fireplace and shelves; these shelves are lined with various 
trophies, and perched right above the fire is a remarkable antique rifle. In front of the 
fire is a single chair with a small side table next to it.
""")

game_room.name = 'game_room'
game_room.title = "The Game Room"

rifle = Item('an old rifle', 'rifle')

game_room.items = Bag([rifle])



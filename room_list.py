# import rooms.kitchen
# import rooms.outside

# kitchen = rooms.kitchen.Kitchen_Room()
# outside = rooms.outside.Outside_Room()

from rooms.kitchen import Kitchen_Room
from rooms.outside import Outside_Room
from rooms.game_room import GameRoom_Room

game_room = GameRoom_Room()
kitchen = Kitchen_Room()
outside = Outside_Room()

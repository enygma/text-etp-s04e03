from detail_item import *
import room_list
import formatting
from items.pipe_case import PipeCase

class SideTable(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.takeable = False
        self.description = """
It's a round table made of flimsy but well-polished wood."""

    def look(self):
        print("Sitting on it is a small, brown box. Judging by its size and shape, you believe it's a %s%scase%s made to hold a pipe." % formatting.highlight)

        pipe_case = PipeCase('pipe case', 'pipe_case', 'case')
        room_list.game_room.items.add(pipe_case)

        return True
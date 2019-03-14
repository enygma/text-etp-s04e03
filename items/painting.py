from detail_item import *
import room_list
import formatting

class Painting(Detail_Item):

    def __init__(self, name, aliases):
        Detail_Item.__init__(self, name, aliases)
        
        self.takeable = False
        self.seen_pattern = False
        self.description = """
The painting is of two men standing in this very room, standing proudly with
guns slung over their shoulders. The eyes of one of the men seem to be looking in various
directions, but you've heard of that optical illusion before. The background of the painting
includes most of the room exactly as it is now. The only odd thing is the card table, or
rather, the chairs around it. Two of them are tucked in neatly, but two are spun around
the wrong way, and one of these is tilted back on two legs, leaning against the edge of the
table."""

    def look(self):
        chairs = room_list.game_room.items.find('chairs')
        
        if not chairs.arranged:
            print('Looking at the painting, you wonder if %s%sarranging%s the chairs to match would be useful.' % formatting.highlight)
            chairs.actions.append({
                "match": "arrange chairs", 
                "method": "action_arrange"
            })
            chairs.load_actions()

        else:
            print("The chairs at the card table are now matching the ones in the painting.")

            print("""You notice something else odd about the painting. You watch the painted man's eyes, and there's 
no doubt about it: even when you're not moving, they are.  They're not just following you. They seem to be glancing up. 
Then they peer off to the left. Then they roll up again, and then off to the right. Up once more, and right once more. 
Then they drop down. Then, they... well, they sort of vibrate. Like they're shaking in place as fast as they can.""")
            self.seen_pattern = True

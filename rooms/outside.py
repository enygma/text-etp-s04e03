from adventurelib import *
from rooms.back_of_house import *

outside = Room("""
“Hi, this is Bill. We spoke earlier – Bill, from Culloden Manor? Listen, I’ve been calling you
because a few things have been going awry at the house tonight, and before we go in I’ll
need to explain them to you. It’s too much to get into over the phone, but trust me, you’ll want
to hear it. It’s got car crashes, doors that lock themselves, ice cream that literally screams...
sorry. I shouldn’t laugh. This is actually quite serious. Please, for your own safety, call me
back as soon as you get this.”

Still no service. You've really got to move to a new phone carrier. You've had no bars since
the city centre, and even though the manor is on a steep hill, you've got nothing. How are
you supposed to meet the historian who invited you here if you can't contact him?
You look up and take in the sight of the Culloden Manor. It's in pretty good shape for a
place so old; the haunted house tours must make good money. You wonder if you'd be
allowed to move in if you got some share of the ownership.

To the east you can continue around to the back of the house.
""")

outside.name = 'outside'
outside.title = "Outside the House"
outside.items = Bag()
outside.east = back_of_house
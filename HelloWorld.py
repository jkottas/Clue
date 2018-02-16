from clue_interfaces import *
from player_example import *
from clue_constants import *

print(list(Cards))

print(Cards.Ballroom is Rooms.Ballroom) # false
print(Cards.Ballroom == Rooms.Ballroom) # true

for subclass in PlayerBase.__subclasses__():
	print(subclass.playername())
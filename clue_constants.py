from enum import Enum, IntEnum, auto

#class ClueConstants(object):
	# player starting locations

class MovementActions(Enum):
	Roll = auto()
	SecretPassage = auto() # only possible from the corner rooms
	Remain = auto() # only possible if a player has summoned you to a room with a suspicion

class Cards(IntEnum):
	Col_Mustard = 1
	Miss_Scarlet = 2
	Prof_Plum = 3
	Mr_Green = 4
	Mrs_White = 5
	Mrs_Peacock = 6
	Candlestick = 7
	Knife = 8
	Lead_Pipe = 9
	Revolver = 10
	Rope = 11
	Wrench = 12
	Ballroom = 13
	Billiard_Room = 14
	Conservatory = 15
	Dining_Room = 16
	Hall = 17
	Kitchen = 18
	Library = 19
	Lounge = 20
	Study = 21

class Suspects(IntEnum):
	Col_Mustard = 1
	Miss_Scarlet = 2
	Prof_Plum = 3
	Mr_Green = 4
	Mrs_White = 5
	Mrs_Peacock = 6

class Weapons (IntEnum):
	Candlestick = 7
	Knife = 8
	Lead_Pipe = 9
	Revolver = 10
	Rope = 11
	Wrench = 12

class Rooms (IntEnum):
	Ballroom = 13
	Billiard_Room = 14
	Conservatory = 15
	Dining_Room = 16
	Hall = 17
	Kitchen = 18
	Library = 19
	Lounge = 20
	Study = 21


import abc
from clue_constants import *

class PlayerBase(object):
	@abc.abstractmethod
	def playername():
		# used for display only
		return "doofus"

	def init(playerUID, startinghand, playerstates):
		# playerUID will be how you are identified for the entire game
		# startinghand is a list of Cards, known only to you
		# playerstates is a list of PlayerState, which includes PlayerUID, color, player order, number of cards in hand, and pawn identity
		return

	def choosemovementaction(playerstates, possiblemovementactions):
		# this method will be called at the start of your turn, even if you have only one possible movement action
		# return the movement action you would like to take
		return MovementActions.Roll

	def move(diceroll):
		# diceroll is the number rolled on the dice 1-6. Indicate your desired ending square
		# this method will only be called if you chose the Roll MovementAction
		return "3,4"

	def suspect():
		# return the Character and Weapon card you would like to suspect, or None.
		# the room you are in will automatically be added to your suspect list.
		# this method will only be called if you end your turn in different room from last turn.
		return {Cards.Miss_Scarlet, Cards.Candlestick}

	def accuse():
		# return the Character, Weapon, and Room card you would like to accuse, or None.
		# guessing wrong will result in a loss.
		return None


from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.game.players import RandomComputerPlayer
from tic_tac_toe.logic.models import Mark

from console.renderers import ConsoleRenderer


players1 = RandomComputerPlayer(Mark("X"))
players2 = RandomComputerPlayer(Mark("O"))

TicTacToe(players1, players2, ConsoleRenderer()).play()

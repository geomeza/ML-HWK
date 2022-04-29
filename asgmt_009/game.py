import math
import random

class Game:

  def __init__(self, q_table = None):
    self.state = (0, False)
    self.mulligan = False
    self.game_over = False
    if q_table is None:
      self.q_table = { (1, False): [1,1,1], (1, True): [1,1, None], (2, False): [2,1,1], \
      (3, False): [3, -3, 1], (3, True): [3,-3, None]}

  def take_turn(self, action):
    if action == "stop":
      self.game_over = True
      return self.state
    roll = random.randint(1,3)
    if (roll + self.state[0]) > 3:
      if action != "mulligan":
        self.state = (-3, self.mulligan)
        self.game_over = True
      else:
        self.mulligan = True
        self.state = (self.state[0], self.mulligan)
    else:
      if action == "mulligan":
        self.mulligan = True
        self.state = (self.state[0], self.mulligan)
      else
        self.state = (self.state[0] + roll, self.mulligan)
    return self.state



def q_learning_algo(self, )

def g
game = Game()
print(game.state, game.q_table)
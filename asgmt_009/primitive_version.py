import math
import random

class Game:

  def __init__(self, update_vals, q_table = None):
    self.score = 0
    self.old_score = None
    self.game_over = False
    self.update_vals = update_vals
    if q_table is None:
      self.q_table = [[1,1], [2,1], [3,-3]]

  def take_turn(self, action):
    if action == "stop":
      self.game_over = True
      return self.score
    self.old_score = self.score
    roll = random.randint(1,3)
    if (roll + self.score) > 3:
      self.score = -3
      self.game_over = True
      return self.state
    else:
      self.score = self.score + roll
    return self.score

  def update_vals(self, action):
    if self.score == 3:
      return      
    self.take_turn(action)
    row_to_update = self.q_table[self.old_score]
    max_val = max(row_to_update)
    expected_val = row_to_upodate[-1]
    row_to_update[-1] = 
    

game = Game()
game.take_turn()
print(game.state, game.q_table)
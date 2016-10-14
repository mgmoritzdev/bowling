class Frame:
  """ A turn of a player with 2 balls, 
    if strike it skips the second throw and add points from 2 next throws, 
    if spare, it add points from 1 next throw. """

  def __init__(self):
    self.points = 0
    self.throws = 0
    self.extraBalls = 0
    self.finished = False

  def throw(self, pins):
    if self.finished:
      self.sumExtraPoints(pins)
      return

    self.throws += 1
    self.points += pins
    self.finished = self.throws == 2 or self.points == 10
    self.extraBalls = (1 if self.points == 10 else 0) * (2 if self.throws == 1 else 1)

  def sumExtraPoints(self, pins):
    if (self.extraBalls > 0):
      self.points += pins
      self.extraBalls -= 1
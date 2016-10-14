import frame
import throwBallException

class Game:

  totalFrames = 10

  def __init__(self):
    self.frames = []
    self.frames.append(frame.Frame())

  def throw(self, pins):
    self.updateCurrentFrame()
    
    if self.gameEnded():
      raise throwBallException.ThrowBallException('Unable to throw a ball after game ended')    
    
    self.frames[-1].throw(pins)    
    for frame in self.frames[0:len(self.frames)-1]:
      frame.sumExtraPoints(pins)
    
  def updateCurrentFrame(self):
    if self.frames[-1].finished and len(self.frames) < 10:
      self.frames.append(frame.Frame())

  def getScore(self):
    return reduce(lambda x, y: x + y, map(lambda x: x.points, self.frames))

  def gameEnded(self):
    return len(self.frames) == 10 and self.frames[-1].finished == True and self.frames[-1].extraBalls == 0
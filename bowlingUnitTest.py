import unittest
import bowling
import throwBallException

class SimpleBowlingTestCase(unittest.TestCase):
  def setUp(self):
    self.longMessage = True
    self.game = bowling.Game()

class RegularGameTestCase(SimpleBowlingTestCase):
  def runTest(self):
    self.game.throw(1)
    self.game.throw(4)
    self.game.throw(4)
    self.game.throw(5)
    self.game.throw(6)
    self.game.throw(4)
    self.game.throw(5)
    self.game.throw(5)
    self.game.throw(10)
    self.game.throw(0)
    self.game.throw(1)
    self.game.throw(7)
    self.game.throw(3)
    self.game.throw(6)
    self.game.throw(4)
    self.game.throw(10)
    self.game.throw(2)
    self.game.throw(8)
    self.game.throw(6)
    self.assertEqual(self.game.getScore(), 133, 'Wrong score')    

class AlmostPerfectGameTestCase(SimpleBowlingTestCase):
  def runTest(self):
    for x in range(0, 11):
      self.game.throw(10)
    self.game.throw(9)
    self.assertEqual(self.game.getScore(), 299, 'Wrong score')

class PerfectGameTestCase(SimpleBowlingTestCase):
  def runTest(self):
    for x in range(0, 12):
      self.game.throw(10)
    self.assertEqual(self.game.getScore(), 300, 'Wrong score')

class ExceededNumberOfThrowsInGameTestCase(SimpleBowlingTestCase):
  def runTest(self):
    for x in range(0, 20):
      self.game.throw(0)
    self.assertEqual(self.game.getScore(), 0, 'Wrong score')
    
    with self.assertRaises(throwBallException.ThrowBallException):
      self.game.throw(1)

if __name__ == '__main__':
  unittest.main()
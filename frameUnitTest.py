import unittest
import frame

class SimpleFrameTestCase(unittest.TestCase):
  def setUp(self):
    self.longMessage = True
    self.frame = frame.Frame()

class FrameNoMarkTestCase(SimpleFrameTestCase):
  def runTest(self):
    self.frame.throw(3)
    self.frame.throw(4)
    self.frame.throw(8) # ignored
    self.assertEqual(self.frame.points, 7, 'Wrong score')
    self.assertEqual(self.frame.extraBalls, 0, 'Wrong extra balls')

class FrameSpareBeforeExtraBallTestCase(SimpleFrameTestCase):
  def runTest(self):
    self.frame.throw(6)
    self.frame.throw(4)
    self.assertEqual(self.frame.points, 10, 'Wrong score')
    self.assertEqual(self.frame.extraBalls, 1, 'Wrong extra balls')

class FrameSpareAfterExtraBallTestCase(SimpleFrameTestCase):
  def runTest(self):
    self.frame.throw(6)
    self.frame.throw(4)
    self.frame.throw(3)
    self.frame.throw(7) # ignored
    self.assertEqual(self.frame.points, 13, 'Wrong score')
    self.assertEqual(self.frame.extraBalls, 0, 'Wrong extra balls')

class FrameStrikeBeforeExtraBallsTestCase(SimpleFrameTestCase):
  def runTest(self):
    self.frame.throw(10)
    self.assertEqual(self.frame.points, 10, 'Wrong score')
    self.assertEqual(self.frame.extraBalls, 2, 'Wrong extra balls')


class FrameStrikeAfterFirstExtraBallTestCase(SimpleFrameTestCase):
  def runTest(self):
    self.frame.throw(10)
    self.frame.throw(10)
    self.assertEqual(self.frame.points, 20, 'Wrong score')
    self.assertEqual(self.frame.extraBalls, 1, 'Wrong extra balls')


class FrameStrikeAfterSecondExtraBallTestCase(SimpleFrameTestCase):
  def runTest(self):
    self.frame.throw(10)
    self.frame.throw(7)
    self.frame.throw(3)
    self.frame.throw(6) # ignored
    self.assertEqual(self.frame.points, 20, 'Wrong score')
    self.assertEqual(self.frame.extraBalls, 0, 'Wrong extra balls')


if __name__ == '__main__':
  unittest.main()
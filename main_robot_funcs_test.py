
from unittest import *
import unittest
from main_robot_funcs import *

class TestMovement(unittest.TestCase):

	def setUp(self):
		pass

	def test_R1move3D(self):
		self.assertEqual(test_move_1.r1move3D(90,120,30),(90,120,30))
		self.assertEqual(test_move_1.r1move3D(45,45,45),(45,45,45))

	def test_R2move2D(self):
		self.assertEqual(test_move_1.r2move2D(0,90),(0,90))
		self.assertEqual(test_move_1.r2move2D(0,180),(0,180))

	def test_R3move3D(self):
		self.assertEqual(test_move_1.r3move3D(90,120,30),(90,120,30))
		self.assertEqual(test_move_1.r3move3D(45,45,45),(45,45,45))


if __name__ == '__main__':
	testor_1 = Movement(0,0,1,1)
	testor_2 = Movement(0,0,0,0)
	testor_3 = Movement(1,1,2,2)
	
	test_move_1 = SpaceFrame()
	unittest.main()
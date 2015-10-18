'''
Making up Wyke's robot movements and actions in python
Author  : Neal Bazirake
Date  	: 07/22/2015

Description : This is a wide API that would be used to generalize the 
movements of motars in a given movement streak.

NOTE 1:
While thinking about the motor movements, all we need to think about 
is the movement of the;
	1. BALL AND SOCKET Movement
	2. HINGE MOVEMENT

NOTE 2:
We have to layout a kind of geo-grid probably a 3D-mini geo-grid on which the 
element will move. However, initially, i will layout a 2D- grid on ground on 
which this element will ride and we will name this a tile.

'''



import math
#import RPI.GPIO as GPIO

#ACTIONS
'''
	PREFACE
	
	MAKE SIMULATION:
		1. import numpy
		2. import kinematics

	IN THIS CASE WE ARE TALKING ABOUT THE MOTOR movements

		1. MOVING 180
		2. MOVING 90
		3. MOVING 360

	IN THIS CASE WE ARE TALKING ABOUT THE ENTIRE MACHINE
		1. WALKING
			   INTIAL:
			   	 A) All MOVEMENTS WILL BE SET TO 90' THUS ROBOT WILL BE IN LAY DOWN MODE.
			a. GETTING SIGNALS FROM EACH LEG 
				a) GET MOVEMENT OF R1 : BALL and SOCKET Joint
					a) Should move in 360'
				B) GET MOVEMENT OF R2
					a) Should MOVE 180'
					b) Should MOVE 90'
				C) GET MOVEMENT OF R3
					a) Should MOVE 360'
					b) Should MOVE 0' (only while intiating into flight)
			b. MOVING FORWARD
			c. MOVING BACKWARD
			d. MOVING LEFT
			e. MOVING RIGHT
			

		2. FLYING
			a. GETTING OFF GROUD
				- Starting motors
				- Moving about 1 meter off the ground
			b. MOVING LEFT
			c. MOVING RIGHT
			d. MOVING FORWARD
			e. RETURN BACK TO LAND DOWN

		3. SWIMMING
			a. GETTING INTO WATER
				-Curving in of TIRES	
				-Opening back propeler
			

		#4. DRIVING FORWARD : MAY BE SUBJECT TO CHANGE
			a. GETTING TIRES ONTO THE GROUND 
			b. MOVING FORWARD
			c. MOVING BACKWARD
			d. MOVING LEFT
			e. MOVING RIGHT 

		5. MEETING OBSTACLES
			a. DETECT MODE OF TRANSPORT
			b. DETECT TERRAIN
			   + Get height 
			c. GETTING BACK INTO OPTIMAL MOVING PROCESS.

		6. TRANFORMATION FROM ONE MODE OF TRANSPORT TO another



'''

class SpaceFrame():
	'''
	This class is supposed to put out the layout for geospace where robot will move
	To move towards the intial position just define a new position with intial movements.
	'''

	def __init__(self):
		self.x = 0
		self.y = 0
		self.z = 0

	def r1move3D(self,x,y,z):
		#This mimicks the shoulder or ball and socket
		return (self.x+x, self.y+y,self.z+z)

	def r2move2D(self,x,y):
		#This mimicks the human elbow in a hinge like momvemnt 
		# and shoudl mimick the ulna or radius
		self.x = 0
		self.y = 0
		return(self.x + x , self.y + y)

	def r3move3D(self,x,y,z):
		#This mimicks the human wrist
		#This also going to be a propulsion joint
		return (self.x+x, self.y+y,self.z+z)




class Walk():
	'''
	This class is supposed to support the movements that are controlled by the controllers from the 
	user to the breadboard. Needs; activated pin on breadboard, amount of volage. We are going to assume
	a constant amount of voltage is provided to a specific motor. We also have to think about the number
	'''
	def __init__(self):
		self.pin = 'Pin15'
		self.voltage = '15V'
		
	def moveForward(self):
		# 1. Switch on the particular breadboard PIN
		# 2. Intialize the legs to original position before movement.
		# 3. Send the necessary voltage
		pass

	def moveBackward(self):
		# 1. Switch on the particular breadboard PIN
		# 2. Intialize the legs to original position before movement.
		# 3. Send the necessary voltage
		pass

	def turnLeft(self):
		# 1. Switch on the particular breadboard PIN
		# 2. Intialize the legs to original position before movement.
		# 3. Send the necessary voltage
		pass

	def turnRight(self):
		# 1. Switch on the particular breadboard PIN
		# 2. Intialize the legs to original position before movement.
		# 3. Send the necessary voltage
		pass



class Movement():

	def __init__(self, xposFrom, yposFrom, xposTo, yposTo):
		self.xposFrom = xposFrom
		self.yposFrom = yposTo
		self.xposTo = xposTo
		self.yposTo = yposTo
		
	def moveElement(self,oldPos,newPos):

		pass

	def nomovedMethod(self):
		#Boolean checker that something moved
		return (self.xposFrom == self.xposTo) and (self.yposFrom == self.yposTo)

	def moveRight(self):
		pass

	def moveLeft(self):
		pass

#class LegMovement(self):
#	'''This class supports the movement of an entire leg from the start to finsih
#    '''






if __name__ == '__main__':
	#ansi = MovementMotar()
	#print(ansi.back_to_origin())
	ThreeDFrame()

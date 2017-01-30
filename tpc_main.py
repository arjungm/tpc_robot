import cozmo
import requests
from enum import Enum

class Action(Enum):
	LEFT = 1
	RIGHT = 2
	FORWARD = 3
	REVERSE = 4

def fetch_next_command():
	...

def cozmo_left(robot: cozmo.robot.Robot):
	robot.turn_in_place(degrees(30)).wait_for_completed()

def cozmo_right(robot: cozmo.robot.Robot):
	robot.turn_in_place(degrees(-30)).wait_for_completed()

def cozmo_forward(robot: cozmo.robot.Robot):
	robot.drive_straight( distance_mm(70), speed_mmps(50) ).wait_for_complete()

def cozmo_backward(robot: cozmo.robot.Robot):
	robot.drive_straight( distance_mm(-70), speed_mmps(50) ).wait_for_complete()


def main(robot: cozmo.robot.Robot)
	while(true):
		if(command==LEFT):
			cozmo_left()
		elif(command==RIGHT):
			cozmo_right()
		elif(command==FORWARD):
			cozmo_forward()
		elif(command==REVERSE):
			cozmo_backward()
		sleep(0.5)

cozmo.run_program(main)

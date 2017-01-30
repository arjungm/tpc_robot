#!/usr/bin/env python3

import cozmo
import requests

def cozmo_left(robot: cozmo.robot.Robot):
	robot.turn_in_place(degrees(30)).wait_for_completed()

def cozmo_right(robot: cozmo.robot.Robot):
	robot.turn_in_place(degrees(-30)).wait_for_completed()

def cozmo_forward(robot: cozmo.robot.Robot):
	robot.drive_straight( distance_mm(70), speed_mmps(50) ).wait_for_complete()

def cozmo_backward(robot: cozmo.robot.Robot):
	robot.drive_straight( distance_mm(-70), speed_mmps(50) ).wait_for_complete()


def main(robot: cozmo.robot.Robot)
	command=1
	while(true):
		if(command==1):
			cozmo_left()
		elif(command==2):
			cozmo_right()
		elif(command==3):
			cozmo_forward()
		elif(command==4):
			cozmo_backward()
		command = command + 1
		sleep(0.5)

cozmo.run_program(main)

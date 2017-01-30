import cozmo
import requests

def fetch_next_command()


def cozmo_left(robot: cozmo.robot.Robot)
	robot.turn_in_place(degrees(30)).wait_for_completed()

def cozmo_right(robot: cozmo.robot.Robot)
	robot.turn_in_place(degrees(-30)).wait_for_completed()

def cozmo_forward(robot: cozmo.robot.Robot)
	robot.drive_straight( distance_mm(70), speed_mmps(50) ).wait_for_complete()

def cozmo_backward(robot: cozmo.robot.Robot)
	robot.drive_straight( distance_mm(-70), speed_mmps(50) ).wait_for_complete()


def main(robot: cozmo.robot.Robot)
	


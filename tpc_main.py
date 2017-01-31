#!/usr/bin/env python3

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import requests
import time

def fetch_next_command():
  print('fetching next command')
  r = requests.get('http://cozmo-commander.herokuapp.com/queue').json()
  return r['instruction']

def cozmo_left(robot: cozmo.robot.Robot):
  print('turning left')
  robot.turn_in_place(degrees(30)).wait_for_completed()

def cozmo_right(robot: cozmo.robot.Robot):
  print('turning right')
  robot.turn_in_place(degrees(-30)).wait_for_completed()

def cozmo_forward(robot: cozmo.robot.Robot):
  print('moving forward')
  robot.drive_straight(distance_mm(70), speed_mmps(50)).wait_for_completed()

def cozmo_backward(robot: cozmo.robot.Robot):
  print('moving backward')
  robot.drive_straight(distance_mm(-70), speed_mmps(50)).wait_for_completed()


def main(robot: cozmo.robot.Robot):
  while(True):
    command = fetch_next_command()
    if(command=='!cc-l'):
      cozmo_left(robot)
    elif(command=='!cc-r'):
      cozmo_right(robot)
    elif(command=='!cc-f'):
      cozmo_forward(robot)
    elif(command=='!cc-b'):
      cozmo_backward(robot)
    else:
      print('cannot match the command "{}" to a comzo capability'.format(command))
    time.sleep(3)

cozmo.run_program(main)

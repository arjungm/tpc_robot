#!/usr/bin/env python3

import cozmo
import requests

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
  robot.drive_straight(distance_mm(70), speed_mmps(50)).wait_for_complete()

def cozmo_backward(robot: cozmo.robot.Robot):
  print('moving backward')
  robot.drive_straight(distance_mm(-70), speed_mmps(50)).wait_for_complete()


def main(robot: cozmo.robot.Robot):
  command = fetch_next_command();
  while(true):
    if(command=='!cc-l'):
      cozmo_left()
    elif(command=='!cc-r'):
      cozmo_right()
    elif(command=='!cc-f'):
      cozmo_forward()
    elif(command=='!cc-b'):
      cozmo_backward()
    else:
      print('cannot match the command "{}" to a comzo capability'.format(command))
    sleep(0.5)

cozmo.run_program(main)

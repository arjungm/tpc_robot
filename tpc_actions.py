#!/usr/bin/env python3

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

def left(robot: cozmo.robot.Robot):
  print('turning left')
  robot.turn_in_place(degrees(30)).wait_for_completed()

def right(robot: cozmo.robot.Robot):
  print('turning right')
  robot.turn_in_place(degrees(-30)).wait_for_completed()

def forward(robot: cozmo.robot.Robot):
  print('moving forward')
  robot.drive_straight(distance_mm(70), speed_mmps(50)).wait_for_completed()

def backward(robot: cozmo.robot.Robot):
  print('moving backward')
  robot.drive_straight(distance_mm(-70), speed_mmps(50)).wait_for_completed()

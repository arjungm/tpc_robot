#!/usr/bin/env python3

import cozmo
import requests
import time

import tpc_actions
actions = tpc_actions

def fetch_next_command():
  print('fetching next command')
  r = requests.get('http://cozmo-commander.herokuapp.com/queue').json()
  return r['instruction']

def main(robot: cozmo.robot.Robot):
  while(True):
    command = fetch_next_command()
    if(command=='!cc-l'):
      actions.left(robot)
    elif(command=='!cc-r'):
      actions.right(robot)
    elif(command=='!cc-f'):
      actions.forward(robot)
    elif(command=='!cc-b'):
      actions.backward(robot)
    else:
      print('cannot match the command "{}" to a comzo capability'.format(command))
    time.sleep(3)

cozmo.run_program(main)

#!/usr/bin/python

import pygame
import daemon
import time
import pynotify
import os

def main():
  pygame.init()
  pygame.joystick.init()
  js = pygame.joystick.Joystick(0)
  js.init()
  pynotify.init("Joyvol")
  while True:
    for event in pygame.event.get():
      if event.type == pygame.JOYBUTTONDOWN:
        pynotify.Notification("UNMUTE", "Headphones stowed, unmuting speakers" ).show()
        os.system("amixer -q set 'Surround',0 100")
#        print "UNMUTE"
      if event.type == pygame.JOYBUTTONUP:
        pynotify.Notification("MUTE", "Headphones in use, muting speakers" ).show()
        os.system("amixer -q set 'Surround',0 0")
#        print "MUTE"
    time.sleep(.5)


#with daemon.DaemonContext():
#  main()    
main()

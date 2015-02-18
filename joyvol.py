#!/usr/bin/python

import pygame
import daemon
import time
import pynotify
import os
import argparse


def main():
    parser = argparse.ArgumentParser(description='JoyVol: control audio (or anything else really) based on joystick buttons')
    parser.add_argument('--js', dest='joystick_id', action='store_const',
                        const=sum, default=0,
                        help='the pygame ID of the joystick')
    parser.add_argument('--button', dest='button_id', action='store_const',
                        const=sum, default=0,
                        help='the pygame ID of the button')
    parser.add_argument('--libnotify', dest='libnotify', action='store_true')
    parser.add_argument('--no-libnotify', dest='libnotify', action='store_false')
    parser.set_defaults(libnotify=True)


    args = vars(parser.parse_args())

    pygame.init()
    pygame.joystick.init()
    js = pygame.joystick.Joystick(0)
    js.init()
    pynotify.init("Joyvol")
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.JOYBUTTONDOWN and
               event.dict['joy'] == args['joystick_id'] and
               event.dict['button'] == args['button_id']):
                os.system("amixer -q set 'Surround',0 100")
                if args['libnotify']:
                    pynotify.Notification("UNMUTE", "Headphones stowed, unmuting speakers" ).show()
            if (event.type == pygame.JOYBUTTONUP and
               event.dict['joy'] == args['joystick_id'] and
               event.dict['button'] == args['button_id']):
                os.system("amixer -q set 'Surround',0 0")
            	if args['libnotify']:
                	pynotify.Notification("MUTE", "Headphones in use, muting speakers" ).show()

        time.sleep(.5)


#with daemon.DaemonContext():
#  main()    
main()
